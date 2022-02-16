const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\r\n");

for (let i = 1; i < input.length; i++) {
  let floor = +input[i];
  let ho = +input[++i];
  let arr = Array.from(Array(floor + 1), () => new Array(ho + 1).fill(0));

  for (let j = 0; j <= ho; j++) {
    arr[0][j] = j;
  }
  floor;
  ho;
  cul(floor, ho, arr);
}

function cul(f, h, apartment) {
  for (let i = 1; i <= f; i++) {
    //층 수 계산
    for (let j = 1; j <= h; j++) {
      // 호수 계산
      if (j === 1) apartment[i][j] = 1;
      else {
        apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j];
      }
    }
  }
  console.log(apartment[f][h]);
}
