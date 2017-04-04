import unittest
from loancalculator import CalculateRepayment

class LoanCalculator(unittest.TestCase):
    def test_accurate_answer(self):
        self.assertEquals(CalculateRepayment(100000,12,12), 112020)
    #test if the answer for the given amount is equal to the expected result
    #for validating the correctness of the answer
    #other tests:loan repaid in 1 yr
    #amount is non decimal, rounded off to nearest integer
    #maximum principal is 200000
    #the defined interest rate is 14% p.a
    #most of the tests here so far are to check if the other tests are running because I have limited knowledge in equal
    #expressing these conditions in test cases

    def test_doesnt_execute_tests(self):
        for test in self.tests:
            self.assertFalse(test.called)
    def test_if_all_tests_passing(self):
        self.assertTrue(self.passed_tests.passed)
    #finally check if this argument returns true
    def test_if_one_of_the_tests_fail(self):
        self.assertFalse(self.mixed_result_tests.passed)
    #opposite of previous test
    def test_terminates_when_one_test_fails(self):
        """No more executing tests if one fails"""
        self.assertTrue(self.random_test.called)
        self.assertFalse(self.fake_test_passed.called)
        self.assertFalse(self.fake_failing_test.called)
     def test_loan_repayment_period_is_even_months(self):
        for i in range(0, 12):
            with self.loancalculator(i=i):
                self.assertEqual(i % 2, 0)

    


if __name__ == '__main__':
    unittest.main()