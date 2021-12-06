def test_matrix():
    try:
        get_determinant([]):
    except ValueError as e:
        assert str(e) == "EMPTY"
    try:
        get_determinant([[0],[0,0]])
    except ValueError as e:
        assert str(e) == "CANT DO"

    assert get_determinant([1,1],[1,1]) == 0
    assert get_determinant([1,2],[3,4]) == -2

