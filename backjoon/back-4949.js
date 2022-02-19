const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");
input.pop();

input.map((el) => {
  let stack = [];
  for (let i = 0; i < el.length; i++) {
    if (el[i] === "[" || el[i] === "(") {
      stack.push(el[i]);
    }

    if (el[i] === "]" && stack[stack.length - 1] !== "[") {
      stack.push(el[i]);
    }
    if (el[i] === ")" && stack[stack.length - 1] !== "(") {
      stack.push(el[i]);
    }
    if (el[i] === "]" && stack[stack.length - 1] === "[") {
      stack.pop();
    }
    if (el[i] === ")" && stack[stack.length - 1] === "(") {
      stack.pop();
    }
  }
  console.log(stack.length === 0 ? "yes" : "no");
});
