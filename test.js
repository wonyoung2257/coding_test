function combination(arr, num) {
  const result = [];
  if (num === 1) return arr.map((v) => [v]);

  arr.forEach((el, idx, array) => {
    const fix = el;
    const restArray = array.slice(idx + 1);
    const combiArr = combination(restArray, num - 1);
    const tempArr = combiArr.map((el) => [fix, ...el]);
    result.push(...tempArr);
  });
  return result;
}
