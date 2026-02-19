def descending_number(num:int)->str:
    ''' Create a function returns the pattern as a string'''
    result = ""
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            result += str(j) + " "
        result += "\n"
    return result

user_input = int(input("Enter a number: "))

result_descending_number=descending_number(user_input)
print(result_descending_number)
print(descending_number.__doc__)

