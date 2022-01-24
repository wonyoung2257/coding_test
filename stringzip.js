function solution(s) {
  let answer = s.length;

  for (let i = 1; i <= parseInt(s.length / 2); i++) {
    let str = "";
    let cnt = 1;
    let tempStr = s.substr(0, i);
    let len = 0;

    for (len = i; len <= s.length; len += i) {
      let nextStr = s.substr(len, i);

      if (tempStr === nextStr) {
        cnt += 1;
      } else {
        if (cnt === 1) str = str + tempStr;
        else str = str + cnt + tempStr;

        cnt = 1;
        tempStr = nextStr;
      }
    }
    if (cnt === 1) str = str + tempStr;
    else str = str + cnt + tempStr;
    answer = Math.min(answer, str.length);
  }

  return answer;
}
