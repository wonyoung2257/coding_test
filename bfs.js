function bfs(graph, start, visited) {
  let queue = [start];

  visited[start] = true;

  while (queue.length !== 0) {
    v = queue.shift();
    console.log(v);

    graph[v].map((el) => {
      if (!visited[el]) {
        queue.push(el);
        visited[el] = true;
      }
    });
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

let visited = new Array(9).fill(false);

bfs(graph, 1, visited);
