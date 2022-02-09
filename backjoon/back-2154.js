const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = +fs.readFileSync(filePath).toString();

solution(input);
function solution(N) {
  let arr = [];
  for (let i = N; i > 0; i--) {
    arr.push(i);
  }
  // console.log(arr.pop());

  while (arr.length !== 1) {
    arr.pop();
    arr.unshift(arr.pop());
  }
  console.log(arr.pop());
}
