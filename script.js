// Define the game levels
const levels = [
    {
      timeLimit: 10, // Time limit for level 1
      successThreshold: 60, // Percentage of successful clicks required to pass level 1
      challengeText: 'Click the button as fast as you can!', // Challenge text for level 1
    },
    {
      timeLimit: 8, // Time limit for level 2
      successThreshold: 75, // Percentage of successful clicks required to pass level 2
      challengeText: 'Click the button as fast as you can, but be careful not to miss!', // Challenge text for level 2
    },
    {
      timeLimit: 6, // Time limit for level 3
      successThreshold: 90, // Percentage of successful clicks required to pass level 3
      challengeText: 'Click the button as fast as you can, but avoid the red button!', // Challenge text for level 3
    },
  ];
  
  let currentLevel = 0;
  let score = 0;
  
  // Select the button element
  const button = document.querySelector('#click-button');
  
  // Add a click event listener to the button
  button.addEventListener('click', handleClick);
  
  // Define the handleClick function
  function handleClick() {
    // Increment the score
    score++;
  
    // If the button is red, decrement the score
    if (button.classList.contains('red')) {
      score--;
    }
  
    // Update the score display
    updateScoreDisplay();
  
    // If the player has clicked the button enough times, advance to the next level
    if (score >= levels[currentLevel].successThreshold) {
      advanceToNextLevel();
    }
  }
  
  // Define the advanceToNextLevel function
  function advanceToNextLevel() {
    // If there are no more levels, end the game
    if (currentLevel >= levels.length - 1) {
      endGame();
      return;
    }
  
    // Otherwise, advance to the next level
    currentLevel++;
  
    // Display the challenge text for the new level
    const challengeText = document.querySelector('#challenge-text');
    challengeText.textContent = levels[currentLevel].challengeText;
  
    // Reset the score and update the score display
    score = 0;
    updateScoreDisplay();
  
    // Reset the button color
    button.classList.remove('red');
    button.classList.add('green');
  
    // Set the time limit for the new level
    setTimeLimit(levels[currentLevel].timeLimit);
  }
  
  // Define the endGame function
  function endGame() {
    // Display the game over message
    const gameOverText = document.querySelector('#game-over-text');
    gameOverText.textContent = 'Game Over';
  
    // Hide the button and challenge text
    button.style.display = 'none';
    challengeText.style.display = 'none';
  }
  
  // Define the setTimeLimit function
  function setTimeLimit(seconds) {
    // Clear any existing timers
    clearInterval(timer);
  
    // Set the time limit
    let timeLeft = seconds;
    const timerDisplay = document.querySelector('#timer');
    timerDisplay.textContent = timeLeft;
  
    // Start the timer
    const timer = setInterval(() => {
      timeLeft--;
      timerDisplay.textContent = timeLeft;
  
      // If the time runs out, end the game
      if (timeLeft <= 0) {
        endGame();
        clearInterval(timer);
      }
    }, 1000);
  }
  
  // Define the updateScoreDisplay function
  function updateScoreDisplay() {
    const scoreDisplay = document.querySelector('#score');
    scoreDisplay.textContent = score;
  }
  