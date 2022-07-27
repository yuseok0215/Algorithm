k = int(input())


for i in range(k):
    paper, point = map(int, input().split())
    test = list(map(int, input().split()))

    input = test[point]
    cnt = 0
    for l in range(paper):
        index = 0
        for m in range(1, paper):
            if test[m] > test[0]: 
                index = m
                
                for i in range(index):
                    test.append(test[0])
                    del test[0]

        cnt += 1

        if test[0] == input:
            print(cnt)
            break

        del test[0]
            


        for m in range(l):
            test.append(test[l])
            del test[0]
            
    print(point_index)
        

    
        