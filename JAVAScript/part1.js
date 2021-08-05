var first = prompt("Enter the first Name: ");
var last = prompt("Enter the last Name: ");
var age = prompt("Enter your age here: ");
var height = prompt("Enter you height here: ");
var pet = prompt("Enter your pet Name: ");

var namcon = null;
var agecon = null;
var heicon = null;
var petcon = null;

if (first[0] == last[0]) {
    namcon=true;
}else{
    namcon=false;
}

if (age>=20 && age<=30) {
    agecon=true;
}else{
    agecon=false;
}

if (height>=170) {
    heicon=true;
}else{
    heicon=false;
}

if (pet[pet.length-1]=="y") {
    petcon=true;
}else{
    petcon=false;
}

if (namcon && agecon && heicon && petcon) {
    console.log("Now U Are Spy");
}