calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(some_string: str) -> tuple:
    count_calls()
    return (len(some_string), some_string.upper(), some_string.lower())


def is_contains(some_string, some_list) -> bool:
    count_calls()
    return some_string.lower() in [item.lower() for item in some_list]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
