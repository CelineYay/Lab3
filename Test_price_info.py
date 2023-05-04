import price_info as p

def test_total_cost_shopping():
    test = 46.75
    result = p.total_cost_shopping()
    assert (result == test)

def test_cost_of_fruit():
    test_fruit = 'watermelon'
    test_quantity = 20
    result = p.cost_of_fruits(test_fruit, test_quantity)
    test = 130
    assert (result == test)