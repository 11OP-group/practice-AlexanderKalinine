numb = int(input("ввидите числo: "))
copy = numb

count_3 = 0
count_last = 0
even_count = 0
sum_greater_5 = 0
product_greater_7 = 1
number_7 = False
count_0_and_5 = 0

last_numb = numb % 10

while copy > 0:
    digit = copy % 10
    copy = copy // 10
    if digit == 3:
        count_3 = count_3 + 1
    if digit == last_numb:
        count_last = count_last + 1
    if digit % 2 == 0:
        even_count = even_count + 1
    if digit > 5:
        sum_greater_5 = sum_greater_5 + digit
    if digit > 7:
        product_greater_7 = product_greater_7 * digit
    if digit == 0 or digit == 5:
        count_0_and_5 += 1

print(count_3)
print(count_last)
print(even_count)
print(sum_greater_5)
if product_greater_7 == 1:
    print(1)
else:
    print(product_greater_7)
print(count_0_and_5)