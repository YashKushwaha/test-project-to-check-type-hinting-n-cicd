from app.users import get_user_age


def test_user_age() -> None:
    user = {
        "name": "Alice",
        "age": 30,
    }

    assert get_user_age(user) == 30