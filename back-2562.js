const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\r\n");
console.log(input);

soultion(input.map((e) => +e));

function soultion(arr) {
  let max = Math.max(...arr);
  console.log(max);
  console.log(arr.indexOf(max) + 1);
}
