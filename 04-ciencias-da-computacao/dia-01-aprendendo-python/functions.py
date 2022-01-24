def compare_numeros(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "números iguais"


if __name__ == "__main__":
    print(compare_numeros(11, 11))
