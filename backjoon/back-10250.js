const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

solution(input);
function solution(input) {
  for (let i = 1; i < input.length; i++) {
    let [H, W, N] = input[i].split(" ").map(Number);
    let room = Math.ceil(N / H);
    let floor = N % H === 0 ? H : N % H;

    console.log(room < 10 ? floor + "0" + room : floor + room.toString());
  }
}
