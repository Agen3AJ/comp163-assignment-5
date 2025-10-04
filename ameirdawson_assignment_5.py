#Challenge Case 1
print("====  Challenge 1: Collatz Conjecture ====")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")

while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:   #number is even
        current_number //= 2
    else:                        #number is odd
        current_number = 3 * current_number + 1
    step_count += 1

print(1)  #
print("Steps:", step_count)
print()

#Challenge Case 2
print("==== Challenge 2: Prime Number Checker ====")
n = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {n-1}...")
is_prime = True

for divisor in range(2, n):
    if n % divisor == 0:
        print(f"{n} is not prime (divisible by {divisor})")
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime!")
    print()

#Challenge Case 3
print("==== Challenge 3: Multiplication Table ====")
print("Multiplication Table:")

print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:2}", end=" ")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()
