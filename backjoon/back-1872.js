const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, ...nums] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\r\n")
  .map(Number);

solution(n, nums);
function solution(n, numbers) {
  let answer = [];
  let tempList = [];
  let ansArr = [];
  let num = 1;
  let idx = 0;

  while (num <= n) {
    if (ansArr[ansArr.length - 1] > numbers[idx]) {
      answer.push("-");
      ansArr.push(tempList.pop());
      idx++;
      continue;
    }

    if (num !== numbers[idx]) {
      tempList.push(num++);
      answer.push("+");
    } else {
      answer.push("+");
      answer.push("-");
      ansArr.push(num++);
      idx++;
    }
  }
  while (tempList.length > 0) {
    answer.push("-");
    ansArr.push(tempList.pop());
  }

  if (ansArr.join() === numbers.join()) {
    console.log(answer.join("\n"));
  } else {
    console.log("NO");
  }
}
