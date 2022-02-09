/**
 * A -> B
 * B -> BA
 */
const fs = require("fs");
let input = fs.readFileSync("input.txt");

solution(+input);

function solution(k) {
  let answer = "";
  let fibo = new Array(45);
  fibo[0] = 0;
  fibo[1] = 1;
  fibo[2] = 1;

  if (k === 1) {
    answer = "0 1";
    console.log(0, 1);
  } else {
    for (let i = 3; i <= k; i++) {
      fibo[i] = fibo[i - 1] + fibo[i - 2];
    }
    console.log(fibo[k - 1], fibo[k]);
  }
}
