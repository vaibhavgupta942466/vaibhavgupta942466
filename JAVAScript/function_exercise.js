// PROBLEM 1: SLEEPING IN
//
// Write a function called sleepIn that takes in two boolean parameters: weekday
// and vacation.
//
// The parameter weekday is true if it is a weekday, and the parameter vacation is
// true if we are on vacation. We sleep in if it is not a weekday or
// we're on vacation. Return true if we sleep in. So some example input and output:
//
// sleepIn(false, false) → true
// sleepIn(true, false) → false
// sleepIn(false, true) → true

// function sleepin(weekday,vacation){
//     if (weekday != true || vacation == true) {
//         return true;
//     }else{
//         return false;
//     }
// }

// PROBLEM 2: MONKEY TROUBLE
//
// We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if
// each is smiling. We are in trouble if they are both smiling or if neither of
// them is smiling. Return true if we are in trouble.
//
// Example Input and Output
//
// monkeyTrouble(true, true) → true
// monkeyTrouble(false, false) → true
// monkeyTrouble(true, false) → false

// function monkeyTrouble(aSmile,bSmile){
//     if(aSmile===bSmile){
//         return true;
//     }else{
//         return false;
//     }
// }

// PROBLEM 3: STRING TIMES
//
// Given a string and a non-negative int n, return a larger
// string that is n copies of the original string.
//
// Example input and output:
//
// stringTimes("Hi", 2) → "HiHi"
// stringTimes("Hi", 3) → "HiHiHi"
// stringTimes("Hi", 1) → "Hi"

// function stringTimes(STRING,num){
//     var st;
//     for(let i=1;i<=num;i++){
//         if(i==1){
//             st=STRING;
//         }else{
//             st=st+STRING;
//         }
//     }    
//     return st;
// }

// Given 3 numerical values, a b c, return their sum. However, if one of the values is
// 13 then it does not count towards the sum and values to its right do not count.
// So for example, if b is 13, then both b and c do not count.
//
// Hint (Explore using multiple return statements inside a single function!)
//
// Example input and output
//
// luckySum(1, 2, 3) → 6
// luckySum(1, 2, 13) → 3
// luckySum(1, 13, 3) → 1

// function luckySum(a,b,c){
//     if(a==13){
//         return 0;
//     }else if(b==13){
//         return a;
//     }else if(c==13){
//         return a+b;
//     }else{
//         return a+b+c;
//     }
// }

// You are driving a little too fast, and a police officer stops you. Write code to
// compute the result, encoded as an int value: 0=no ticket, 1=small ticket,
// 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
// and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
// Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
//
// Here are some example inputs and outputs:
//
// caught_speeding(60, false) → 0
// caught_speeding(65, false) → 1
// caught_speeding(65, true) → 0

function caught_speeding(speed,is_birthday){
    if(speed<=60 && is_birthday==false){
        return 0;
    }else if(speed<=80 && is_birthday==false){
        return 1;
    }else if(speed>80 && is_birthday==false){
        return 2;
    }else{
        return 0;
    }
}