// function hello(name) {
//     console.log("Hello "+name);
// }
// function addnum(num1,num2)
// {
//     console.log(num1+num2);
// }
// function helloSomeone(name="Vaibhav") {
//     console.log("Hello "+name);
// }
// function formal(name="sam" ,title="sir"){
//     console.log(title+" "+name);
// }
// function formal(name="sam" ,title="sir"){
//     return title+" "+name;
// }
// function timesfive(num){
//     var result = num*5;
//     return result;
// }
var v = "Global V";
var stuff = "Global Stuff"

function fun(stuff){
    console.log(v);
    stuff="Reassign stuff inside fun"
    console.log(stuff);
}
fun();
console.log(stuff);