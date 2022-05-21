// Rock Paper Scissors
var randomGuess, userGuess, userScore = 0, computerScore = 0, scissors, paper, stone;

choices = {
	"Rock": 1,
	"Paper": 2,
	"Scissors": 3,
};

function move(move) {
	userGuess = move;
	document.getElementById("rock").classList.remove("outline-4 scale-150");
	document.getElementById("paper").classList.remove("outline-4 scale-150");
	document.getElementById("scissors").classList.remove("outline-4 scale-150");
	document.getElementById(move).classList.add("outline-4 scale-150");
}

function round() {
	randomGuess = Math.floor(Math.random() * 3) + 1;

	if (userGuess === randomGuess) {
		document.getElementById("result").innerHTML = "This is a draw.";
	} else if (userGuess === "rock" && randomGuess === 2) {
		document.getElementById("result").innerHTML = "You have won, scissors will cut paper up.";
	} else if (userGuess === "paper" && randomGuess === 1) {
		document.getElementById("result").innerHTML = "The computer has won, scissors will cut paper up.";
	} else if (userGuess === "paper" && randomGuess === 3) {
		document.getElementById("result").innerHTML = "You have won, paper will wrap up rocks.";
	} else if (userGuess === "scissors" && randomGuess === 2) {
		document.getElementById("result").innerHTML = "The computer has won, paper will wrap up rocks.";
	} else if (userGuess === "scissors" && randomGuess === 1) {
		document.getElementById("result").innerHTML = "You have won, rocks will break scissors.";
	} else if (userGuess === "rock" && randomGuess === 3) {
		document.getElementById("result").innerHTML = "The computer has won, rocks will break scissors.";
	} else if (userGuess === "" && userGuess === null) {
		document.getElementById("result").innerHTML = "You have not entered your choice.";
	}
}