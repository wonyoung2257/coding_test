const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const M = +input[0].split(" ")[1];
const card = input[1].split(" ").map(Number);
solution(M, card);

function solution(M, card) {
  let maxNum = 0;
  for (let i = 0; i < card.length - 2; i++) {
    let one = card[i];
    one;
    for (let j = i + 1; j < card.length - 1; j++) {
      let two = card[j];
      two;
      for (let k = j + 1; k < card.length; k++) {
        let three = card[k];
        three;
        let total = one + two + three;
        total;
        if (total > M) {
          break;
        }

        maxNum = Math.max(maxNum, total);
      }
    }
  }

  console.log(maxNum);
}
