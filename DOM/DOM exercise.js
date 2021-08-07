//Restart game Button
var restart = document.querySelector("#custom_button");
//Grab all The Squares
var squares = document.querySelectorAll(".ram");
//clear all the squares

function clearboard(){
    for(var i = 0; i < squares.length ;i++){
        squares[i].textContent = ' ';
    }
}

restart.addEventListener("click", clearboard);

// var cellone = document.querySelector('#a')
// cellone.addEventListener('click',function(){
//     if(cellone.textContent === " "){
//         cellone.textContent = "X";
//     }else if(cellone.textContent === "X"){
//         cellone.textContent = "0";
//     }else{
//         cellone.textContent = " ";
//     }
// })

function changemarker(){
    if(this.textContent === " "){
        this.textContent = "X";
    }else if(this.textContent === "X"){
        this.textContent = "0";
    }else{
        this.textContent = " ";
    }
}
for(var i = 0 ; i < squares.length ;i++){
    squares[i].addEventListener("click",changemarker)
}