import sys
str = sys.argv[1].upper()

if str.isalpha() != True:
    print("Invalid String")
    exit()

visited = [0 for i in range(len(str))]
output = 0

for i, char in enumerate(str):
    if visited[i] != 1:
        visited[i] = 1
        if i+1 < len(str):
            if char == 'I':   
                if str[i+1] == 'V':
                    visited[i+1] = 1
                    output = output + 4
                elif str[i+1] == 'X':
                    visited[i+1] = 1
                    output = output + 9
                else:
                    output = output + 1
            elif char == 'V':
                output = output + 5
            elif char == 'X':
                if str[i+1] == 'L':
                    visited[i+1] = 1
                    output = output + 40
                elif str[i+1] == 'C':
                    visited[i+1] = 1
                    output = output + 90
                else:
                    output = output + 10
            elif char == 'L':
                output = output + 50
            elif char == 'C':
                if str[i+1] == 'D':
                    visited[i+1] = 1
                    output = output + 400
                elif str[i+1] == 'M':
                    visited[i+1] = 1
                    output = output + 900
                else:
                    output = output + 100
            elif char == 'D':
                output = output + 500
            elif char == 'M':
                output = output + 1000
            else:
                print("Invalid String")
                exit()
        else:
            if char == 'I':
                output = output + 1
            elif char == 'V':
                output = output + 5
            elif char == 'X':
                output = output + 10
            elif char == 'L':
                output = output + 50
            elif char == 'C':
                output = output + 100
            elif char == 'D':
                output = output + 500
            elif char == 'M':
                output = output + 1000
            else:
                print("Invalid String")
                exit()

print(output)