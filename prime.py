def generate_prime_factors(user_input):
    while True:
        try:
            user_input = int(user_input)
            if user_input > 1:
                return user_input  # Return the number if it is greater than 1
                break
            if user_input == 1:
                return []
                break
            else:
                raise ValueError
        except ValueError:
            raise ValueError


if __name__ == "__main__":
    print(generate_prime_factors(15))
