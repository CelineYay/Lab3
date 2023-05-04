import Lab2.bmi.ca as bmi

print("Test Lab2 BMI")


def test_bmi_normal_weight():
    result = []
    h_in = 1.5
    w_in = 80.0
    test_array = 0
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == test_array)


def test_bmi_over_weight():
    result = []
    h_in = 1.73
    w_in = 57
    test_array = 1
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == test_array)


def test_bmi_under_weight():
    result = []
    h_in = 1.6
    w_in = 45
    test_array = -1
    result = bmi.calculate_bmi(h_in, w_in)
    assert (result == test_array)
