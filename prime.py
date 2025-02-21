def generate_prime_factors(user_input):
    while True:
        try:
            user_input = int(user_input)
            if user_input > 1:
                print("hi")
                break
            else:
                raise ValueError

        except ValueError:
            raise ValueError
            break


if __name__ == "__main__":
    generate_prime_factors(user_input=2)
