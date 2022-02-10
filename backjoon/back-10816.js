const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [N, cardN, M, cardM] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\r\n");

cardN = cardN
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const answer = [];
cardM.split(" ").map((el) => {
  let min = minIndex(cardN, +el);
  let max = maxIndex(cardN, +el);
  answer.push(min !== -1 || max !== -1 ? max - min + 1 : 0);
});
console.log(answer.join(" "));

function minIndex(N, target) {
  let min = 0;
  let max = N.length;
  while (min <= max) {
    let mid = Math.floor((max + min) / 2);

    if (N[mid] === target) {
      if (N[mid - 1] === target) {
        max = mid - 1;
      } else {
        return mid;
      }
    } else if (N[mid] > target) {
      max = mid - 1;
    } else {
      min = mid + 1;
    }
  }
  return -1;
}
function maxIndex(N, target) {
  let min = 0;
  let max = N.length;
  while (min <= max) {
    let mid = Math.floor((max + min) / 2);

    if (N[mid] === target) {
      if (N[mid + 1] === target) {
        min = mid + 1;
      } else {
        return mid;
      }
    } else if (N[mid] > target) {
      max = mid - 1;
    } else {
      min = mid + 1;
    }
  }
  return -1;
}
