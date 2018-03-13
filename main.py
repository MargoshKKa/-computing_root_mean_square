# Написать функцию, которая принимает список целых чисел,
# реализует алгоритм нахождения среднего квадратичного (указанного списка)
# и возвращает результат
import computing


def main():
    data = []
    message = 'Enter integer number or "stop": '
    value = ''

    while value != 'stop':
        value = input(message)
        try:
            data.append(int(value))
        except ValueError:
            print("Could not convert data to an integer.")

    if not data:
        print("There are no numbers to calculate")
        return

    root = computing.root_mean_square(data)
    print(data)
    print(root)


if __name__ == '__main__':
    main()

