const fs = require("fs");
let input = fs
  .readFileSync("input.txt")
  .toString()
  .toUpperCase()
  .split("")
  .filter((e) => e !== "\n");
input;

soultion(input);
function soultion(str) {
  if (str.length === 1) {
    console.log(str[0]);
    return;
  }
  const obj = {};
  str.map((el) => {
    if (!obj[el]) {
      obj[el] = 1;
    } else {
      obj[el] += 1;
    }
  });

  let sortobj = [];
  for (let key in obj) {
    sortobj.push([key, obj[key]]);
  }
  sortobj.sort((a, b) => {
    return b[1] - a[1];
  });
  let num = sortobj[0][1] == sortobj[1][1] ? "?" : sortobj[0][0];
  console.log(num);
}
