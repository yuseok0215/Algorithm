n = int(input())

arr = []

for i in range(n):
    a, b= map(int, input().split())
    
    arr.append((a,b))
    
arr = sorted(arr, key = lambda student : student[1])



for student in arr:
    print(student[0], end = ' ')