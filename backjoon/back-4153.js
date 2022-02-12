const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

for (let i = 0; i < input.length - 1; i++) {
  let el = input[i];
  let [A, B, C] = el
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);

  if (Math.pow(A, 2) + Math.pow(B, 2) === Math.pow(C, 2)) {
    console.log("right");
  } else {
    console.log("wrong");
  }
}
