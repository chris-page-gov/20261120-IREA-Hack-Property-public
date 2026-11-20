/* Static national estate screen. It reads reviewed, committed JSON only. */
(() => {
  const $ = id => document.getElementById(id);
  const format = new Intl.NumberFormat('en-GB');
  const fields = ['sector', 'region', 'usage', 'area', 'signal'];
  let dashboard, register, geography, page = 0;
  function value(row, field) { return field === 'area' ? row.areaCode : row[field]; }
  function baseMatch(row) {
    return ['sector', 'region', 'usage'].every(field => !$(field).value || value(row, field) === $(field).value);
  }
  function match(row) { return baseMatch(row) && (!$('area').value || row.areaCode === $('area').value); }
  function optionList(id, values) {
    const select = $(id); const first = select.firstElementChild;
    select.replaceChildren(first);
    [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b, 'en-GB')).forEach(value => {
      const option = document.createElement('option'); option.value = value; option.textContent = value; select.append(option);
    });
  }
  function numberMetric(label, count, extra) {
    const block = document.createElement('div'); block.className = 'metric';
    const strong = document.createElement('strong'); strong.textContent = format.format(count);
    block.append(strong, document.createTextNode(label));
    if (extra) { const small = document.createElement('div'); small.className = 'small'; small.textContent = extra; block.append(small); }
    return block;
  }
  function selectedCells() { return dashboard.queries.area_cells.rows.filter(match); }
  function areaStats() {
    const stats = new Map();
    dashboard.queries.area_cells.rows.filter(baseMatch).forEach(row => {
      const code = row.areaCode || '';
      if (!stats.has(code)) stats.set(code, { code, name: row.onsArea || 'Unassigned', estate: 0, prompts: 0 });
      const current = stats.get(code);
      current.estate += row.records;
      current.prompts += Number(row.poorWithNia) + Number(row.unratedLargeNia);
    });
    return stats;
  }
  function renderMetrics(cells) {
    const estate = cells.reduce((sum, row) => sum + row.records, 0);
    const prompts = cells.reduce((sum, row) => sum + Number(row.poorWithNia) + Number(row.unratedLargeNia), 0);
    const rated = cells.reduce((sum, row) => sum + Number(row.poorWithNia), 0);
    const missing = cells.reduce((sum, row) => sum + Number(row.unratedLargeNia), 0);
    const measured = cells.reduce((sum, row) => sum + Number(row.niaUsable), 0);
    $('metrics').replaceChildren(
      numberMetric('estate workbook rows', estate),
      numberMetric('usable measured-area rows', measured),
      numberMetric('investigation prompts', prompts),
      numberMetric('E–G rating and area', rated),
      numberMetric('large area, rating absent', missing)
    );
  }
  function areaColour(count, max) {
    if (!count) return '#dfe9e9';
    const t = Math.log1p(count) / Math.log1p(Math.max(max, 1));
    const start = [169, 218, 209], end = [7, 94, 112];
    return '#' + start.map((n, i) => Math.round(n + (end[i] - n) * t).toString(16).padStart(2, '0')).join('');
  }
  function selectArea(code) { $('area').value = code; page = 0; render(); $('area').focus(); }
  function renderAreas(stats) {
    const svg = $('area-map'); svg.replaceChildren();
    const max = Math.max(...[...stats.values()].map(row => row.prompts), 1);
    geography.areas.forEach(area => {
      const row = stats.get(area.code) || { name: area.name, estate: 0, prompts: 0 };
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', area.path);
      path.setAttribute('fill', areaColour(row.prompts, max));
      path.setAttribute('role', 'button'); path.setAttribute('tabindex', '0');
      path.setAttribute('aria-label', `${area.name}: ${format.format(row.prompts)} investigation prompts; select area`);
      if ($('area').value === area.code) { path.setAttribute('stroke', '#a84b00'); path.setAttribute('stroke-width', '1.6'); }
      const title = document.createElementNS('http://www.w3.org/2000/svg', 'title'); title.textContent = `${area.name}: ${format.format(row.prompts)} prompts`;
      path.append(title);
      path.addEventListener('click', () => selectArea(area.code));
      path.addEventListener('keydown', event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); selectArea(area.code); } });
      svg.append(path);
    });
    const rows = [...stats.values()].filter(row => row.code).sort((a, b) => b.prompts - a.prompts || a.name.localeCompare(b.name, 'en-GB'));
    const tbody = $('area-rows'); tbody.replaceChildren();
    rows.forEach(row => {
      const tr = document.createElement('tr');
      const name = document.createElement('td'); const button = document.createElement('button');
      button.type = 'button'; button.textContent = row.name; button.addEventListener('click', () => selectArea(row.code)); name.append(button);
      const estate = document.createElement('td'); estate.textContent = format.format(row.estate);
      const prompts = document.createElement('td'); prompts.textContent = format.format(row.prompts);
      const share = document.createElement('td'); share.textContent = row.estate ? `${(100 * row.prompts / row.estate).toFixed(1)}%` : '—';
      tr.append(name, estate, prompts, share); tbody.append(tr);
    });
    const other = stats.get('');
    $('unassigned').textContent = other ? `${format.format(other.estate)} workbook rows, including ${format.format(other.prompts)} prompts, have no assigned ONS area.` : '';
  }
  function filteredRecords() {
    const query = $('search').value.trim().toLocaleLowerCase('en-GB');
    return register.records.filter(item => {
      const row = item.screeningRecord;
      return match(row) && (!$('signal').value || row.signal === $('signal').value) &&
        (!query || `${row.propertyName} ${row.buildingReference} ${row.onsArea || ''}`.toLocaleLowerCase('en-GB').includes(query));
    });
  }
  function td(text) { const cell = document.createElement('td'); cell.textContent = text == null ? '—' : String(text); return cell; }
  function renderRegister() {
    const rows = filteredRecords();
    const pages = Math.max(1, Math.ceil(rows.length / 50)); page = Math.min(page, pages - 1);
    $('register-count').textContent = `${format.format(rows.length)} of ${format.format(register.records.length)} provisional records match these controls.`;
    const tbody = $('candidate-rows'); tbody.replaceChildren();
    rows.slice(page * 50, (page + 1) * 50).forEach(item => {
      const row = item.screeningRecord;
      const tr = document.createElement('tr');
      tr.append(
        td(`${row.propertyName} (${row.buildingReference})`),
        td(`${row.onsArea || 'Area unassigned'} · ${row.region} · ${row.usage}`),
        td(row.floorAreaM2 == null ? 'Not recorded' : `${format.format(row.floorAreaM2)} m²`),
        td(`${row.epcBand} / ${row.decBand}`), td(row.signal),
        td(item.reportedTenureClass.replaceAll('_', ' '))
      ); tbody.append(tr);
    });
    $('page-status').textContent = `Page ${page + 1} of ${pages}`;
    $('previous').disabled = page === 0; $('next').disabled = page >= pages - 1;
  }
  function render() { renderMetrics(selectedCells()); renderAreas(areaStats()); renderRegister(); }
  async function load() {
    try {
      const urls = ['data/dashboard.json', 'data/candidates.json', 'data/ons-area-map.json'];
      const responses = await Promise.all(urls.map(url => fetch(url)));
      responses.forEach((response, i) => { if (!response.ok) throw new Error(`Could not load ${urls[i]}`); });
      [dashboard, register, geography] = await Promise.all(responses.map(response => response.json()));
      optionList('sector', dashboard.queries.building_cells.rows.map(row => row.sector));
      optionList('region', dashboard.queries.building_cells.rows.map(row => row.region));
      optionList('usage', dashboard.queries.building_cells.rows.map(row => row.usage));
      const areaNames = new Map(geography.areas.map(row => [row.code, row.name]));
      const areaSelect = $('area');
      [...areaNames].sort((a, b) => a[1].localeCompare(b[1], 'en-GB')).forEach(([code, name]) => {
        const option = document.createElement('option'); option.value = code; option.textContent = name; areaSelect.append(option);
      });
      fields.forEach(field => $(field).addEventListener('change', () => { page = 0; render(); }));
      $('search').addEventListener('input', () => { page = 0; renderRegister(); });
      $('previous').addEventListener('click', () => { page--; renderRegister(); });
      $('next').addEventListener('click', () => { page++; renderRegister(); });
      render();
    } catch (error) {
      $('metrics').textContent = 'The reviewed data could not be loaded. Open the register download or try again later.';
      console.error(error);
    }
  }
  document.addEventListener('DOMContentLoaded', load);
})();
