
number = int(input("Please input a number: "))

print(f"Multiplication table for {number}:")
for j in range(1, number+1):
    for i in range(1, 11):
        result = j * i
        print(f"{j} X {i} = {result}")

