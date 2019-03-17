from balanced_parentheses import match_open_close, balanced_parentheses


def test_length_2():
    assert balanced_parentheses(2) == {'()'}


def test_length_4():
    assert balanced_parentheses(4) == {'()()', '(())'}


def test_length_6():
    assert balanced_parentheses(6) == {
        '()()()',
        '((()))',
        '()(())',
        '(())()',
        '(()())',
    }


def test_open_close_close():
    assert match_open_close(1, 2) == {
        '())',
        ')()',
    }


def test_length_8():
    assert len(balanced_parentheses(8)) == 14


def test_length_10():
    assert len(balanced_parentheses(10)) == 42


def test_length_12():
    assert len(balanced_parentheses(12)) == 132
