var of = prompt("Would you like to start web app? y/n");
var namelist = [];
//var namelist = new Array();
function add(random){
    namelist.push(random);
}
function remove(){
    namelist.pop();
}
function display(){
    for(letter of namelist){
        console.log(letter);
    }
}
function quit(){
    alert("Thanks for using the Web App! Please refesh the page to start again");
}
function webapp(){
    var action = prompt("please select an action add,remove,display,or quit");
    if(action === "add"){
        var name = prompt("What name would you like to add");
        add(name);
        webapp();
    }
    if(action === "remove"){
        remove();
        webapp();
    }
    if(action === "display"){
        display();
        webapp();
    }
    if(action === "quit"){
        quit();
    }
}
if (of === "n"){
    quit();
}
if (of === "y"){
    webapp();
}