//dfs, bfs를 인접리스트 방식으로 구현할 때 근접한 노드를 오름차순으로 **정렬!!**
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [temp, ...nodes] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\r\n");

let [N, M, V] = temp.split(" ").map(Number);

let graph = [];
for (let i = 0; i <= N; i++) graph[i] = [];

let visited = new Array(N + 1).fill(false);

nodes.map((el) => {
  let [A, B] = el.split(" ").map(Number);

  graph[A].push(B);
  graph[B].push(A);
});
graph.map((el) => {
  el.sort((a, b) => a - b);
});
let answer = [];

dfs(graph, V, visited);
console.log(answer.join(" "));

answer = [];

visited = new Array(N + 1).fill(false);

bfs(graph, V, visited);
console.log(answer.join(" "));

function dfs(graph, v, visited) {
  visited[v] = true;
  answer.push(v);
  for (const el of graph[v]) {
    if (!visited[el]) {
      dfs(graph, el, visited);
    }
  }
}

function bfs(graph, v, visited) {
  let queue = [v];
  visited[v] = true;
  while (queue.length !== 0) {
    let node = queue.shift();
    answer.push(node);
    graph[node].map((el) => {
      if (!visited[el]) {
        queue.push(el);
        visited[el] = true;
      }
    });
  }
}
