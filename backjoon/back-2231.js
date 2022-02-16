const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = +fs.readFileSync(filePath);

let answer = [];
let num = 0;

while (num < input) {
  let sum = num
    .toString()
    .split("")
    .reduce((prev, cur) => {
      return +prev + +cur;
    }, 0);

  sum += num;

  if (sum === input) {
    answer.push(num);
  }
  num++;
}
answer;
console.log(answer.length === 0 ? 0 : Math.min(...answer));

/**
 * N의 가장 작은 생성자를 구해라
 * 245의 분해합은 256 따라서 245는 256의 생성자
 */
