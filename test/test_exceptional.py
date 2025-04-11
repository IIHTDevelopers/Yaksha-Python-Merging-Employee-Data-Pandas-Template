import unittest
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

    def test_invalid_csv_path(self):
        """Test handling of a non-existent CSV file."""
        try:
            analysis = EmployeeDataAnalysis("non_existent_employee_data.csv", "salary_data.csv")
            self.test_obj.yakshaAssert("TestInvalidCsvPath", False, "exceptional")
            print("TestInvalidCsvPath = Failed")
        except:
            self.test_obj.yakshaAssert("TestInvalidCsvPath", True, "exceptional")
            print("TestInvalidCsvPath = Passed")

    def test_missing_column_in_csv(self):
        """Test handling of missing column in the CSV."""
        try:
            analysis = EmployeeDataAnalysis("missing_column_employee_data.csv", "salary_data.csv")
            analysis.merge_data()
            self.test_obj.yakshaAssert("TestMissingColumnInCsv", False, "exceptional")
            print("TestMissingColumnInCsv = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestMissingColumnInCsv", True, "exceptional")
            print("TestMissingColumnInCsv = Passed")
