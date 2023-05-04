import Lab2.temp as temperature

print("test lab 2 temp")


def test_find_min_max():
    in_x = [19.9, 33.5, 78.2, 11.3]
    test_arr = [11.3, 78.2]
    result = temperature.find_min_max(in_x)
    assert (result == test_arr)

def test_calc_ave():
    in_x = [19.9, 33.5, 78.2, 11.3]
    test = 35.725
    result = temperature.calc_average(in_x)
    assert (result == test)

def test_calc_median_temperature():
    in_x = [19.9, 33.5, 78.2, 11.3]
    test = 55.85
    result = temperature.calc_median_temperature(in_x)
    assert (result == test)
