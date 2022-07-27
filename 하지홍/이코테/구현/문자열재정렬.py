S = list(input())

string_array = []
int_array = []

for elem in S:
    if elem.isalpha():
        string_array.append(elem)
    else:
        int_array.append(elem)
        
string_array.sort()
int_array.sort()

for elem in int_array:
    string_array.append(elem)
    
result = ''.join(elem for elem in string_array)

print(result)