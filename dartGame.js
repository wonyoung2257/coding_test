function solution(dartResult) {
    let answer = 0;
    let prePoint = 0
    
    
    for(let i = 0; i< dartResult ; i++){
        if(dartResult[i+3] === '*' || dartResult[i+3] === '#'){
            if(dartResult === 'S'){
                prePoint = dartResult[i]
            }
            if(dartResult === 'D'){
                prePoint = dartResult[i] **2
            }
            if(dartResult === 'T'){
                prePoint = dartResult[i] **3
            }
            if(dartResult[i+3] === '*'){
                if(i ===0){
                    prePoint *=2
                }else{
                    prePoint
                }
            }
            
        }
    }
    return answer;
}