from turtle import left, right


n = int(input()) # 항상 짝수로 입력

n_str = str(n) # 자릿 수를 뽑기 위한 형변환
length = len(n_str)

left_sum = 0 # 절반 중 왼쪽 부분의 합
right_sum = 0 # 절반 중 오른쪽 부분의 합
for i in range(length//2):
    left_sum += int(n_str[i])
    right_sum += int(n_str[length-1-i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
