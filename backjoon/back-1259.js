const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\r\n");

input;
solution(input);
function solution(input) {
  for (let i = 0; i < input.length; i++) {
    let answer = "";
    if (input[i] === "0") break;

    let temp = input[i].split("");
    for (let j = 0; j < temp.length / 2; j++) {
      if (temp[j] !== temp[temp.length - 1 - j]) {
        answer = "no";
        break;
      }
    }
    if (answer !== "no") {
      answer = "yes";
    }
    console.log(answer);
  }
}
