import unittest
from app.models import User

class Usertest(unittest.TestCase):

  def setUp(self):
    self.new_user = User(password = 'admin')

  def test_password_setter(self):
    self.assertTrue(self.new_user.passW is not None)

  def test_no_access(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_check_password(self):
    self.assertTrue(self.new_user.check_password('admin'))