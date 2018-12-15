from Excercises.frequency import count_freq


def test_count_freq():
    result = count_freq([1, 1, 2, 2])
    expected = {
        1: 2, 2: 2
    }
    assert result == expected
