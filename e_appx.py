def e_appx(num):
    e = 1

    for i in range(1, num + 1):
        e += 1/(factorial(i))
    return e


def factorial(num):
    if (not isinstance(num, int)):
        return None
    if (num <= 1):
        return 1
    return num * factorial(num - 1)


num = int(input("Enter the number of terms to be used for approximation: "))
approx_e = e_appx(num)
print(f"The approximation of e using {num} terms is {approx_e}")
