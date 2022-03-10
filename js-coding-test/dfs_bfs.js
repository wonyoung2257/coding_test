function dfs(graph, v, visited) {
  visited[v] = true;
  console.log(v);
  for (const el of graph[v]) {
    if (!visited[el]) {
      dfs(graph, el, visited);
    }
  }
}

let graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];

visited = new Array(9).fill(false);

dfs(graph, 1, visited);
