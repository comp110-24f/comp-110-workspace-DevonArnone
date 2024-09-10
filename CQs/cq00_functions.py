__author__ = "730751173"


def mimic(message: str) -> str:
    """Return message back to you"""
    return message


def main() -> None:
    """Print result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
