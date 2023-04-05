const startBtn = document.querySelector('#start-btn');
const instruction = document.querySelector('#instruction');
const message = document.querySelector('#message');

startBtn.addEventListener('click', () => {
  startBtn.disabled = true;
  instruction.textContent = 'Breathe in... hold... breathe out...';
  let breathCount = 0;
  const breathInterval = setInterval(() => {
    breathCount++;
    if (breathCount === 10) {
      clearInterval(breathInterval);
      message.textContent = 'You won! You maintained a calm state for 10 seconds.';
    } else if (breathCount % 4 === 1) {
      instruction.textContent = 'Breathe in...';
    } else if (breathCount % 4 === 3) {
      instruction.textContent = 'Breathe out...';
    }
  }, 1000);
});
