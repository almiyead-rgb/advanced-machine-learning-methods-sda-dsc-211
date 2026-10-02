(() => {
  'use strict';
  const labels = JSON.parse(document.getElementById('ui-labels').textContent);
  const locale = document.documentElement.lang;
  const scoreInputs = [document.getElementById('technical-score'), document.getElementById('presentation-score')];
  const result = document.getElementById('grade-result');
  const format = n => new Intl.NumberFormat(locale, {maximumFractionDigits:2}).format(n);
  function calculate() {
    const raw = scoreInputs.map(input => input.value.trim());
    if (raw.some(value => value === '')) {
      result.textContent = labels.calcEmpty;
      result.dataset.state = 'empty';
      scoreInputs.forEach(input => input.removeAttribute('aria-invalid'));
      return;
    }
    const valid = scoreInputs.map((input,i) => /^\d+(?:\.\d{1,2})?$/.test(raw[i]) && input.validity.valid);
    scoreInputs.forEach((input,i) => input.setAttribute('aria-invalid', String(!valid[i])));
    if (!valid.every(Boolean)) {
      result.textContent = labels.calcInvalid;
      result.dataset.state = 'invalid';
      return;
    }
    // Integer hundredths avoid floating-point boundary errors at70 and95.
    const cents = raw.map(value => Math.round(Number(value) * 100)).reduce((a,b) => a+b,0);
    const state = cents >= 9500 ? 'distinction' : cents >= 7000 ? 'pass' : 'fail';
    const label = state === 'distinction' ? labels.calcDistinction : state === 'pass' ? labels.calcPass : labels.calcFail;
    result.textContent = `${format(cents/100)} / ${format(100)} — ${label}`;
    result.dataset.state = state;
  }
  document.getElementById('grade-calculator').addEventListener('submit', event => event.preventDefault());
  scoreInputs.forEach(input => input.addEventListener('input', calculate));
  const checks = [...document.querySelectorAll('[data-check]')];
  const key = 'sda-dsc-211-readiness-v1';
  let storageAvailable = true;
  function unavailable() {
    storageAvailable = false;
    const notice = document.getElementById('storage-note');
    notice.textContent = labels.storage;
    notice.hidden = false;
  }
  try {
    const saved = JSON.parse(localStorage.getItem(key) || '[]');
    if (Array.isArray(saved)) checks.forEach(check => { check.checked = saved.includes(check.dataset.check); });
  } catch (_) { unavailable(); }
  function updateProgress(save) {
    const selected = checks.filter(check => check.checked).map(check => check.dataset.check);
    document.getElementById('readiness-progress').value = selected.length;
    document.getElementById('progress-text').textContent = `${format(selected.length)} / ${format(checks.length)} ${labels.done}`;
    if (save && storageAvailable) {
      try { localStorage.setItem(key,JSON.stringify(selected)); } catch (_) { unavailable(); }
    }
  }
  checks.forEach(check => check.addEventListener('change', () => updateProgress(true)));
  document.getElementById('reset-progress').addEventListener('click', () => {
    checks.forEach(check => { check.checked = false; });
    updateProgress(true);
  });
  updateProgress(false);
  const terms = [...document.querySelectorAll('[data-term]')];
  const normalize = value => value.normalize('NFKD').replace(/[ً-ٰٟ]/g,'').replace(/[أإآ]/g,'ا').replace(/(^|\s)ال(?=[\u0621-\u064a])/g,'$1').toLocaleLowerCase();
  document.getElementById('term-search').addEventListener('input', event => {
    const query = normalize(event.target.value.trim());
    terms.forEach(term => { term.hidden = !normalize((term.dataset.search || '') + ' ' + term.textContent).includes(query); });
    document.getElementById('no-results').hidden = terms.some(term => !term.hidden);
  });
  document.querySelector('[data-language]').addEventListener('click', event => {
    // Both languages share section IDs; keep the reader's location.
    if (location.hash) event.currentTarget.href = event.currentTarget.href.split('#')[0] + location.hash;
  });
})();
