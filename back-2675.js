const fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\r\n");
//문자열을 자르고 뒤에 공백에 주의

soultion(input);

function soultion(input) {
  for (let i = 1; i < input.length; i++) {
    let answer = [];
    let [num, word] = input[i].split(" ");
    console.log(typeof word);
    let temp = word.split("");
    console.log(temp);
    temp.map((el) => {
      for (let j = 0; j < +num; j++) {
        answer.push(el);
      }
    });
    console.log(answer.join(""));
  }
}
