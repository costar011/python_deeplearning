
a = 8
b = 3
print("a + b = ", a+b)      # 더하기
print("a - b = ", a-b)      # 빼기
print("a * b = ", a*b)      # 곱하기
print("a ** b = ", a**b)    # 거듭제곱
print("a / b = ", a/b)      # 나누기
print("a // b = ", a//b)    # 몫
print("a % b = ", a%b)      # 나머지

#============================

a = 5                   #int
b = 5.011               #float
c = True                #bool
d = [1,2,3]             #list
e = {"item": "책상"}    #dict
f = "abcdefg"           #str

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print("=== 변환 방법 ===")
print(type(float(a)))
print(type(str(a)))

#============================
# 0과 1로만 구분 , 0은 false / 1은 true
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(0.001))
print(bool(int(0.5)))
print(type(None)) #C/C++ = Null

#============================
print("aa'a'aa")
print('"hello world"')
print('''===========================
      Hello IoT
      my name is Sukhen
      I want A+
===========================     ''')

#============================
text = 'KR'
text2 = 'US'
text3 = 'BZ'
print(text,"\t",text2,"\t",text3,"\n","\t> Nice Nation")

#============================
t1 = 10,50,'hello','bye'
t2 = 1,2,3,4,5,6,7,8,9,10

print(t1[0])
print(t1[1:])
for i in t2:
    if i <= 9:
        print(i, end=" ")
    else:
        print(i)
num1,num2,num3,num4,num5,num6,num7,num8,num9,num10 = t2
print(num1,num3,num5,num7,num9)
print(type(t1))

#============================
data = [123,456,789,246,357,468,'a','b','c',0.15]
print(type(data))
print(type(data[8]))
print(type(data[-1]))
print(data[0],data[:3])

for i in data:
    print(i, end=" ")
    
print("")
        
data[1] = 30 # 특정 주소 변경
data.append(80) # 마지막 주소에 추가
data.insert(3, 50) # 3번째 주소에 값 넣고 뒤로 한칸씩 밀기
data.extend([30,40,50]) # 마지막 주소뒤에 여러개 값 넣기

for i in data:
    print(i, end=" ")
    
print("")
#============================
things = {"가구":"소파","음식":"김치","가전":"냉장고"} #
things2 = dict({"가구":"책상","음식":"초콜릿","가전":"청소기"})
print(type(things))
print(type(things2))

print(things["가구"])
print(things2.get("음식"))

for i,j in things2.items():
    print(f"{i}: {j}")
    
print("")

#추가
things['이름'] = 'sukhen'
print(things["이름"])

#수정
things['이름'] = "홍길동"
print(things["이름"])

#여러 값 수정
things.update({"가구":"의자","이름":"이순신"})

for i,j in things.items():
    print(f"{i} : {j}")
    
print("")

#============================
number = input("number & text > ")
print(number)