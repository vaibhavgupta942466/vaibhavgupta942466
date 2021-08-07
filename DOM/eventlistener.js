var headone = document.querySelector("#one");
var headtwo = document.querySelector("#two");
var headthree = document.querySelector("#three")

headone.addEventListener("mouseover",function(){
    headone.textContent = "Mouse Currently Over";
    headone.style.color = "Red";
})
headone.addEventListener("mouseout",function(){
    headone.textContent = "Hover Over Me:";
    headone.style.color = "Black";
})

headtwo.addEventListener("click",function(){
    headtwo.textContent = "Clicked On";
    headtwo.style.color = "Blue";
})