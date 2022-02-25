from pyleague import rounds


def test_rounds():
    even_number = rounds(list("ABCD"))
    assert next(even_number) == [("A", "D"), ("C", "B")]
    assert next(even_number) == [("C", "A"), ("B", "D")]
    assert next(even_number) == [("A", "B"), ("D", "C")]
    assert next(even_number) == [("D", "A"), ("B", "C")]
    assert next(even_number) == [("A", "C"), ("D", "B")]
    assert next(even_number) == [("B", "A"), ("C", "D")]

    odd_number = rounds(list("BCD"))
    assert next(odd_number) == [("C", "B")]
    assert next(odd_number) == [("B", "D")]
    assert next(odd_number) == [("D", "C")]
    assert next(odd_number) == [("B", "C")]
    assert next(odd_number) == [("D", "B")]
    assert next(odd_number) == [("C", "D")]
