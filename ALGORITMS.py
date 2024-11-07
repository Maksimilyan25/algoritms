# Удаление дубликатов.

num_lines = int(input())
score = 0
first_list = [int(s) for s in input().split()]

second_list = first_list[:1]
for i in range(1, num_lines):
    if first_list[i - 1] != first_list[i]:
        second_list.append(first_list[i])
    else:
        score += 1
second_list.extend('_' * score)
print(*second_list)


# Определение индекса для вставки.

def check_element_in_list(desired_element, ordered_list):
    left, right = 0, len(ordered_list)
    while left < right:
        mid = (left + right) // 2
        if ordered_list[mid] < desired_element:
            left = mid + 1
        else:
            right = mid
    return left  # индекс либо найденного, либо позиции, где должен быть

first_list = [int(x) for x in input().split()]
my_score = int(input())
result = check_element_in_list(my_score, first_list)
print(result)

# Неправильные горы.

def valid_mountain_array(arr):

    n = len(arr)

    # Проверка длины массива
    if n < 3:
        return False

    i = 0

    # Восхождение
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Проверка, что достигли пика
    if i == 0 or i == n - 1:
        return False

    # Спуск
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # Проверка, что дошли до конца массива
    return i == n - 1

# Пример использования:
arr = list(map(int, input().split()))
print(valid_mountain_array(arr))
