from web_sanity_check import WebSanityCheck, TestResult

def test_get_flaky_tests():
    web_sanity_check = WebSanityCheck()
    web_sanity_check.add_test_result("test1", 40, "file1.py", 10)
    web_sanity_check.add_test_result("test2", 20, "file2.py", 20)
    web_sanity_check.add_test_result("test3", 50, "file3.py", 30)
    flaky_tests = web_sanity_check.get_flaky_tests()
    assert len(flaky_tests) == 2
    assert flaky_tests[0].test_name == "test1"
    assert flaky_tests[1].test_name == "test3"

def test_mark_test_as_investigated():
    web_sanity_check = WebSanityCheck()
    web_sanity_check.add_test_result("test1", 40, "file1.py", 10)
    web_sanity_check.mark_test_as_investigated("test1")
    flaky_tests = web_sanity_check.get_flaky_tests()
    assert len(flaky_tests) == 0

def test_get_flaky_tests_empty():
    web_sanity_check = WebSanityCheck()
    flaky_tests = web_sanity_check.get_flaky_tests()
    assert len(flaky_tests) == 0

def test_mark_test_as_investigated_not_found():
    web_sanity_check = WebSanityCheck()
    web_sanity_check.add_test_result("test1", 40, "file1.py", 10)
    web_sanity_check.mark_test_as_investigated("test2")
    flaky_tests = web_sanity_check.get_flaky_tests()
    assert len(flaky_tests) == 1
    assert flaky_tests[0].test_name == "test1"
