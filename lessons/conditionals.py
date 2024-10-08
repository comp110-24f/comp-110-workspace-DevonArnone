"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


print(less_than_10(num=2))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
