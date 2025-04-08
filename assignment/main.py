# Loop through two-digit numbers and check if they are prime
for num in range(10, 100):
    if all(num % i != 0 for i in range(2, num)):
        print(num)
