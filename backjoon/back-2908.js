const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split(" ");

let num = +input[0];
let num2 = +input[1];

solution(num, num2);

function solution(num, num2) {
  let A = +num.toString().split("").reverse().join("");
  let B = +num2.toString().split("").reverse().join("");

  console.log(Math.max(A, B));
}
