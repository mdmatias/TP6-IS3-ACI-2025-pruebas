# Archivo con los tests de integración

# python -m pip install pytest
# conda install pytest

import pytest
import example.liquidacion as lq

def setup():
    # Se define en esta clase una instancia de la clase a testear
    instancia = lq.Liquidacion()
    return instancia

def test_integrado():
    un_empleado = setup()
    hs_trabajadas = 160
    antiguedad = 3
    total_fc = un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad)
    
    basico = un_empleado.calcular_sueldo_basico(hs_trabajadas)    
    bruto = un_empleado.calcular_sueldo_bruto(basico, antiguedad)
    total_fs = un_empleado.calcular_sueldo_neto(bruto)

    assert total_fc == total_fs