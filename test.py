import unittest

class TestRunner:

    @staticmethod
    def run_all_tests():

        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        test_dir = './tests'
        suite.addTests(loader.discover(start_dir=test_dir, pattern='test_*.py'))

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if result.wasSuccessful():
            return 0
        else:
            return 1

if __name__ == '__main__':
    exit(TestRunner.run_all_tests())
