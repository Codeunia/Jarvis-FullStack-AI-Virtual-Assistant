const evtSource = new EventSource("/stream");
const terminal = document.getElementById("terminal-output");
evtSource.onmessage = function (event) {
  const line = event.data;
  const htmlLine = document.createElement("div");
  htmlLine.textContent = `> ${line}`;
  terminal.appendChild(htmlLine);
  terminal.scrollTop = terminal.scrollHeight;
};
