def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value < target:
            left = mid + 1
        elif mid_value >= target:
            right = mid - 1

    return left


def custom_sort(arr):
    # Сортировка списка по возрастанию (можно использовать стандартную функцию sorted)
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    try:
        # Ввод последовательности чисел
        input_sequence = input("Введите последовательность чисел через пробел: ")
        numbers = [float(num) for num in input_sequence.split()]

        # Проверка на наличие чисел в последовательности
        if not numbers:
            print("Пустая последовательность чисел.")
            return

        # Ввод числа, с которым будем сравнивать
        target_number = float(input("Введите любое число: "))

        # Сортировка списка чисел
        sorted_numbers = custom_sort(numbers)

        # Поиск позиции элемента с помощью двоичного поиска
        position = binary_search(sorted_numbers, target_number)

        # Проверка на валидность позиции
        if position >= len(sorted_numbers):
            print("Нет элементов, удовлетворяющих условию.")
        else:
            print("Позиция элемента в отсортированной последовательности:", position)
            print("Элемент:", sorted_numbers[position])
    except ValueError:
        print("Ошибка ввода. Введите числа через пробел.")
    except Exception as e:
        print("Произошла ошибка:", e)


if __name__ == "__main__":
    main()
