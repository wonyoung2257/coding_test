const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, ...nums] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

nums.sort((a, b) => {
  return a - b;
});

let average = nums.reduce((prev, cur) => {
  return prev + cur;
}, 0);
average = Math.round(average / nums.length);

let center = nums[Math.floor(nums.length / 2)];

const numMap = {};

for (let num of nums) {
  if (numMap[num]) {
    numMap[num] = numMap[num] + 1;
  } else {
    numMap[num] = 1;
  }
}

let hitMaxNum = Math.max.apply(null, Object.values(numMap));

let hitMaxNumArr = [];
let hitMaxNumResult = 0;
for (let numKey in numMap) {
  if (numMap[numKey] === hitMaxNum) {
    hitMaxNumArr.push(numKey);
  }
}

if (hitMaxNumArr.length > 1) {
  hitMaxNumArr = hitMaxNumArr.sort((a, b) => a - b);
  hitMaxNumResult = hitMaxNumArr[1];
} else {
  hitMaxNumResult = hitMaxNumArr[0];
}

let range = Math.max(...nums) - Math.min(...nums);

console.log(average === -0 ? 0 : average);
console.log(center);
console.log(hitMaxNumResult);
console.log(range);
