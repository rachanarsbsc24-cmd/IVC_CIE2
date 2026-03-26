n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n = n // 10

sum_str = str(sum_digits)


if sum_str == sum_str[::-1]:
    print("Sum is Palindrome")
else:
    print("Sum is Not Palindrome")