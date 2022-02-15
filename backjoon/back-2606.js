const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [C, N, ...cums] = fs.readFileSync(filePath).toString().trim().split("\r\n");

let graph = [];

for (let i = 0; i <= C; i++) {
  graph[i] = [];
}

cums.map((el) => {
  let [idx, num] = el.split(" ");
  graph[idx].push(num);
  graph[num].push(idx);
});

let visited = new Array(+C + 1).fill(false);

let cnt = 0;
dfs(graph, 1, visited);

function dfs(graph, v, visited) {
  visited[v] = true;
  cnt++;
  for (const key of graph[v]) {
    if (!visited[key]) {
      dfs(graph, key, visited);
    }
  }
}

console.log(cnt - 1);
