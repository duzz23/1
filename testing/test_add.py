from datetime import date
from sqlalchemy.orm import Session as SessionType
from create_db import create_user, Session


class TestCreateUser:
    def test_create_user(self):
        session: SessionType = Session()
        user = {
          "name": "Kelly Slater",
          "age": 50,
          "born": date(1972, 2, 11),
          "board": 3
          }

        result = create_user(session, **user)
        assert result.age == user.get("age")


