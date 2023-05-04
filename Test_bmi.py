import Lab2.bmi as bmi

print("Test Lab2 BMI")


def test_bmi_normal_weight():
    h_in = 1.75
    w_in = 57
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == 0)


def test_bmi_over_weight():
    h_in = 1.5
    w_in = 80
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == 1)


def test_bmi_under_weight():
    h_in = 1.6
    w_in = 45
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == -1)
