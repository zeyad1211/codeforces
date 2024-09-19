number = list(input())
count = 0
for i in number:
    if count == 0 and i == '9':
        count += 1
        continue
    if int(i) > 4:
        number[count] = str(9 - int(i)) 
        
    count += 1
print(''.join(number))