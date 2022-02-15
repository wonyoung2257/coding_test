const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");
let [N, M] = input[0].split(" ").map(Number);

let graph = [];
for (let i = 0; i <= N; i++) {
  graph[i] = [];
}
let visited = new Array(N + 1).fill(false);
input.shift();
input.map((el) => {
  let [A, B] = el.split(" ").map(Number);
  graph[A].push(B);
  graph[B].push(A);
});

function dfs(v) {
  visited[v] = true;
  for (const el of graph[v]) {
    if (!visited[el]) {
      dfs(el);
    }
  }
}

let ans = 0;
for (let i = 1; i <= N; i++) {
  if (!visited[i]) {
    dfs(i);
    ans++;
  }
}

console.log(ans);
