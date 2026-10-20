"""Demonstrate focused handling of invalid numeric input and zero division."""


def main() -> None:
    try:
        denominator = float(input("Enter a number to divide 100 by: "))
        result = 100 / denominator
    except ValueError:
        print("Please enter a valid number, such as -2, 1.5, or 5.")
    except ZeroDivisionError:
        print("The denominator cannot be zero.")
    else:
        print(f"100 / {denominator:g} = {result:g}")


if __name__ == "__main__":
    main()
