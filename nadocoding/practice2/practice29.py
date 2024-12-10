# with

# with open("profile.pickle", "rb") as profile_file: #file을 열어서 profile_file이라는 변수에 저장 / rb: read binary
#    print(pickle.load(profile_file)) # close를 안해도 됨
#    # 자동으로 close를 해줌

# with open("study.txt", "w", encoding="utf8") as study_file: # encoding="utf8": 한글이 깨지지 않게 함
#    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file: # r: read # encoding="utf8": 한글이 깨지지 않게 함
    print(study_file.read())