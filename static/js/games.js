// Rock Paper Scissors
var computer_move, user_move, userScore = 0, computerScore = 0;

choices = {
	"Rock": 1,
	"Paper": 2,
	"Scissors": 3,
};

function move(move) {
	user_move = move;
	document.getElementById("rock").classList.remove('outline', 'scale-110', 'font-xl', 'decoration-indigo-900');
	document.getElementById("paper").classList.remove('outline', 'scale-110', 'font-xl', 'decoration-indigo-900');
	document.getElementById("scissors").classList.remove('outline', 'scale-110', 'font-xl', 'decoration-indigo-900');
	document.getElementById(move).classList.add('outline', 'scale-110', 'font-xl', 'decoration-indigo-900');
}

function start_round() {
	computer_move = Math.floor(Math.random() * 3) + 1;

	// * User vs Computer
	if (user_move == "rock") {
		if (computer_move == 1) { // * Rock vs Rock
			document.getElementById("result-text").innerHTML = "It's a tie!";
		} else if (computer_move == 2) { // * Rock vs Paper
			document.getElementById("result-text").innerHTML = "The computer has won, paper will wrap rock up.";
		} else { // * Rock vs Scissors
			document.getElementById("result-text").innerHTML = "You have won, rock will break scissors";
		}
	} else if (computer_move == "paper") {
		if (computer_move == 1) { // * Paper vs Rock
			document.getElementById("result-text").innerHTML = "You have won, paper will wrap rock up.";
		} else if (computer_move == 2) { // * Paper vs Paper
			document.getElementById("result-text").innerHTML = "It's a tie!";
		} else { // * Paper vs Scissors
			document.getElementById("result-text").innerHTML = "The computer has won, scissors will cut paper.";
		}
	} else {
		if (computer_move == 1) { // * Scissors vs Rock
			document.getElementById("result-text").innerHTML = "The computer has won, rock will break scissors.";
		} else if (computer_move == 2) { // * Scissors vs Paper
			document.getElementById("result-text").innerHTML = "You have won, scissors will cut paper.";
		} else { // * Scissors vs Scissors
			document.getElementById("result-text").innerHTML = "It's a tie!";
		}
	}
}