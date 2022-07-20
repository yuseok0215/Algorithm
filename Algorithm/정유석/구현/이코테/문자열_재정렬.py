# s = input()

# half = len(s)//2
# i = 0
# part_length = 1
# while i != half:
#     same_cnt = 0 # 같은 알파벳 개수
#     for l in range(half//part_length-1):
#         if s[l] == s[l+1]:
#             same_cnt += 1
#         else:
#             s[l-same_cnt:l+1]
        

2
#     i += 1 


def soslution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 상태초기화
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))
    
    return answer