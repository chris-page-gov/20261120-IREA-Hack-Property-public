'use strict';

for (const input of document.querySelectorAll('[data-filter]')) {
  const id = input.dataset.filter;
  const rows = [...document.querySelectorAll('#' + id + ' tbody tr')];
  const status = document.querySelector('[data-filter-status="' + id + '"]');
  const result = document.getElementById(id + '-result');
  if (status) {
    const labels = new Set(rows.map(row => row.cells[1].textContent.trim()));
    for (const label of [...labels].sort()) status.add(new Option(label, label));
  }
  const update = () => {
    const text = input.value.trim().toLocaleLowerCase('en-GB');
    let visible = 0;
    for (const row of rows) {
      const inText = row.textContent.toLocaleLowerCase('en-GB').includes(text);
      const inStatus = !status || !status.value || row.cells[1].textContent.trim() === status.value;
      row.hidden = !(inText && inStatus);
      if (!row.hidden) visible++;
    }
    const label = id === 'areas' ? 'area' : 'question';
    if (result) result.textContent = visible + ' ' + label + (visible === 1 ? '' : 's');
  };
  input.addEventListener('input', update);
  if (status) status.addEventListener('change', update);
  update();
}
