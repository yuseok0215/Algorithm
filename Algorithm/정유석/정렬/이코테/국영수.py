n = int(input())

grade = []
for _ in range(n):
    data = list(map(input().split))
    grade.append((data[0], int(data[1]), int(data[2]), int(data[3])))    

grade = sorted(grade, key = lambda x:x[0])
grade = sorted(grade, key = lambda x:-x[3])
grade = sorted(grade, key = lambda x:x[2])
grade = sorted(grade, key = lambda x:-x[1])

for i in range(n):
    print(grade[i][0])
    
