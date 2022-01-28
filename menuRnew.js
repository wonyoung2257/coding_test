function solution(orders, course) {
  let answer = [];
  let obj = {};

  course.map((num) => {
    orders.forEach((menu) => {
      combination(menu.split(""), num).map((el) => {
        const word = el.sort().join("");
        obj[word] ? (obj[word] += 1) : (obj[word] = 1);
      });
    });
  });
  obj;

  course.map((num) => {
    let maxNum = 0;
    for (const key in obj) {
      if (obj[key] === 1) continue;
      if (key.length === num) {
        obj[key] > maxNum ? (maxNum = obj[key]) : "";
      }
    }
    let temp = Object.keys(obj).filter((key) => {
      return obj[key] === maxNum && key.length === num;
    });
    temp;
    temp.map((el) => answer.push(el));
  });
  answer;

  return answer.sort();
}

function combination(arr, num) {
  const result = [];
  if (num === 1) return arr.map((el) => [el]);

  arr.forEach((fix, idx, array) => {
    const restArray = array.slice(idx + 1);
    const combiArr = combination(restArray, num - 1);
    const combiFix = combiArr.map((el) => [fix, ...el]);

    result.push(...combiFix);
  });

  return result;
}

solution(["XYZ", "XWY", "WXA"], [2, 3, 4]);
// solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]);

console.log(combination("wxa".split(""), 2));
