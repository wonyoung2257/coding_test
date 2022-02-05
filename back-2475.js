const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split(" ");

soultion(input);
function soultion(num) {
  const sum = input.reduce((acc, cur, i) => {
    return acc + cur * cur;
  }, 0);
  console.log(sum % 10);
}
