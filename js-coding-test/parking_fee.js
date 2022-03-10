function solution(fees, records) {
  let answer = [];
  let obj = {};

  records.map((el) => {
    let [parkingTime, num, state] = el.split(" ");

    if (state === "IN") {
      if (num in obj) {
        obj[num] = {
          ...obj[num],
          time: transMin(parkingTime),
          state,
        };
      } else {
        obj[num] = {
          time: transMin(parkingTime),
          state,
          totalTime: 0,
        };
      }
      obj;
    } else {
      obj[num].totalTime += transMin(parkingTime) - obj[num].time;
      obj[num] = {
        ...obj[num],
        time: transMin(parkingTime),
        state,
      };
    }
  });

  for (const key in obj) {
    if (obj[key].state === "IN") {
      obj[key].totalTime += transMin("23:59") - obj[key].time;
    }
    obj[key].fee = culFee(fees, obj[key].totalTime);
  }
  Object.keys(obj)
    .sort()
    .map((el) => {
      answer.push(obj[el].fee);
    });
  answer;

  return answer;
}

const transMin = (time) => {
  let [hour, min] = time.split(":");
  return hour * 60 + +min;
};

const culFee = (fees, totalTime) => {
  let [defaultTime, defaultFee, unitTime, unitFee] = fees;
  let culTime = totalTime - defaultTime;

  return culTime < 1
    ? defaultFee
    : defaultFee + Math.ceil(culTime / unitTime) * unitFee;
};

solution(
  [180, 5000, 10, 600],
  [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
  ]
);
solution(
  [120, 0, 60, 591],
  [
    "16:00 3961 IN",
    "16:00 0202 IN",
    "18:00 3961 OUT",
    "18:00 0202 OUT",
    "23:58 3961 IN",
  ]
);
