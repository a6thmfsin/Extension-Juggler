import itertools
import random

def generate_combinations(extension1, extension2):
    return list(itertools.product(extension1, extension2))

def print_combinations(combinations, message="Combinations:"):
    print(message)
    for combination in combinations:
        print("".join(combination))

def generate_null_combinations(combinations, null_character="%00"):
    return ["".join(combination[:-1]) + null_character + combination[-1] for combination in combinations]

def add_null_at_end(combinations, null_character="%00"):
    return ["".join(combination) + null_character for combination in combinations]

def add_null_in_middle(combinations, null_character="\\x00"):
    return ["".join(combination[:-1]) + null_character + combination[-1] for combination in combinations]

php_extensions = [".php", ".xphp", ".html", ".pgif", ".phar", ".php3", ".php4", ".php5", ".php7", ".php8", ".phpt", ".pht", ".phtm", ".phtml", ".xphp"]
suffix_extensions = [".png", ".jpg", ".jpeg", ".mp3", ".gif"]

result = generate_combinations(php_extensions, suffix_extensions)

null_result = generate_null_combinations(result)

result_with_null_at_end = add_null_at_end(result)

result_with_null_in_middle = add_null_in_middle(result)

all_combinations = result + null_result + result_with_null_at_end + result_with_null_in_middle

random.shuffle(all_combinations)

print_combinations(all_combinations)
