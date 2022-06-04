let button = document.getElementById("sheesh");
let h1 = document.getElementById("sheesh-text");

let count = 0;

button.addEventListener('click', function () {
    if (count == 0) button.innerHTML = "Are you sure?";
    else if (count == 1) {
        button.innerHTML = "You have been warned...";
        for (let i = 1; i <= 20; i++) {
            h1.innerHTML += "SIUUUU! ";
            if (!(i%2)) h1.innerHTML += "<br>";
        }
    }
    count++;
});