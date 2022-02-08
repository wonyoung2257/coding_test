const fs = require("fs");
let input = fs
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((el) => +el);

solution(input);
function solution(input) {
  const [x, y, w, h] = input;
  let answer = [];

  answer.push(Math.abs(y - h));
  answer.push(Math.abs(y - 0));
  answer.push(Math.abs(w - x));
  answer.push(Math.abs(x - 0));

  console.log(Math.min(...answer));
}
