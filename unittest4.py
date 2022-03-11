from cmath import exp
import unittest
import pytest
from unittest.mock import Mock
import sys

sys.path.append("../")
from models.job_history import JobHistory
from models.database import Database


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.jbh = JobHistory("dd", "Alchemy", "India", "demo", "demo", "demo", "demo", "demo")
        Database.initialise(host="localhost", database="python-sql-assignment-suman", user="postgres", password="@SumanNehra", port='5432')

    def test_can_show_all_data(self):
        assert self.jbh.show_all_data() == None

    def test_can_save_to_db(self):
        self.assertRaises(Exception, self.jbh.save_to_db())