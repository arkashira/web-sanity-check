from test_generator import generate_tests, calculate_coverage, UserFlow

def test_generate_tests():
    user_flows = [UserFlow(["step1", "step2"]), UserFlow(["step3", "step4"])]
    recording_tool = "Selenium"
    generated_tests = generate_tests(user_flows, recording_tool)
    assert len(generated_tests) == 2

def test_calculate_coverage():
    user_flows = [UserFlow(["step1", "step2"]), UserFlow(["step3", "step4"])]
    generated_tests = ["def test_Selenium_step1():\n    assert True\n", "def test_Selenium_step3():\n    assert True\n"]
    coverage = calculate_coverage(user_flows, generated_tests)
    assert coverage == 100.0

def test_calculate_coverage_partial():
    user_flows = [UserFlow(["step1", "step2"]), UserFlow(["step3", "step4"])]
    generated_tests = ["def test_Selenium_step1():\n    assert True\n"]
    coverage = calculate_coverage(user_flows, generated_tests)
    assert coverage == 50.0
