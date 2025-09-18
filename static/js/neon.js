document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".neon-animation");
  
    function createParticle() {
      const particle = document.createElement("div");
      particle.classList.add("particle");
  
      const size = Math.random() * 6 + 4; // 4–10px
      particle.style.width = `${size}px`;
      particle.style.height = `${size}px`;
  
      // random horizontal start position
      particle.style.left = `${Math.random() * window.innerWidth}px`;
  
      container.appendChild(particle);
  
      // Remove after animation duration (6s + buffer)
      setTimeout(() => {
        particle.remove();
      }, 6500);
    }
  
    // spawn particles every 200ms
    setInterval(createParticle, 200);
  });