


def menu(choice):

    switcher = {
        "1": fun1,
        "2": fun2,
        "3": fun3,
        "4": fun4,
        "6": fun5
    }
    func = switcher.get(choice, lambda: "Неверный выбор")
    return func()


def fun1():
    print("введите а = ")
    a = int(input())
    print("введите b = ")
    b = int(input())
    print("введите c = ")
    c = int(input())
    print("введите d = ")
    d = int(input())
    s = a + b + c + d
    print(" s = ", s)


def fun2():
    text = input("Введите текст")
    words = text.split()

    new_text = ""

    for word in words:
        if word[-1] != "a":
            new_text += word + " "

    print(new_text)


def fun3():
    n = int(input())
    if n >= 2:
        nums = [int(input()) for i in range(n)]
        sums = []
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            sums.append(s)
        print(sums)
    else:
        print("Вы ввели размер меньше 2")


# ЗАДАНИЕ 4
def fun4():
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    if sorted(word1) == sorted(word2):
        print("Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")


def fun5():
    n = int(input("Введите количесто чисел первого множества = "))
    nums1 = [int(input()) for i in range(n)]
    v = int(input("Введите количество элементов второго множества = "))
    nums2 = [int(input()) for l in range(v)]

    for num in nums1:
        if num in nums2:
            print(num)


choice = input("Выберите задание (1-4,6): ")
menu(choice)
