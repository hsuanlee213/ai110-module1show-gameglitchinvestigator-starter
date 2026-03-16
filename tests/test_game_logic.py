from logic_utils import (
    check_guess,
    parse_guess,
    get_range_for_difficulty,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_valid_and_decimal():
    ok, val, err = parse_guess("42")
    assert ok is True and val == 42 and err is None

    ok, val, err = parse_guess("3.0")
    assert ok is True and val == 3 and err is None


def test_parse_guess_invalid_and_empty():
    ok, val, err = parse_guess("")
    assert ok is False and val is None and err == "Enter a guess."

    ok, val, err = parse_guess(None)
    assert ok is False and val is None and err == "Enter a guess."

    ok, val, err = parse_guess("abc")
    assert ok is False and val is None and err == "That is not a number."


def test_get_range_for_difficulty_levels():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_update_score_behaviour():
    # Win gives points and respects minimum
    assert update_score(0, "Win", 0) == 90
    assert update_score(0, "Win", 100) == 10

    # Too High: even attempt -> +5, odd -> -5
    assert update_score(0, "Too High", 2) == 5
    assert update_score(10, "Too High", 1) == 5

    # Too Low: always -5
    assert update_score(10, "Too Low", 1) == 5
