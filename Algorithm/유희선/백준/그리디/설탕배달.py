import sys
sys.stdin=open("input.txt","rt")

n=int(input())
cnt=0
#x와 n을 비교하기 위해서 x변수 사용
x=n #ex. 19

#x가 5로 나눌 수 있는 경우
if x>=5: 
    cnt+=x//5
    x=x%5 #x = 19%5 = 4

# 위의 경우만 한다면 3으로 나누어떨어지지 않는 경우 발생
# x가 3으로 나누어 떨어질 수 있을 때까지 값 변경
while x%3!=0:
        cnt-=1
        x+=5 # 4+5 = 9
        if x>n: #계속 5씩 더해주다가 입력값보다 넘어서면 break
            break

if x>n:
    print(-1)
# x가 3으로 나누떨어질 수 있도록 만들었음 ex. x=9
else:
    cnt+=x//3
    print(cnt)