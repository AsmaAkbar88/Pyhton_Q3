from add import add


def tests_main():
    result = add(4 , 4)
    assert result == 8 , "4+4 should be 8"


tests_main()