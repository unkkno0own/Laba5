N = int(input("Введіть довжину масива: "))

array = []
for i in range(N):
    element = float(input(f"Введіть елемент {i + 1}: "))
    array.append(element)

max_element = max(array)

print("Максимальний елемент масива:", max_element)
