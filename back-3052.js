const fs = require("fs");
let input = fs
  .readFileSync("input.txt")
  .toString()
  .split("\r\n")
  .map((el) => +el);

solution(input);
function solution(input) {
  let answerArr = [];
  let count = 0;

  input.map((el) => {
    let temp = el % 42;

    if (!answerArr.includes(temp)) {
      count += 1;
    }
    answerArr.push(temp);
  });
  answerArr;
  console.log(count);
}
