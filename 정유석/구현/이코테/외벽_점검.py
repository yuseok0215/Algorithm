# n = int(input())

# weak = list(map(int, input().split()))
# dist = list(map(int, input().split()))

# checking = []
# for i in range(len(dist)):
#     if i == len(dist)-1:
#         checking.append(n - (weak[i] - weak[0]))
#     else:
#         checking.append(abs(weak[i] - weak[i+1]))
        
# print(checking)
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 

    for start in range(length):
        # 친구를 나열 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1] 

            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break   
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    return answer


            