/**
 * 들어온 문자열을 배열로 나뉜다.
 * 각 집합의 길이 순으로 정렬한다.
 * 정렬한 처음 원소를 뽑고
 * 순차적으로 다음 배열과 비교하여
 * 없은 요소를 찾아 answer 배열에 push 한다.
 */
function solution(s) {
  let answer = [];
  let sorted = s
    .replace(/{/gi, "")
    .split("}")
    .sort((a, b) => a.length - b.length)
    .filter((e) => e !== "");

  sorted.map((el, idx) => {
    let temp = el.split(",").filter((e) => e);
    if (idx === 0) answer.push(temp.join());
    else {
      //2자리 이상의 숫자를 자리마다 짤라서 확인하여 문제가 됨
      answer.push(temp.filter((e) => !answer.includes(e)).join());
    }
  });
  return answer.map((el) => +el);
}

solution("{{20,111},{111}}");
// solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
