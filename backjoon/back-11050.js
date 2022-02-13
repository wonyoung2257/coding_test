const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, K] = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let NFac = factorial(N);
let KFac = factorial(K);
let NKFac = factorial(N - K);

console.log(NFac / (NKFac * KFac));

function factorial(num) {
  let result = 1;
  for (let i = 2; i <= num; i++) {
    result *= i;
  }
  return result;
}
