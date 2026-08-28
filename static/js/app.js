const messages = [
  "You are my calm in chaos.",
  "I choose you, always.",
  "You feel like home.",
  "Some feelings never fade."
];

function generate() {
  const msg = messages[Math.floor(Math.random()*messages.length)];
  document.getElementById("msg").innerText = msg;
}

const cards = document.querySelectorAll(".memory");

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
  });
}, {
  threshold: 0.3
});

cards.forEach(card => {
  observer.observe(card);
});
