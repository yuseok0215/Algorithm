n = int(input())

graph = list(map(int, input().split()))
graph.sort()
print(graph[(n-1)//2])