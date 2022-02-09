const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = +fs.readFileSync(filePath).toString();

solution(input);

function solution(num) {
  let number = 665;
  let count = num;
  while (count > 0) {
    number++;
    if (number.toString().includes("666")) {
      count--;
    }
  }
  console.log(number);
}
