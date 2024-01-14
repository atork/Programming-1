numbers = []
while True:
    num = input('Enter a number or type "done" when finished: ')
    if num == 'done':
        break
    numbers.append(num)
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

