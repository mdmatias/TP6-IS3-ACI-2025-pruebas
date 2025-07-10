from behave import given, when, then
from app.calculos import suma

@given('tengo los números {a} y {b}')
def step_given_tengo_los_numeros(context, a, b):
    context.a = a
    context.b = b

@when('los sumo')
def step_when_los_sumo(context):
    context.resultado = suma(context.a, context.b)

@then('el resultado debe ser {esperado:d}')
def step_then_el_resultado_debe_ser(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, pero fue {context.resultado}"