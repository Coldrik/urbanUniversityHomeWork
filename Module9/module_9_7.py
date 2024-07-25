def is_prime(func):
    def wrapper(a,b,c):
        original_result = func(a,b,c)
        prime = True  #  Простое
        if abs(original_result) < 2:
            prime = True  #  Простое
        else:
            for i in range(2, original_result):
                if original_result % i == 0:
                    prime = False  #  Составное
                    break

                else:
                    prime = True  #  Простое
        if prime:
            print('Простое')
        else:
            print('Составное')

        return original_result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
