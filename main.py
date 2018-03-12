# Написать функцию, которая принимает список целых чисел,
# реализует алгоритм нахождения среднего квадратичного (указанного списка)
# и возвращает результат
import computing

data = []
message = 'Enter integer number or "stop": '
value = input(message)
while value != 'stop':
    try:
        data.append(int(value))
        value = input(message)
    except (ValueError):
        print("Could not convert data to an integer.")
        value = input(message)
    except:
        print("Unexpected error")
        raise

root = computing.root_mean_square(data)
print(data)
print(root)
