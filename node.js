const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();
console.log(input);
const inputC = +input[0];

console.log(input[1]);
for (let i = 1; i <= inputC; ++i) {
  const arr = input[i].split(" ").map((item) => +item);
  console.log(input[i]);
  let newArr = [];
  for (let i = 0; i < arr.length; ++i) {
    newArr.push(arr[i]);
  }
  const testCase = {
    N: arr[0],
    arr: newArr,
  };
  console.log(testCase);
  // inputTestCase.push(testCase);
  break;
}

function solution(c, inputCase) {}
