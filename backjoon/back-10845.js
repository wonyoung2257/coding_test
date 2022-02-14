const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

solution(input);
function solution(value) {
  let queue = [];
  let answer = [];
  for (let i = 1; i < value.length; i++) {
    let [command, num] = value[i].split(" ");

    switch (command) {
      case "push":
        queue.push(+num);
        break;
      case "pop":
        answer.push(queue.length === 0 ? -1 : queue.shift());
        break;
      case "size":
        answer.push(queue.length);
        break;
      case "empty":
        answer.push(queue.length === 0 ? 1 : 0);
        break;
      case "front":
        answer.push(queue.length === 0 ? -1 : queue[0]);
        break;
      case "back":
        answer.push(queue.length === 0 ? -1 : queue[queue.length - 1]);
        break;
    }
  }
  console.log(answer.join("\n"));
}
