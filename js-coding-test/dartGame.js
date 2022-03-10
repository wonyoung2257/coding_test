function solution(dartResult) {
  let answer = 0;
  let point = [];
  let idx = -1;
  let resultArr = dartResult.replace(/10/g, "k").split("");

  for (let i = 0; i < resultArr.length; i++) {
    const temp = resultArr[i] === "k" ? "10" : resultArr[i];
    temp;

    if (isNaN(temp)) {
      switch (temp) {
        case "S":
          point[idx] = point[idx];
          break;
        case "D":
          point[idx] = point[idx] ** 2;
          break;
        case "T":
          point[idx] = point[idx] ** 3;
          break;
        case "*":
          if (idx > 0) {
            point[idx] *= 2;
            point[idx - 1] *= 2;
          } else {
            point[idx] *= 2;
          }
          break;
        case "#":
          point[idx] *= -1;
          break;
      }
    } else {
      idx += 1;
      point[idx] = +temp;
    }
  }

  answer = point.reduce((sum, currValue) => {
    return sum + currValue;
  }, 0);

  return answer;
}
console.log(solution("10S10S10S"));
