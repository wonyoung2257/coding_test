const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
input;
input = input[0];
input;
input = input.split(" ").map((item) => BigInt(item));

solution(input[0], input[1]);

function solution(A, B) {
  let answer = A + B + "\n";
  answer += A - B + "\n";
  answer += A * B;
  console.log(answer);
}
