import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from kursinis import AccountManager, StandardAccount, PremiumAccount


class TestAccountFileImport(unittest.TestCase):

    def setUp(self):
        self.manager = AccountManager()
        self.manager._accounts.clear()

    def test_valid_account_file_loading(self):
        mock_file_data = """Jonas,Jonaitis,jonukas,2023-01-01,Standart
Ona,Onaitė,super_ona,2023-01-05,Premium
Emilija,Emil,Emma_xo,2023-02-10,Standart
Dominykas,Domauskas,Hey_Dom,2023-02-15,Premium
"""

        with patch("builtins.open", mock_open(read_data=mock_file_data)):
            with open("accounts_info.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    first_name, last_name, username, join_date, account_type = line.split(",")
                    join_date = datetime.strptime(join_date, "%Y-%m-%d")

                    if account_type == "Standart":
                        account = StandardAccount(first_name, last_name, username, join_date)
                    elif account_type == "Premium":
                        account = PremiumAccount(first_name, last_name, username, join_date)
                    else:
                        continue

                    self.manager.add_account(account)

        usernames = [acc.username for acc in self.manager.get_all_accounts()]
        expected_usernames = ["jonukas", "super_ona", "Emma_xo", "Hey_Dom"]
        self.assertCountEqual(usernames, expected_usernames)

        super_ona = self.manager.get_account_by_username("super_ona")
        self.assertEqual(super_ona.account_type, "Premium")

    def test_invalid_date_format(self):
        mock_data = """Jonas,Jonaitis,jonukas,2023-01-01,Standart
Ona,Onaitė,super_ona,01-05-2023,Premium
"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            with self.assertRaises(ValueError):
                with open("accounts_info.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                        first_name, last_name, username, join_date, account_type = line.split(",")
                        # Klaidingas datos formatas:
                        join_date = datetime.strptime(join_date, "%Y-%m-%d")

    def test_unknown_account_type_ignored(self):
        mock_data = """Jonas,Jonaitis,jonukas,2023-01-01,Standart
Kazys,Kazlauskas,kazys,2023-01-02,Gold
Ona,Onaitė,super_ona,2023-01-05,Premium
"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            with open("accounts_info.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    first_name, last_name, username, join_date, account_type = line.split(",")
                    join_date = datetime.strptime(join_date, "%Y-%m-%d")

                    if account_type == "Standart":
                        account = StandardAccount(first_name, last_name, username, join_date)
                    elif account_type == "Premium":
                        account = PremiumAccount(first_name, last_name, username, join_date)
                    else:
                        continue

                    self.manager.add_account(account)

        usernames = [acc.username for acc in self.manager.get_all_accounts()]
        self.assertIn("jonukas", usernames)
        self.assertIn("super_ona", usernames)
        self.assertNotIn("kazys", usernames)

    def test_empty_file(self):
        mock_data = ""  # Tuščias failas

        with patch("builtins.open", mock_open(read_data=mock_data)):
            with open("accounts_info.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    first_name, last_name, username, join_date, account_type = line.split(",")
                    join_date = datetime.strptime(join_date, "%Y-%m-%d")
                    if account_type == "Standart":
                        account = StandardAccount(first_name, last_name, username, join_date)
                    elif account_type == "Premium":
                        account = PremiumAccount(first_name, last_name, username, join_date)
                    else:
                        continue
                    self.manager.add_account(account)

        self.assertEqual(len(self.manager.get_all_accounts()), 0)


if __name__ == "__main__":
    unittest.main()
