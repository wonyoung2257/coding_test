const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

for (let i = 1; i < input.length; i++) {
  let temp = input[i].split("");
  let arr = [];
  temp.map((el) => {
    if (el === "(") arr.push(el);
    else {
      if (arr.length !== 0 && arr[arr.length - 1] === "(") arr.pop();
      else arr.push(el);
    }
  });
  console.log(arr.length === 0 ? "YES" : "NO");
}
