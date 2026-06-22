from web_sanity_check import WebSanityCheck, UserFlow
import pytest

def test_record_user_flow():
    wsc = WebSanityCheck()
    flow = UserFlow(["step1", "step2"])
    wsc.record_user_flow(flow)
    assert len(wsc.recorded_flows) == 1

def test_generate_tests():
    wsc = WebSanityCheck()
    flow = UserFlow(["step1", "step2"])
    wsc.record_user_flow(flow)
    tests = wsc.generate_tests()
    assert len(tests) == 1
    assert "assert step1 == 'step1'" in tests[0]
    assert "assert step2 == 'step2'" in tests[0]

def test_save_and_load_recorded_flows(tmp_path):
    wsc = WebSanityCheck()
    flow = UserFlow(["step1", "step2"])
    wsc.record_user_flow(flow)
    filename = tmp_path / "recorded_flows.json"
    wsc.save_recorded_flows(str(filename))
    wsc.recorded_flows = []
    wsc.load_recorded_flows(str(filename))
    assert len(wsc.recorded_flows) == 1
    assert wsc.recorded_flows[0].steps == ["step1", "step2"]

def test_generate_tests_coverage():
    wsc = WebSanityCheck()
    flow = UserFlow(["step1", "step2", "step3"])
    wsc.record_user_flow(flow)
    tests = wsc.generate_tests()
    assert len(tests) == 1
    assert "assert step1 == 'step1'" in tests[0]
    assert "assert step2 == 'step2'" in tests[0]
    assert "assert step3 == 'step3'" in tests[0]
    # Check that at least 80% of the user flow is covered
    assert len([line for line in tests[0].split("\n") if line.startswith("assert")]) >= len(flow.steps) * 0.8
