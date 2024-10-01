
let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let isGameActive = true;
const resultText = document.getElementById("resultText");
const endGame = document.querySelector(".end_game");

const xImage = '<img src="images/x.png" alt="X">';
const oImage = '<img src="images/o.png" alt="O">';

const winConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
];

function cellClicked(event) {
  const cell = event.target;
  const cellIndex = parseInt(cell.id);

  if (board[cellIndex] !== "" || !isGameActive) {
    return;
  }

  updateBoard(cell, cellIndex);
  checkForWinner();
}

function updateBoard(cell, index) {
  board[index] = currentPlayer;
  
  if (currentPlayer === "X") {
    cell.innerHTML = xImage;
  } else {
    cell.innerHTML = oImage;
  }

  cell.classList.add(currentPlayer);
}

function swapPlayer() {
  currentPlayer = currentPlayer === "X" ? "O" : "X";
}

function checkForWinner() {
  let roundWon = false;

  for (let i = 0; i < winConditions.length; i++) {
    const condition = winConditions[i];
    const a = board[condition[0]];
    const b = board[condition[1]];
    const c = board[condition[2]];

    if (a === "" || b === "" || c === "") {
      continue;
    }

    if (a === b && b === c) {
      roundWon = true;
      break;
    }
  }

  if (roundWon) {
    resultText.textContent = `${currentPlayer} wins!`;
    isGameActive = false;
    showEndGame();
    return;
  }

  if (!board.includes("")) {
    resultText.textContent = "It's a draw!";
    isGameActive = false;
    showEndGame();
    return;
  }

  swapPlayer();
}

function start_game() {
  board = ["", "", "", "", "", "", "", "", ""];
  currentPlayer = "X";
  isGameActive = true;
  resultText.textContent = "";

  document.querySelectorAll(".cell").forEach(cell => {
    cell.innerHTML = ""; // Clear images
    cell.classList.remove("X");
    cell.classList.remove("O");
  });

  hideEndGame();
}

function showEndGame() {
  endGame.style.display = "block";
}

function hideEndGame() {
  endGame.style.display = "none";
}

document.querySelectorAll(".cell").forEach(cell => {
  cell.addEventListener("click", cellClicked);
});
