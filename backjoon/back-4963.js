const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

let obj = {};
let testNum = 0;
for (let i = 0; i < input.length; i++) {
  let [W, H] = input[i].split(" ").map(Number);
  if (W === 0 && H === 0) break;
  let cnt = 0;
  for (let j = i + 1; j < H + i + 1; j++) {
    obj[testNum] === undefined ? (obj[testNum] = []) : "";
    obj[testNum].push(input[j].split(" ").map(Number));
    cnt++;
  }
  i += cnt;
  testNum++;
}
let answer = [];
for (const key in obj) {
  let graph = obj[key];
  let n = graph.length;
  let m = graph[0].length;

  let result = 0;

  for (let i = 0; i < n; i++)
    for (let j = 0; j < m; j++) {
      if (dfs(graph, i, j, n, m)) result++;
    }
  answer.push(result);
}
console.log(answer.join("\n"));

function dfs(graph, x, y, n, m) {
  if (x <= -1 || x >= n || y <= -1 || y >= m) {
    return false;
  }

  if (graph[x][y] === 1) {
    graph[x][y] = 0;
    // 상하좌우 검사
    dfs(graph, x - 1, y, n, m);
    dfs(graph, x, y - 1, n, m);
    dfs(graph, x + 1, y, n, m);
    dfs(graph, x, y + 1, n, m);
    // 대각선 검사
    dfs(graph, x - 1, y - 1, n, m);
    dfs(graph, x - 1, y + 1, n, m);
    dfs(graph, x + 1, y - 1, n, m);
    dfs(graph, x + 1, y + 1, n, m);

    return true;
  }
  return false;
}
