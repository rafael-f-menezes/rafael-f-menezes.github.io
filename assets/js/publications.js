// Renders data/publications.json into #pubs. Edit the JSON to update the list.
(function () {
  var TYPES = { article: 'Journal articles', preprint: 'Preprints', abstract: 'Conference abstracts' };
  var state = { filter: 'all', data: null };

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function sub(s) { return esc(s).replace(/([A-Za-z\)])(\d+)(?![\d.])/g, function (m, a, d) { return a + '<sub>' + d + '</sub>'; }); }
  function authors(list, self) {
    return list.map(function (a) {
      var isMe = self.some(function (p) { return a === p; });
      return isMe ? '<b>' + esc(a) + '</b>' : esc(a);
    }).join(', ');
  }
  function render() {
    var d = state.data, out = document.getElementById('pubs');
    var items = d.publications.filter(function (p) { return state.filter === 'all' || p.type === state.filter; });
    items.sort(function (a, b) { return b.year - a.year; });
    var n = items.length, html = '', lastYear = null;
    html += '<ol class="pubs">';
    items.forEach(function (p) {
      if (p.year !== lastYear) { html += '</ol><div class="pub-year">' + p.year + '</div><ol class="pubs">'; lastYear = p.year; }
      var doi = p.doi ? ' <a class="doi" href="https://doi.org/' + esc(p.doi) + '" target="_blank" rel="noopener">doi:' + esc(p.doi) + '</a>' : '';
      var kind = p.type === 'article' ? '' : ' <span class="muted">(' + (p.type === 'preprint' ? 'preprint' : 'conference abstract') + ')</span>';
      html += '<li data-n="' + (n--) + '"><span class="t">' + sub(p.title) + '</span>' + kind + '<br><span class="a">' + authors(p.authors, d.meta.self_patterns) + '</span><br><span class="v">' + esc(p.venue) + '</span> ' + esc(p.detail) + '.' + doi + '</li>';
    });
    html += '</ol>';
    out.innerHTML = html.replace('<ol class="pubs"></ol>', '');
  }
  function tabs() {
    var wrap = document.getElementById('pub-tabs');
    var keys = ['all', 'article', 'preprint', 'abstract'];
    var counts = { all: state.data.publications.length };
    state.data.publications.forEach(function (p) { counts[p.type] = (counts[p.type] || 0) + 1; });
    wrap.innerHTML = keys.map(function (k) {
      return '<button type="button" data-k="' + k + '" aria-pressed="' + (k === state.filter) + '">' + (k === 'all' ? 'All' : TYPES[k]) + ' (' + (counts[k] || 0) + ')</button>';
    }).join('');
    wrap.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      state.filter = b.getAttribute('data-k');
      Array.prototype.forEach.call(wrap.querySelectorAll('button'), function (x) { x.setAttribute('aria-pressed', x === b); });
      render();
    });
  }
  function metrics() {
    var m = state.data.meta, el = document.getElementById('metrics');
    if (!el) return;
    el.innerHTML = 'Google Scholar: ' + m.metrics.citations + ' citations, h-index ' + m.metrics.h_index + ' (' + esc(m.metrics.as_of) + '). ' +
      '<a href="' + esc(m.scholar) + '" target="_blank" rel="noopener">Scholar profile</a> · <a href="' + esc(m.orcid) + '" target="_blank" rel="noopener">ORCID</a>';
  }
  fetch('data/publications.json').then(function (r) { return r.json(); }).then(function (d) {
    state.data = d; metrics(); tabs(); render();
  }).catch(function () {
    document.getElementById('pubs').innerHTML = '<p>The list could not be loaded. See my <a href="https://scholar.google.com/citations?user=69vW21YAAAAJ&hl=en">Google Scholar profile</a>.</p>';
  });
})();
