"""Small exercise: prices are integer cents, quantities are non-negative integers."""


def total_cents(items):
    """Return the total for (unit_price_cents, quantity) pairs.

    Inputs have already been validated by the caller.
    """
    return sum(unit_price for unit_price, quantity in items)
