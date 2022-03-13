def solution(N, stages):
  answer = []
  temp = [0] * (N+2)
  
  for i in stages:
    temp[i] +=1
  
  player = temp[-1]
  for stage in range(len(temp)-2, 0, -1):
    if temp[stage] == 0:
      culFail = 0
    else:
      player += temp[stage]
      culFail = temp[stage] / player

    answer.append((stage,culFail))
  
  answer.sort(key= lambda x:(x[1], -x[0]), reverse=True)
  for i in range(len(answer)):
    answer[i] = answer[i][0]

  return answer

print(solution(5,	[1, 2, 2, 1, 3]))