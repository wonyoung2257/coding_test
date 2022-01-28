function solution(places) {
  let answer = [];
  let place = [];
  let te = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
  ];
  console.log(te[0][0]);

  while (true) {
    let index = 0;
    place = places[index].map((el) => el.split(""));
    for (let i = 0; i < 6; i++) {
      for (let k = 0; k < 6; k++) {
        place[i][k];
      }
    }
    return;
  }

  return answer;
}

solution([
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]);
