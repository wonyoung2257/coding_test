function dfs(x, y) {
  if (x <= -1 || x >= n || y <= -1 || y >= m) {
    return false;
  }
  if (graph[x][y] === 0) {
    graph[x][y] = 1;

    dfs(x - 1, y);
    dfs(x, y - 1);
    dfs(x + 1, y);
    dfs(x, y + 1);
    return true;
  }
  return false;
}

let n = 3;
let m = 3;

let graph = [
  [0, 0, 1],
  [0, 1, 0],
  [1, 0, 1],
];

let result = 0;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (dfs(i, j)) result++;
  }
}
result;
