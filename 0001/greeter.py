from dataclasses import dataclass
from time import sleep
@dataclass
class User:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def main():
    while True:
        print("Welcome to Blackwood Code Works.")
        print("\nPlease tell us your name below:")

        user_name = input()
        sleep(1)
        print("\nWorking on it...\n")
        sleep(1)
        print(f"{user_name} you say? We will check that with our internal database..\n")
        sleep(1)
        print("\nThe second thing we need is your age which you can enter below:")
        user_age_raw = input()
        sleep(1)

        try:
            user_age = int(user_age_raw)
        except ValueError:
            print(f"{user_age_raw!r} eh? what is that supposed to be.. please enter a valid number")
            continue

        if user_age <= 0:
            print(f"{user_age} years young?! We will check that with our internal database..\n\n")
        elif user_age <= 18:
            print(f"{user_age} years old? We will check that with our internal database as well..\n\n")
        else:
            print(f"{user_age} years? Let us check that with our internal database as well..\n\n")

        sleep(1)
        print("Right on. You can now enter our lovely firm. We will get back to you once the checks are done.")
        user: User = User(user_name, user_age)
        exit(0)
main()
