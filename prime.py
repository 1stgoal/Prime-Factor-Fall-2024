import math


# Function to generate prime factors for a given number.
def generate_prime_factors(test_input):
    while True:
        try:
            input_number = int(test_input)
            if input_number > 1:
                prime_factor_list = find_prime(input_number)  # Get prime numbers from find_prime function.
                return prime_factor_list  # Return the list of primes factors.
            if input_number == 1:
                return []
            else:
                raise ValueError
        except ValueError:
            raise ValueError


# Function to find prime factors of a number.
def find_prime(n):
    # Using square root to limit the number of divisions occurring in the program.
    square_root = math.sqrt(n)
    round_down = math.floor(square_root)

    factors_list = []

    # Iterating through all numbers from 2 up to the rounded square root of n.
    for divisor in range(2, round_down + 1):
        while n % divisor == 0:  # If n is divisible by divisor.
            factors_list.append(divisor)
            n = int(n / divisor)  # Divide n by divisor and continue factoring.

    # After all the division if  n is still > 1, it means n itself is prime.
    if n > 1:
        factors_list.append(n)

    return factors_list


# This is the main block to take the user input and generate prime factors.
if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            if user_input > 1:
                prime_factors_list = generate_prime_factors(user_input)
                print(prime_factors_list)
                break
            if user_input == 1:
                print("[]")
                break
            else:
                raise ValueError
        except ValueError:
            raise ValueError
