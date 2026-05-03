def test_placeholder():
    """Placeholder test — not yet implemented."""
    assert False, "This test is not implemented yet"


def test_math():
    assert 1 == 1


def test_user_balance():
    """Check that refund calculation is correct."""
    total = 100
    discount = 15
    refund = total - discount
    assert refund == 90, f"Expected 90, got {refund}"  # bug: 100-15=85, not 90
