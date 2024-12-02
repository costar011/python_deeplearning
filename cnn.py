# 필요한 라이브러리를 임포트합니다.
import cv2  # OpenCV를 사용해 실시간 영상 처리를 담당합니다.
import numpy as np  # 데이터 처리를 위한 NumPy 라이브러리입니다.
from tensorflow.keras.models import Sequential  # CNN 모델 설계를 위한 Keras 모듈입니다.
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense  # CNN 구성 요소입니다.

# CNN 모델을 정의합니다.
def build_model():
    """
    간단한 CNN 모델을 구성하는 함수입니다.
    """
    model = Sequential([
        # 첫 번째 합성곱 레이어
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
        MaxPooling2D(pool_size=(2, 2)),

        # 두 번째 합성곱 레이어
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),

        # 완전 연결 레이어로 전환
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2, activation='softmax')  # 이진 분류 (클래스가 두 개인 경우)
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# 모델 생성
model = build_model()

# 사전 훈련된 가중치를 로드하거나 직접 훈련 가능
# model.load_weights('path_to_weights.h5')  # 사전 훈련된 모델 사용

# 웹캠 데이터를 실시간으로 처리하는 함수입니다.
def process_live_video():
    """
    OpenCV를 사용해 실시간으로 웹캠에서 데이터를 읽고 CNN 모델로 예측을 수행합니다.
    """
    cap = cv2.VideoCapture(0)  # 0번 웹캠을 엽니다.
    
    while True:
        # 웹캠에서 프레임을 읽습니다.
        ret, frame = cap.read()
        if not ret:
            print("카메라에서 프레임을 가져올 수 없습니다.")
            break

        # 이미지를 그레이스케일로 변환합니다.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 이미지를 모델 입력 크기로 조정합니다.
        resized = cv2.resize(gray, (64, 64))
        normalized = resized / 255.0  # 0-1로 정규화
        reshaped = normalized.reshape(1, 64, 64, 1)  # 모델 입력 형식으로 재구성

        # CNN 모델을 사용해 예측합니다.
        predictions = model.predict(reshaped)
        class_id = np.argmax(predictions)  # 가장 높은 확률을 가진 클래스 ID
        label = "Class A" if class_id == 0 else "Class B"  # 예: Class A 또는 B로 표시

        # 프레임에 예측 결과를 표시합니다.
        cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # 결과를 화면에 표시합니다.
        cv2.imshow('Live Video', frame)

        # 'q' 키를 누르면 종료합니다.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 캡처 및 창을 정리합니다.
    cap.release()
    cv2.destroyAllWindows()

# 실시간 분석 실행
process_live_video()
