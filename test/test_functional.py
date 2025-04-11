import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv", "salary_data.csv")
        cls.test_obj = TestUtils()

    def test_merge_data(self):
        """Test if the employee and salary data are merged correctly."""
        try:
            merged_data = self.analysis.merge_data()
            obj = "Employee_ID" in merged_data.columns and "Salary" in merged_data.columns
            self.test_obj.yakshaAssert("TestMergeData", obj, "functional")
            print("TestMergeData = Passed" if obj else "TestMergeData = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestMergeData", False, "functional")
            print("TestMergeData = Failed")

    def test_display_head(self):
        """Test if the first 5 rows of the merged DataFrame are returned correctly."""
        try:
            self.analysis.merge_data()
            head = self.analysis.display_head()
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDisplayHead", False, "functional")
            print("TestDisplayHead = Failed")

    def test_average_salary_per_department(self):
        """Test if the average salary for each department is calculated correctly."""
        try:
            self.analysis.merge_data()
            avg_salary = self.analysis.calculate_average_salary()
            obj = avg_salary["HR"] == 50000.0
            self.test_obj.yakshaAssert("TestAverageSalaryPerDepartment", obj, "functional")
            print("TestAverageSalaryPerDepartment = Passed" if obj else "TestAverageSalaryPerDepartment = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAverageSalaryPerDepartment", False, "functional")
            print("TestAverageSalaryPerDepartment = Failed")

    def test_save_to_excel(self):
        """Test if the merged DataFrame is saved to an Excel file."""
        try:
            self.analysis.save_to_excel("merged_employee_data.xlsx")
            obj = os.path.exists("merged_employee_data.xlsx")
            self.test_obj.yakshaAssert("TestSaveToExcel", obj, "functional")
            print("TestSaveToExcel = Passed" if obj else "TestSaveToExcel = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveToExcel", False, "functional")
            print("TestSaveToExcel = Failed")
