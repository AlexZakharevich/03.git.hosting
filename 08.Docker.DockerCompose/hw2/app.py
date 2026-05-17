import sys

def factorial(n):
    if n < 0:
        return "Ошибка: отрицательное число"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"Факториал {n} = {factorial(n)}")