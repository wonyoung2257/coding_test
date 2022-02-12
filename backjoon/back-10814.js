const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");
input.shift();

solution(input);
function solution(input) {
  let arr = input.map((el) => {
    return el.split(" ");
  });
  arr = arr.sort((a, b) => {
    return +a[0] - +b[0];
  });

  arr.map((el) => {
    console.log(el.join(" "));
  });
}
