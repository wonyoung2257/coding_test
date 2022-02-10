const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");
const N = input[0].split(" ")[1];
const lens = [];
let max = 0;
for (let i = 1; i < input.length; i++) {
  if (+input[i] > max) max = +input[i];
  lens.push(+input[i]);
}

solution(N, lens);
function solution(N, lens) {
  let min = 0;
  let answer = 0;
  while (min <= max) {
    let mid = Math.floor((max + min) / 2);
    let cnt = 0;
    lens.map((len) => {
      let rest = Math.floor(len / mid);
      cnt += rest;
    });
    if (cnt >= N) {
      if (mid > answer) answer = mid;
      min = mid + 1;
    } else {
      max = mid - 1;
    }
  }
  console.log(answer);
}
