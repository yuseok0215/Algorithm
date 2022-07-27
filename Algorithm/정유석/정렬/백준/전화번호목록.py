t = int(input())


def solution(phone_k):
    answer = True
    phone_k.sort()
    for i in range(len(phone_k)-1):
        if len(phone_k[i]) < len(phone_k[i+1]):
            if phone_k[i + 1][:len(phone_k[i])] == phone_k[i]:
                answer = False
                break
    return answer

for _ in range(t):
    n = int(input())

    phone = []
    for _ in range(n):   # 12358 123 -> 123 12358
        data = int(input())
        phone.append(data)

    k = solution(phone)
    