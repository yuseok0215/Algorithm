s = input()

alphabet = [] # 알파벳을 추출할 배열
number = [] # 숫자를 추출할 배열
for i in range(len(s)):
    if 65<=ord(s[i])<=90: # 대문자를 아스키코드를 통해 정수로 변환
        alphabet.append(s[i])
    else:
        number.append(s[i])

alphabet.sort()
str_alphabet = ''.join(s for s in alphabet) # 출력값을 위한 리스트 -> 문자열 형변환
sum = 0
for i in range(len(number)):
    sum += int(number[i])

print(str_alphabet + str(sum))


