const events = [
  ['00:00.82', 'model.request', 'Plan research workflow', '820ms', 'ok'],
  ['00:05.12', 'tool.call', 'browser.search', '4.3s', 'ok'],
  ['00:05.24', 'memory.write', 'Persist source summary', '120ms', 'ok'],
  ['00:07.04', 'tool.call', 'filesystem.write', '1.8s', 'warn'],
  ['00:18.42', 'model.response', 'Compose final answer', '620ms', 'ok']
];
document.querySelector('#timeline').innerHTML = events.map(event => `<div class="event ${event[4] === 'warn' ? 'warn' : ''}"><small>${event[0]}</small><span><b>${event[1]}</b><br>${event[2]}</span><small>${event[3]} · ${event[4]}</small></div>`).join('');
