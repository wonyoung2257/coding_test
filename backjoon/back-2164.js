const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = +fs.readFileSync(filePath);

solution(input);
function solution(num) {
  let arr = new Array(num);
  for (let i = 0; i < num; i++) {
    arr[i] = i + 1;
  }
  let front = 0;
  let rear = arr.length - 1;

  for (let i = 0; i < num - 1; i++) {
    front++;
    arr[++rear] = arr[front++];
  }
  console.log(arr[arr.length - 1]);
}
