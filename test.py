def solution(scoville, K):
    cnt = 0
    
    while min(scoville) < K:
      if len(scoville) <2:
        break
      minf = min(scoville)
      scoville.pop(scoville.index(minf))
      minf2 = min(scoville)
      scoville.pop(scoville.index(minf2))
      cul = minf + (minf2 *2)
      scoville.append(cul)
      
      cnt+=1
    if scoville[0]<K:
      return -1
    
    return cnt

print(solution([1, 2,3,4,5 ], 7))