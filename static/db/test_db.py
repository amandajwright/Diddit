import unittest
import db

class Db_test(unittest.TestCase):
    def test_wrong_path(self):
        self.assertFalse(db.check_db('wrong_path'))
    def test_file_not_exist(self):
        self.assertFalse(db.check_db('file:static/to_do_list.db'))


if __name__ == '__main__':
    unittest.main()