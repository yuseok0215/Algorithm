from re import S


n, m = map(int, input().split())

cross = [[] for _ in range(N + 1)]
for _ in range(m):
    m, n = map(int, input().split()) #간선에 대한 중복을 없애주기 위함
    cross[m].append(n)
    cross[n].append(m)

visited = [False] * (n+1)

# cnt = 0
# def dfs(last):

#     for i, j in cross: # last값이 다른 간선의 첫 지점과 연결이 되는지 확인
#         if last == i:
#             dfs(j) # 그 뒤로 다시 연결된 다른 간선들 탐색
#             cnt += 1 # dfs 재귀함수가 모두 마지막 시점일 때 cnt 증가

#     return cnt 



def dfs(last):
    visited[last] = True
    



print(cnt)
