def solution(number, k):
    answer = ''
    numArr = list(map(int, number))
    long = len(number) - k
    i= 0
    while len(answer) != len(number) - k:
      maxNum = max(numArr[0:len(numArr)-long])
      numArr = numArr[numArr.index(maxNum)+1:]
      
      answer += str(maxNum)
      long -=1
    print(answer)

    return answer

solution("1231234", 3)