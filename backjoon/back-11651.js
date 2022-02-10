const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
input.shift();
const temp = input.map((el) => el.split(" ").map(Number));

solution(temp);

function solution(input) {
  input = input.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  });
  let answer = "";
  input.forEach((el) => {
    answer += el[0] + " " + el[1] + "\n";
  });
  console.log(answer);
}
