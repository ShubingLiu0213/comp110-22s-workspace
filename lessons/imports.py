"""Examples of importing python."""

from lessons import helpers


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer is {helpers.The_ANSWER}")


if __name__ == "__main__":
    main()