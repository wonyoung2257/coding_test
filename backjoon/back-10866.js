const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

solution(input);
function solution(input) {
  let deque = [];
  let answer = [];
  for (let i = 1; i < input.length; i++) {
    let [command, num] = input[i].split(" ");
    num = +num;
    switch (command) {
      case "push_front":
        deque.unshift(num);
        break;
      case "push_back":
        deque.push(num);
        break;
      case "pop_front":
        answer.push(deque.length === 0 ? -1 : deque.shift());
        break;
      case "pop_back":
        answer.push(deque.length === 0 ? -1 : deque.pop());
        break;
      case "size":
        answer.push(deque.length);
        break;
      case "empty":
        answer.push(deque.length === 0 ? 1 : 0);
        break;
      case "front":
        answer.push(deque.length === 0 ? -1 : deque[0]);
        break;
      case "back":
        answer.push(deque.length === 0 ? -1 : deque[deque.length - 1]);
        break;
    }
  }
  console.log(answer.join("\n"));
}
