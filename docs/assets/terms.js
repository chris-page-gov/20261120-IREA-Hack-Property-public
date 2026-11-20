/* Short, contextual definitions for technical material. No data leaves the page. */
(() => {
  const terms = {
    EPC: 'Energy Performance Certificate: an assessed building energy rating, usually from A (best) to G (worst). Check the certificate date and the premises it covers.',
    DEC: 'Display Energy Certificate: a rating based on recorded operational energy use for a public building. It differs from an EPC.',
    NIA: 'Net internal area: measured usable floor area within a building. This screen uses the workbook’s IPMS 3 measure where it exceeds 1 square metre.',
    IPMS: 'International Property Measurement Standards: a defined way to measure floor area. IPMS 3 is the net internal area basis used here.',
    IMD: 'Index of Multiple Deprivation: a relative ranking of neighbourhoods. Decile 1 is the most deprived tenth within the relevant nation.',
    LSOA: 'Lower layer super output area: a small statistical area used to publish English Census and deprivation data.',
    UPRN: 'Unique Property Reference Number: an identifier for an addressable location. A UPRN alone does not prove ownership or match a whole building.',
    NGD: 'National Geographic Database: Ordnance Survey’s detailed geographic data. This public site does not retrieve or contain licensed NGD building extracts.',
    OGL: 'Open Government Licence: a UK public sector reuse licence. It normally requires source attribution and does not cover excluded third-party rights.',
    ONS: 'Office for National Statistics: the source of the administrative boundaries used for the national area comparison.',
    PSGA: 'Public Sector Geospatial Agreement: a licence for eligible public sector use of Ordnance Survey data. It is distinct from an open data licence.'
  };
  const pattern = new RegExp('\\b(' + Object.keys(terms).join('|') + ')\\b', 'g');
  const blocked = 'A,BUTTON,ABBR,CODE,PRE,SCRIPT,STYLE,TEXTAREA,SUMMARY';
  let activeButton = null;
  const panel = document.createElement('aside');
  panel.id = 'term-panel'; panel.className = 'term-panel'; panel.hidden = true;
  panel.setAttribute('aria-labelledby', 'term-panel-heading');
  panel.innerHTML = '<div class="close-row"><button type="button" aria-label="Close definition">Close</button></div><p class="eyebrow">Technical term</p><h2 id="term-panel-heading"></h2><p class="term-definition"></p>';
  const closeButton = panel.querySelector('button');
  function closePanel() {
    panel.hidden = true;
    if (activeButton) { activeButton.setAttribute('aria-expanded', 'false'); activeButton.focus(); activeButton = null; }
  }
  closeButton.addEventListener('click', closePanel);
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && !panel.hidden) closePanel(); });
  function showTerm(button, term) {
    if (activeButton) activeButton.setAttribute('aria-expanded', 'false');
    activeButton = button; button.setAttribute('aria-expanded', 'true');
    panel.querySelector('h2').textContent = term;
    panel.querySelector('.term-definition').textContent = terms[term];
    panel.hidden = false; closeButton.focus();
  }
  function addHelp(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.parentElement || node.parentElement.closest(blocked) || node.parentElement.closest('[data-no-terms]')) continue;
      if (pattern.test(node.textContent)) nodes.push(node);
      pattern.lastIndex = 0;
    }
    nodes.forEach(node => {
      const fragment = document.createDocumentFragment(); let last = 0;
      node.textContent.replace(pattern, (match, term, offset) => {
        fragment.append(document.createTextNode(node.textContent.slice(last, offset)));
        const button = document.createElement('button');
        button.type = 'button'; button.className = 'term-button'; button.textContent = term;
        button.setAttribute('aria-label', `What does ${term} mean?`);
        button.setAttribute('aria-expanded', 'false');
        button.setAttribute('aria-controls', panel.id);
        button.addEventListener('click', () => showTerm(button, term));
        fragment.append(button); last = offset + match.length;
        return match;
      });
      fragment.append(document.createTextNode(node.textContent.slice(last)));
      node.replaceWith(fragment);
    });
  }
  document.addEventListener('DOMContentLoaded', () => {
    document.body.append(panel);
    document.querySelectorAll('main, .technical-terms').forEach(addHelp);
  });
})();
