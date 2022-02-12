const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");
let arr = [];
let answer = [];
for (let i = 1; i < input.length; i++) {
  const [command, num] = input[i].split(" ");

  switch (command) {
    case "push":
      arr.push(num);
      break;
    case "pop":
      let temp = arr.pop();
      answer.push(temp !== undefined ? temp : -1);
      break;
    case "size":
      answer.push(arr.length);
      break;
    case "empty":
      answer.push(arr.length === 0 ? "1" : "0");
      break;
    case "top":
      answer.push(arr.length === 0 ? "-1" : arr[arr.length - 1]);
      break;
  }
}
console.log(answer.join("\n"));
