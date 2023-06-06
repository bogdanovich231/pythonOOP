import time

def kurgan_sort(numbers):
    n = len(numbers)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                sorted = False


numbers = [4, 10, 11, 5, 73, 5, 1, 4, 10, 11, 5, 73, 5, 1]

start_time = time.time()

kurgan_sort(numbers)

end_time = time.time()
execution_time = end_time - start_time

print(f"Kurgan Sort Execution time: {execution_time} seconds")

end_time = time.time()
execution_time = end_time - start_time
sorted_numbers = sorted(numbers)

print(f"Quick Sort time: {execution_time} seconds")

with open("time_2.txt", "w") as file:
    file.write(f"Kurgan Sort time: {execution_time} seconds")

