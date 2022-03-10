function solution(progresses, speeds) {
  let answer = [];
  let arr = [];
  let cnt = 1;
  let temp;

  progresses.map((el, i) => {
    arr[i] = Math.ceil((100 - el) / speeds[i]);
  });
  temp = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (temp >= arr[i]) {
      cnt += 1;
    } else {
      answer.push(cnt);
      cnt = 1;
      temp = arr[i];
    }
  }
  answer.push(cnt);

  return answer;
}

solution([93, 30, 55], [1, 30, 5]);

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]);

solution([0, 0, 0, 0, 0, 0], [99, 99, 10, 15, 15, 15]);
