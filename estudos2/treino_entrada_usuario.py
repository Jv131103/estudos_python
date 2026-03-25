class UserInputError(Exception):
    pass


class StringEmptyError(UserInputError):
    pass


class NotebookOptionError(UserInputError):
    pass


class AgeNotIsValidError(UserInputError):
    pass


class AgeTypeError(UserInputError):
    pass


def empty_string(string: str) -> None:
    if not string:
        raise StringEmptyError("A string cannot be empty!")


def valid_age(age: str) -> int:
    empty_string(age)

    try:
        _age = int(age)
    except ValueError:
        raise AgeTypeError("age needs to be of the whole type.")

    if not (0 <= _age <= 115):
        raise AgeNotIsValidError("Age cannot be negative nor exceed the stipulated maximum limit of 115 years.")

    return _age


def username() -> str:
    name = input("What's your name? ").strip().title()
    empty_string(name)
    return name


def user_age() -> int:
    age = valid_age(input("How old are you?: ").strip())
    return age


def user_group() -> str:
    group = input("What's your class group? ").strip().upper()
    empty_string(group)
    return group


OPTIONS = {
    "yes": True,
    "no": False
}


def user_has_laptop() -> bool:
    has_laptop = input("Do you have a laptop? [yes / no] ").strip().lower()
    empty_string(has_laptop)
    option = OPTIONS.get(has_laptop)
    if option is None:
        raise NotebookOptionError("To confirm, simply type 'yes' or 'no'.")
    return option


def main():
    while True:
        try:
            name = username()
            age = user_age()
            group = user_group()
            has_laptop = user_has_laptop()

        except UserInputError as uie:
            print("--" * 30)
            print("An exception occurred.")
            print(uie)
        else:
            print("**" * 30)
            print("\t\tinfo: type datas")
            print("**" * 30)
            print(f"{name=}, type={type(name)}")
            print(f"{age=}, type={type(age)}")
            print(f"{group=}, type={type(group)}")
            print(f"{has_laptop=}, type={type(has_laptop)}")
            print("**" * 30)
            year_word = "year" if age == 1 else "years"
            print(f"Hello! My name is {name}, I'm {age} {year_word} old and I'm in class {group}.")
            print()

        print("==" * 30)
        again = input("AGAIN? [Y / N] ").strip().lower()
        if again != "y":
            break
        print("==" * 30)


main()
