var arr = [0, 1];

let v = arr.reduce((acc, cur, index, arr) => {
  console.log(acc);
  console.log(cur);
  console.log(index);
  console.log(arr);
});
