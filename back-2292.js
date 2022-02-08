const fs = require("fs");
let input = +fs.readFileSync("input.txt").toString();

solution(input);
function solution(N) {
  N;
  let center = 1;
  let cnt = 1;

  while (true) {
    if (N <= center) {
      break;
    }
    center = center + cnt * 6;
    center;
    cnt++;
  }
  console.log(cnt);
}
