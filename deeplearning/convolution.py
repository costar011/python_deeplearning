def convolution(array, kernel):
    # 합성곱 연산 결과를 저장할 리스트
    aryResult = []
    
    # 입력 배열(array)을 커널(kernel)로 합성곱 연산할 수 있는 모든 위치를 순회
    for i in range(len(array) - len(kernel) + 1):  # 세로 방향 슬라이싱 범위 설정
        for j in range(len(array[0]) - len(kernel[0]) + 1):  # 가로 방향 슬라이싱 범위 설정
            
            # 현재 위치에서 커널 크기만큼의 부분 배열(array)을 슬라이싱
            aryPart = array[i:i+len(kernel), j:j+len(kernel[0])] 
            
            # 슬라이싱 된 부분 배열과 커널을 원소별로 곱한 뒤, 모두 더해 결과 저장
            aryResult.append(np.sum(aryPart * kernel))
    
    # 결과 리스트를 2D 배열로 변환해 반환 (출력 크기 계산: (원본 배열 크기 - 커널 크기 + 1))
    return np.array(aryResult).reshape(
        len(array) - len(kernel) + 1, 
        len(array[0]) - len(kernel[0]) + 1
    )
