my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

my_ascending_sorted_list = sorted(my_list)
my_descending_sorted_list = sorted(my_list, reverse=True)

print("initial list: ", my_list)
print("ascending list: ", my_ascending_sorted_list)
print("descending list: ", my_descending_sorted_list)

print("even numbers of the list: ", end="")
for number in my_list[:]:
    if number % 2 == 0:
        print(number, end=" ")
print()

print("even numbers of the list using slice: ", my_ascending_sorted_list[1::2])

print("odd numbers of the list: ", end="")
for number in my_list[:]:
    if number % 2 == 1:
        print(number, end=" ")
print()

print("odd numbers of the list using slice: ", my_ascending_sorted_list[0::2])

print("numbers of the list that are multiples of 3: ", end="")
for number in my_list:
    if number % 3 == 0:
        print(number, end=" ")

