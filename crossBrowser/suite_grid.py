import unittest
import suite_all_tests_with_Chrome
#import suite_all_tests_with_Firefox

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestSuite()
    suite_chrome = suite_all_tests_with_Chrome.suite()
    #suite_firefox = suite_all_tests_with_Firefox.suite()
    suite.addTests(suite_chrome)
    #suite.addTests(suite_firefox)
    runner.run(suite)
