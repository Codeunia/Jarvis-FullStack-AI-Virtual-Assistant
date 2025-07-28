
const torch = document.getElementById("torch");

document.addEventListener("mousemove", (e) => {
    const x = e.clientX + "px";
    const y = e.clientY + "px";
    torch.style.setProperty("--x", x);
    torch.style.setProperty("--y", y);
});

window.addEventListener("DOMContentLoaded", () => {
  const nav = document.getElementById("nav-buttons");

  // Delay slightly after typewriter (e.g., 2200ms)
  setTimeout(() => {
    nav.style.opacity = "1";
    nav.style.pointerEvents = "auto";
  }, 3200);
});

const pages = {
      "wake up": "home.html",
    };

    window.onload = () => {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

      if (!SpeechRecognition) {
        alert("Speech Recognition not supported in this browser.");
        return;
      }

      const recognition = new SpeechRecognition();
      recognition.lang = "en-US";
      recognition.interimResults = false;
      recognition.maxAlternatives = 1;

      recognition.start();

      recognition.onresult = (event) => {
        const command = event.results[0][0].transcript.toLowerCase();
        console.log("Heard:", command);

        for (let keyword in pages) {
          if (command.includes(keyword)) {
            window.location.href = pages[keyword];
            return;
          }
        }

        alert("Sorry, no page found for command: " + command);
      };

      recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
      };
    };