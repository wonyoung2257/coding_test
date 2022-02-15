const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

/**
 * 입력값 길이 3이면
 * n m k 값 얻어서 그래프 초기화
 *
 */
graph = [...Array(10)].map(() => Array(8).fill(0));
console.log(Array(8).fill(0));

graph;
