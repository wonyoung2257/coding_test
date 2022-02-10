const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, cardN, M, cardM] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\r\n");

const obj = {};

cardN.split(" ").map((el) => {
  if (obj[el] === undefined) obj[el] = 1;
  else obj[el] += 1;
});
const answer = [];
cardM.split(" ").map((el) => {
  if (obj[el] !== undefined) answer.push(obj[el]);
  else answer.push(0);
});
console.log(answer.join(" "));
