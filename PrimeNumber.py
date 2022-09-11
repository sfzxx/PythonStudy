# Determine whether a positive integer is prime.

print('Please enter a positive integer:')
num = input()
i = 2

if int(num) == 1:
    print(str(num) + ' is a prime number.')
else:
    while i < int(num):
        if int(num) % i == 0:
            break    # 存在因子，跳出循环,且为除1以外的最小因子
        i = i + 1

    if i == int(num):
        print(str(num) + ' is a prime number.')
    else:
        print(str(num) + ' is a composite number and ' + str(i) + ' is the minimum factor other than 1.')



