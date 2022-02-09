const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split(" ");

soultion(+input[0], +input[1]);
function soultion(x, y) {
  if (x > y) {
    console.log(">");
  } else if (x < y) {
    console.log("<");
  } else {
    console.log("==");
  }
}
