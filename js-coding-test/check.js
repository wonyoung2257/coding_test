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
    console.log(place[0][0]);
    for (let i = 0; i < 5; i++) {
      for (let k = 0; k < 5; k++) {
        console.log(place[i][k]);
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
