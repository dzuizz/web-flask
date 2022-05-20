// Rock Paper Scissors
function start_round(move) {
    let computer_move = Math.floor((Math.random() * 3) + 1);
    
    if (move == "rock") {
        $("#rock").addClass("selected");
        $("#paper").removeClass("selected");
        $("#scissors").removeClass("selected");
    } else if (move == "paper") {
        $("#paper").addClass("selected");
        $("#rock").removeClass("selected");
        $("#scissors").removeClass("selected");
    } else if (move == "scissors") {
        $("#scissors").addClass("selected");
        $("#rock").removeClass("selected");
        $("#paper").removeClass("selected");
    }

    if (move == "rock") {
        if (computer_move == 1) {
            $("#result").html("You tied!");
        } else if (computer_move == 2) {
            $("#result").html("You lost!");
        } else if (computer_move == 3) {
            $("#result").html("You won!");
        }
    } else if (move == "paper") {
        if (computer_move == 1) {
            $("#result").html("You won!");
        } else if (computer_move == 2) {
            $("#result").html("You tied!");
        } else if (computer_move == 3) {
            $("#result").html("You lost!");
        }
    } else if (move == "scissors") {
        if (computer_move == 1) {
            $("#result").html("You lost!");
        } else if (computer_move == 2) {
            $("#result").html("You won!");
        } else if (computer_move == 3) {
            $("#result").html("You tied!");
        }
    }
}