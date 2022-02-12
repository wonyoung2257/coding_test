const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

const white = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
];
const black = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
];
console.log(black[0][0]);
const [row, col] = input.shift().split(" ");
function check(x, y, board) {
  let cnt = 0;

  for (let i = x; i < x + 8; i++) {
    for (let j = y; j < y + 8; j++) {
      if (board === "black") {
        if (input[i][j] !== black[i - x][j - y]) cnt += 1;
      } else {
        if (input[i][j] !== white[i - x][j - y]) cnt += 1;
      }
    }
  }
  return cnt;
}
let answer = [];
for (let i = 0; i + 7 < row; i++) {
  for (let j = 0; j + 7 < col; j++) {
    answer.push(check(i, j, "black"));
    answer.push(check(i, j, "white"));
  }
}

console.log(Math.min(...answer));
