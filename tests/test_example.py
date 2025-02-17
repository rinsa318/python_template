from src.example import add, sub


class TestCalc:
    def test_add(self) -> None:
        assert add(1, 1) == 2

    def test_sub(self) -> None:
        assert sub(2, 1) == 1
