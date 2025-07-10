from behave import given, when, then
from examples.calculos import cuadrado

@given('ingreso el número {n}')
def step_ingreso_numero(context, n):
    try:
        context.numero = int(n)
    except ValueError:
        context.numero = n  # Guarda como string si no es número

@when('calculo el cuadrado')
def step_calculo_cuadrado(context):
    context.resultado = cuadrado(context.numero)

@then('el resultado debe ser {esperado}')
def step_verifico_resultado(context, esperado):
    if esperado == "None":
        assert context.resultado is None
    else:
        assert context.resultado == int(esperado)
