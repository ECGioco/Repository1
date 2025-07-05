print("Hello from Both")
def mean(numbers):
    return sum(numbers)/len(numbers)
def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]