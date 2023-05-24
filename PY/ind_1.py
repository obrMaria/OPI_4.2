#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.
Поле first — дробное число; поле second — целое число, показатель степени. Реализовать
метод power() — возведение числа first в степень second. Метод должен правильно
работать при любых допустимых значениях first и second. Максимально задействовать имеющиеся в Python
средства перегрузки операторов"""


class Number:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if self.first == 0:
            raise ValueError

    def display(self):
        print(f"{self.first} ^ {self.second} = {self.first ** self.second}")

    def __pow__(self, other):
        return Number(self.first ** other.first, self.second * other.second)

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":
    num1 = Number(1.5, 4)
    num1.display()

    num2 = Number(2.1, 2)
    num2.display()

    result = num1 ** num2
    result.display()

    print(f"num1 == num2: {num1 == num2}")
    print(f"num1 != num2: {num1 != num2}")
