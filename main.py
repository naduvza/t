import random


class Randomnumber:
    def __init__(self, *numbers):
        self.__numbers = numbers
        self.__result = self.__process_numbers()

    def __process_numbers(self):
        operation = random.choice(['+', '-', '*', '/'])
        result = self.__numbers[0]

        for num in self.__numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/':
                result /= num if num != 0 else 1

        return result

    def __str__(self):
        return f"Результат обчислень: {self.__result:.2f}"


cipher = Randomnumber(5, 10, 2)
print(cipher)
