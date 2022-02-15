const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let arr = Array(input[1] + 1).fill(true);

for (let i = 2; i <= input[1]; i++) {
  for (let j = i + i; j <= input[1]; j += i) {
    if (arr[j]) arr[j] = false;
  }
}

arr[0] = false;
arr[1] = false;

for (let i = input[0]; i <= input[1]; i++) {
  if (arr[i]) console.log(i);
}
