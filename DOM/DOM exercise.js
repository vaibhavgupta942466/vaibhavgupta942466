//Restart game Button
var restart = document.querySelector("#custom_button");
//Grab all The Squares
var squares = document.querySelectorAll("#ram");
//clear all the squares

function clearboard(){
    for(var i = 0; i < squares.length ;i++){
        squares[i].textContent = ' ';
    }
}

console.log(squares.length)