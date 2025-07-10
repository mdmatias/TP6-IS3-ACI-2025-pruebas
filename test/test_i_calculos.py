from examples.calculos import cuadrado_binomio

# Test cases for the cuadrado_binomio function

def test_cuadrado_binomio_correcto():
    assert cuadrado_binomio(2, 3) == 25  # (2 + 3)^2 = 25

def test_cuadrado_binomio_negativo():
    assert cuadrado_binomio(-1, 4) == 9

def test_cuadrado_binomio_invalido():
    assert cuadrado_binomio("a", 2) is None
