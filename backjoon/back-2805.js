const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const M = +input[0].split(" ")[1];
let max = 0;
let tree = [];
input[1].split(" ").forEach((el) => {
  if (+el > max) max = +el;
  tree.push(+el);
});

solution(M, tree);
function solution(M, tree) {
  // 이진 탐색풀이
  // min과 max 사이의 크기로 H 설정
  // H로 자른 총합이 M보다 크면 H 값 늘림
  // 작다면 H값 줄임
  let mid = 0;
  let total = 0;
  let min = 0;
  while (min <= max) {
    total = 0;
    mid = Math.floor((max + min) / 2);
    tree.forEach((el) => {
      let rest = el - mid;
      if (rest > 0) total += rest;
    });

    if (total > M) {
      min = mid + 1;
    } else {
      max = mid - 1;
    }
  }
  console.log(mid);
}
