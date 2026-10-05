def discounted_total(subtotal: float, coupon: str | None = None) -> float:
    """Total after a coupon: SAVE10 takes 10% off orders of 50 or more."""
    if coupon == "SAVE10" and subtotal >= 50:
        return round(subtotal * 0.9, 2)
    return subtotal
