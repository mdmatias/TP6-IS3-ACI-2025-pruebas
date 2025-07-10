# Archivo con los tests unitarios

# python -m pip install pytest

import pytest
import example.liquidacion as lq

def setup():
    # Se define en esta clase una instancia de la clase a testear
    instancia = lq.Liquidacion()
    return instancia

def test_instancia_basica():
    un_empleado = setup()
    assert un_empleado.valor_hora == 550
    assert un_empleado.pct_bonificacion == 8
    assert un_empleado.pct_retenciones == 11
    assert un_empleado.pct_obraSocial == 3

def test_calcular_sueldo_basico():
    un_empleado = setup()
    hs_trabajadas = 40
    assert un_empleado.calcular_sueldo_basico(hs_trabajadas) == 22000.00

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (22000, 3, 25960.00),
        (22000, 6, 28160.00),
    ]
)
def test_calcular_sueldo_bruto(valor_a, valor_b, resultado):
    un_empleado = setup()
    assert un_empleado.calcular_sueldo_bruto(valor_a, valor_b) == resultado

# def ():
#     un_empleado = setup()
#     basico = 22000
#     antiguedad = 3
#     assert un_empleado.calcular_sueldo_bruto(basico, antiguedad) == 

def test_calcular_sueldo_neto():
    un_empleado = setup()
    bruto = 25960
    assert un_empleado.calcular_sueldo_neto(bruto) ==  22325.60

def test_calcular_sueldo_empleado():
    un_empleado = setup()
    hs_trabajadas = 40
    antiguedad = 3
    assert un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad) == 22325.60
