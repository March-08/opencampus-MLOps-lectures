from compute_launch import days_until_launch


def test_day_until_launch_4():
    assert days_until_launch(20, 24) == 4


def test_day_until_launch_10():
    assert days_until_launch(30, 40) == 10


def test_day_until_launch_negative():
    assert days_until_launch(30, 23) == -7
