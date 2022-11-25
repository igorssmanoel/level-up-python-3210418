def get_prime_factors(number):
    new_number = number
    result = []
    i = 2
    while (new_number > 1):
        if (new_number % i == 0):
            result.append(i)
            new_number = new_number // i
        else:
            i += 1
    return result


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
    print(get_prime_factors(256))
