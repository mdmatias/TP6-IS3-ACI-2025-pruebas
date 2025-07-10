from behave import given, when, then
from examples.calculos import suma

@given('tengo los números {a} y {b}')
def step_given_tengo_los_numeros(context, a, b):
    context.a = int(a)
    context.b = int(b)

@when('los sumo')
def step_when_los_sumo(context):
    context.resultado = suma(context.a, context.b)

@then('el resultado de la suma debe ser {esperado:d}')
def step_then_el_resultado_de_suma(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, pero fue {context.resultado}"