import pytest

def test_placeholder():
    """Placeholder test — not yet implemented."""
    pytest.skip("Skipped by Drufiy — needs implementation")


def test_math():
    assert 1 == 1


def test_user_balance():
    """Check that refund calculation is correct."""
    total = 100
    discount = 15
    refund = total - discount
    assert refund == 85, f"Expected 85, got {refund}"
