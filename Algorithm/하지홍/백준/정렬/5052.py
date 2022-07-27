T = int(input())

for _ in range(T):
    N = int(input())

    phonebook = []

    for _ in range(N):
        phonebook.append(input())

    phonebook.sort(key=str)

    flag = True

    for i in range(len(phonebook)-1):
        if phonebook[i] == phonebook[i+1][:len(phonebook[i])]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
