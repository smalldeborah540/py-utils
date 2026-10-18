import pytest

from retry import retry


def test_succeeds_after_failures():
    calls = {"n": 0}

    @retry(tries=3, delay=0.01)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError("transient")
        return "ok"

    assert flaky() == "ok"
    assert calls["n"] == 2


def test_raises_after_exhaustion():
    @retry(tries=2, delay=0.01)
    def always_fails():
        raise RuntimeError("nope")

    with pytest.raises(RuntimeError):
        always_fails()
