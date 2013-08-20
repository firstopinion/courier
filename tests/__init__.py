# stdlib
import unittest

# artisan
import courier_test


def suite():
    """
    Gather all the tests from this package in a test suite.
    """

    test_suite = unittest.TestSuite()
    test_suite.addTest(courier.suite())
    return test_suite


# Execute from command line
if __name__ == "__main__":
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE)
