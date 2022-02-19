const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, ...nums] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\r\n")
  .map(Number);

nums.sort((a, b) => {
  return a - b;
});

let average = nums.reduce((prev, cur) => {
  return prev + cur;
}, 0);
average = Math.round(average / nums.length);

let center = nums[Math.floor(nums.length / 2)];

let obj = {};
nums.map((el) => {
  obj[el] === undefined ? (obj[el] = 1) : (obj[el] += 1);
});
obj;

let range = Math.max(...nums) - Math.min(...nums);
