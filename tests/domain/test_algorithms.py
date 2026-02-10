from app.domain.number_theory.algorithms import euclid_alg
from app.domain.linear_algebra.algorithms import symbolic_matrix_power


class TestEuclidAlg:
    def test_known_gcd(self):
        assert euclid_alg(12, 8) == 4

    def test_known_gcd_large(self):
        assert euclid_alg(270, 192) == 6

    def test_coprime(self):
        assert euclid_alg(13, 7) == 1

    def test_same_number(self):
        assert euclid_alg(5, 5) == 5

    def test_one_input_is_zero(self):
        assert euclid_alg(0, 7) == 7
        assert euclid_alg(7, 0) == 7


class TestSymbolicMatrixPower:
    def test_1x1_matrix(self):
        result = symbolic_matrix_power(1, 2)
        assert isinstance(result, str)

    def test_2x2_identity_power(self):
        result = symbolic_matrix_power(2, 1)
        assert isinstance(result, str)
        # m=1 means X^1, so result should contain the original symbols
        assert "x00" in result

    def test_returns_string(self):
        result = symbolic_matrix_power(2, 2)
        assert isinstance(result, str)
