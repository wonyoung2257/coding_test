const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

let arr = new Array(1000).fill(true);

for (let i = 2; i <= 1000; i++) {
  if (arr[i]) {
    for (let j = i * i; j <= 1000; j += i) {
      arr[j] = false;
    }
  }
}

let cnt = 0;
input[1].split(" ").map((el) => {
  if (arr[el] && +el !== 1) cnt += 1;
});
console.log(cnt);
