from functools import reduce


def pr (num1,num2) : 
    return num1*num2
nums = [2, 4, 6, 2]
result = reduce(pr,nums)
print(result)

# avec lambda function 
print("="*50)
resulte = reduce (lambda n1,n2 : n1*n2 , nums)
print(result)