from pricing import discounted_total


def test_no_coupon_keeps_the_subtotal():
    assert discounted_total(80) == 80
