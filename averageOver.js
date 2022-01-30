const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();
input = input.split("\n");
const inputC = +input[0];
const inputTestCase = [];

for (let i = 1; i <= inputC; ++i) {
  const arr = input[i].split(" ").map((item) => +item);

  let newArr = [];
  for (let j = 1; j < arr.length; ++j) {
    newArr.push(arr[j]);
  }
  const testCase = {
    N: arr[0],
    arr: newArr,
  };
  inputTestCase.push(testCase);
}

solution(inputC, inputTestCase);

function solution(C, inputCase) {
  const average = [];
  inputCase.map((el) => {
    let sum = el.arr.reduce((prev, curr) => prev + curr);
    average.push(sum / el.N);
  });

  inputCase.map((el, idx) => {
    let cnt = 0;
    el.arr.map((num) => {
      if (num > average[idx]) {
        cnt += 1;
      }
    });
    console.log(((cnt / el.arr.length) * 100).toFixed(3) + "%");
  });
}
