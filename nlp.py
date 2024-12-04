# pip install transformers -> 필요한 라이브러리 설치


from transformers import pipeline  # Hugging Face의 파이프라인 기능을 사용
import os  # 파일 처리를 위한 라이브러리

# 요약을 수행하는 함수 정의
def summarize_text(text, max_length=130, min_length=30):
    """
    주어진 텍스트를 요약하는 함수입니다.
    
    Args:
        text (str): 요약할 원본 텍스트
        max_length (int): 요약된 텍스트의 최대 길이
        min_length (int): 요약된 텍스트의 최소 길이
    
    Returns:
        str: 요약된 텍스트
    """
    # Hugging Face의 'summarization' 파이프라인 생성
    summarizer = pipeline("summarization")  
    
    # 텍스트 요약 수행
    summary = summarizer(
        text,  # 요약할 텍스트
        max_length=max_length,  # 요약문 최대 길이
        min_length=min_length,  # 요약문 최소 길이
        do_sample=False  # 결과의 일관성을 유지하기 위해 sampling 비활성화
    )
    # 요약된 텍스트 반환
    return summary[0]['summary_text']

# 실행할 메인 함수
if __name__ == "__main__":
    # 요약할 예제 텍스트
    example_text = """
    Artificial intelligence (AI) refers to the simulation of human intelligence in machines 
    that are programmed to think like humans and mimic their actions. The term may also 
    be applied to any machine that exhibits traits associated with a human mind such as 
    learning and problem-solving. The ideal characteristic of artificial intelligence is its 
    ability to rationalize and take actions that have the best chance of achieving a specific 
    goal. AI is continuously evolving to benefit many different industries. Machines are 
    wired using a cross-disciplinary approach based on mathematics, computer science, 
    linguistics, psychology, and more.
    """

    # 텍스트 요약 함수 호출
    summarized_text = summarize_text(example_text)

    # 결과 출력
    print("=== 원본 텍스트 ===")
    print(example_text)
    print("\n=== 요약된 텍스트 ===")
    print(summarized_text)
