sum = int(input("Ввидите сумму наличных: "))

sum_5000 = sum//5000
sum = sum%5000

sum_2000 = sum//2000
sum = sum%2000

sum_1000 = sum//1000
sum = sum%1000

sum_500 = sum//500
sum = sum%500

sum_200 = sum//200
sum = sum%200

sum_100 = sum//100
sum = sum%100

print(f"купюр 5000: {sum_5000}, купюр 2000: {sum_2000}, купюр 1000: {sum_1000}, купюр 500: {sum_500}, купюр 200: {sum_200}, купюр 100: {sum_100}")
