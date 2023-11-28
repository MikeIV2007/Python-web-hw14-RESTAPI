import unittest
from unittest.mock import MagicMock
from datetime import datetime

from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel
from src.repository.users import (
    get_user_by_email,
    create_user,
    update_token,
    confirmed_email,
    update_avatar,
)


class TestUsers(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_user_by_email(self):
        test_user = User()
        self.session.query().filter().first.return_value = test_user
        result = await get_user_by_email("test@test.com", self.session)
        self.assertEqual(result, test_user)

    async def test_get_user_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await get_user_by_email("test@test.com", self.session)
        self.assertIsNone(result)

    async def test_create_user(self):
        body = UserModel(
            username="username",
            email="test@test@email",
            password="1234456",
        )
        result = await create_user(body, self.session)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.password, body.password)
        self.assertTrue(hasattr(result, "id"))
        self.assertTrue(hasattr(result, "created_at"))
        self.assertTrue(hasattr(result, "avatar"))
        self.assertTrue(hasattr(result, "refresh_token"))
        self.assertTrue(hasattr(result, "confirmed"))

    async def test_update_token(self):
        new_token = "new_refresh_token"
        result = await update_token(self.user, new_token, self.session)
        self.assertEqual(result, new_token)
        self.session.commit.assert_called_once()

    async def test_confirmed_email(self):
        email = "test@test.com"
        result = await confirmed_email(email, self.session)
        self.assertEqual(result, True)
        self.session.commit.assert_called_once()

    async def test_update_avatar(self):
        email = "test@test.com"
        new_url = "new_url"
        result = await update_avatar(email, new_url, self.session)
        self.assertEqual(result.avatar, new_url)


if __name__ == "__main__":
    unittest.main()
