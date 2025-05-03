import unittest
from datetime import datetime
from kursinis import (
    StandardAccount,
    PremiumAccount,
    AccountManager
)

class TestAccountSystem(unittest.TestCase):

    def setUp(self):
        self.manager = AccountManager()
        # Reset singleton state
        self.manager._accounts.clear()

        self.user1 = StandardAccount("Jonas", "Jonaitis", "jonukas", datetime(2023, 1, 1))
        self.user2 = StandardAccount("Ona", "Onaitė", "ona123", datetime(2023, 1, 2))
        self.user3 = PremiumAccount("Petras", "Petraitis", "petras_p", datetime(2023, 1, 3))

        self.manager.add_account(self.user1)
        self.manager.add_account(self.user2)
        self.manager.add_account(self.user3)

    def test_add_friend_success(self):
        result = self.user1.add_friend(self.user2)
        self.assertTrue(result)
        self.assertIn(self.user2, self.user1.friends_list())
        self.assertIn(self.user1, self.user2.friends_list())

    def test_add_friend_limit(self):
        u = [StandardAccount(f"V{i}", f"P{i}", f"u{i}", datetime(2023, 1, 1)) for i in range(5)]
        for user in u:
            self.manager.add_account(user)
            self.user1.add_friend(user)
        sixth_friend = StandardAccount("Six", "Friend", "six", datetime(2023, 1, 1))
        self.manager.add_account(sixth_friend)
        result = self.user1.add_friend(sixth_friend)
        self.assertFalse(result)

    def test_add_friend_premium(self):
        self.user3.add_friend(self.user1)
        self.assertIn(self.user1, self.user3.friends_list())
        self.assertIn(self.user3, self.user1.friends_list())

    def test_update_to_premium(self):
        updated = self.manager.update_to_premium("jonukas")
        self.assertEqual(updated.account_type, "Premium")
        self.assertIsInstance(updated, PremiumAccount)

    def test_add_friend_by_username(self):
        self.manager.add_friend_by_username("jonukas", "ona123")
        self.assertIn(self.user2, self.user1.friends_list())

    def test_remove_friend_by_username(self):
        self.manager.add_friend_by_username("jonukas", "ona123")
        self.manager.remove_friend_by_username("jonukas", "ona123")
        self.assertNotIn(self.user2, self.user1.friends_list())
        self.assertNotIn(self.user1, self.user2.friends_list())

    def test_display_accounts(self):
        all_output = self.manager.display_all_accounts("All")
        self.assertIn("jonukas", all_output)
        self.assertIn("ona123", all_output)
        self.assertIn("petras_p", all_output)

    def test_remove_account(self):
        self.manager.add_friend_by_username("jonukas", "ona123")
        self.manager.remove_account(self.user1)
        self.assertNotIn(self.user1, self.manager.get_all_accounts())
        self.assertNotIn(self.user1, self.user2.friends_list())

if __name__ == "__main__":
    unittest.main()
