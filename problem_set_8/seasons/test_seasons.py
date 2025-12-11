from seasons import calculate_minutes
import pytest

def tests_valid_calculate_minutes():
    assert calculate_minutes("2005-11-28") == "ten million, five hundred, thirty-six thousand, four hundred, eighty minutes"
    assert calculate_minutes("2024-12-10") == "five hundred, twenty-five thousand, six hundred minutes"
    assert calculate_minutes("2023-12-10") == "one million, fifty-two thousand, six hundred, forty minutes"

def tests_invalid_calculate_minutes():
    with pytest.raises(ValueError):
        calculate_minutes("200523")
    with pytest.raises(ValueError):
        calculate_minutes("January, 3 2025")
    with pytest.raises(ValueError):
        calculate_minutes("12-10-2023")