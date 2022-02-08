const fs = require("fs");
let input = fs
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((e) => +e);

solution(input);

function solution([A, B, V]) {
  day = (V - B - 1) / (A - B) + 1;
  console.log(parseInt(day));
}
