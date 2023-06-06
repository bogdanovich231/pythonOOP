import time

numbers = range(1000, 52665)

start_time = time.time()

stack = []
queue = []

for number in numbers:
    queue.append(number)

while queue:
    stack.append(queue.pop(0))

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

with open("time.txt", "w") as file:
    file.write(f"Execution time: {execution_time} seconds")