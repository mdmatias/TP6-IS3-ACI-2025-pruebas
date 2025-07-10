from example.calculos import suma, cuadrado
import pytest

# Testing the suma function
def test_suma():
    assert suma(2,5) == 7

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2, 3, 5),           
        (2, -3, -1), # suma de un entero negativo           
        (0, 5, 5),
        (None, 5, None),     
        (None, None, None), # para llegar al 100% de coverage     
        (2, None, None), # para llegar al 100% de coverage     
        ('2', 5, 7),
        (2, suma(2, 2), 6),
    ]
)
def test_varios_casos(valor_a, valor_b, resultado):
    assert suma(valor_a, valor_b) == resultado

def test_suma_str_letras():
     assert suma('a',5) == None

def test_suma_asoc():
    #propiedad asociativa
    assert suma(suma(2,2),2) == suma(2,suma(2,2))


#Testing the cuadrado function

def test_cuadrado_valor_positivo():
    assert cuadrado(3) == 9

def test_cuadrado_valor_negativo():
    assert cuadrado(-4) == 16

def test_cuadrado_valor_invalido():
    assert cuadrado("a") is None

