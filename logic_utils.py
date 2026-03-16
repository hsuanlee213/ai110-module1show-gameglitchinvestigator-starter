def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIXME: Not yet implemented in `logic_utils.py`. Original logic lives in `app.py`.
    # Refactor `get_range_for_difficulty` from `app.py` here to centralize game logic.
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIXME: Not implemented. See parsing logic in `app.py.parse_guess`. Parsing must
    # normalize input to an integer and return (ok, value, error_message).
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    def _to_int(value):
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        if isinstance(value, str):
            try:
                if "." in value:
                    return int(float(value))
                return int(value)
            except Exception:
                raise TypeError("value is not numeric")
        raise TypeError("value is not numeric")

    try:
        g = _to_int(guess)
        s = _to_int(secret)
    except TypeError:
        raise TypeError("check_guess requires numeric-compatible inputs")

    if g == s:
        return "Win"
    if g > s:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIXME: Not implemented. Copy or adapt scoring rules from `app.py.update_score`
    # so tests and the app share the same scoring behavior.
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
