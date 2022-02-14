const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, K] = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

solution(N, K);
function solution(N, K) {
  let arr = [];
  for (let i = 0; i < N; i++) {
    arr[i] = i + 1;
  }
  let rear = -1;
  let answer = [];
  while (arr.length > 0) {
    for (let i = 0; i < K; i++) {
      rear++;
      if (rear >= arr.length) {
        rear = 0;
      }
    }
    answer.push(arr.splice(rear--, 1).join());
  }

  console.log("<" + answer.join(", ") + ">");
}
