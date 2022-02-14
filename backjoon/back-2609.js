const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [num1, num2] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

console.log(GCD(num1, num2), LCM(num1, num2));

function GCD(num1, num2) {
  // 최대공약수
  while (true) {
    r = num1 % num2;
    if (r === 0) return num2;

    num1 = num2;
    num2 = r;
  }
}

function LCM(num1, num2) {
  return (num1 * num2) / GCD(num1, num2);
}
