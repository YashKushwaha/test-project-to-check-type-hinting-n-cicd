from typing import TypedDict


class User(TypedDict):
    name: str
    age: int


def get_user_age(user: User) -> int:
    return user["age"]