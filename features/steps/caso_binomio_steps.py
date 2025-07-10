from behave import given, when, then
from examples.calculos import cuadrado_binomio

@given('ingreso los valores {a} y {b}')
def step_ingreso_valores(context, a, b):
    # Intentar convertir los valores a enteros si es posible
    try:
        context.a = int(a)
    except ValueError:
        context.a = a

    try:
        context.b = int(b)
    except ValueError:
        context.b = b

@when('calculo el cuadrado del binomio')
def step_calculo_binomio(context):
    context.resultado = cuadrado_binomio(context.a, context.b)

@then('el resultado del binomio debe ser {esperado}')
def step_verifico_resultado_binomio(context, esperado):
    if esperado == "None":
        assert context.resultado is None
    else:
        assert context.resultado == int(esperado)
