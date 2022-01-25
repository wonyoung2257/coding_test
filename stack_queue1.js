function solution(progresses, speeds) {
  let answer = [];
  let obj = [];
  let day = 1;
  let temp;

  progresses.map((el, i) => {
    obj[i] = Math.ceil((100 - el) / speeds[i]);
  });
  temp = obj[0];
  for (let i = 1; i < obj.length; i++) {
    if (temp >= obj[i]) {
      day += 1;
    } else {
      answer.push(day);
      day = 1;
      temp = obj[i];
    }
  }
  answer.push(day);

  return answer;
}

solution([93, 30, 55], [1, 30, 5]);

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]);

solution([0, 0, 0, 0, 0, 0], [99, 99, 10, 15, 15, 15]);
