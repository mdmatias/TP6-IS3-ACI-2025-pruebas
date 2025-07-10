Feature: Calcular el cuadrado de un número

  Scenario: El usuario ingresa el número 5
    Given ingreso el número 5
    When calculo el cuadrado
    Then el resultado debe ser 25

  Scenario: El usuario ingresa el número -4
    Given ingreso el número -4
    When calculo el cuadrado
    Then el resultado debe ser 16

  Scenario: El usuario ingresa el número 0
    Given ingreso el número 0
    When calculo el cuadrado
    Then el resultado debe ser 0

  Scenario: El usuario ingresa un valor no numérico
    Given ingreso el número "hola"
    When calculo el cuadrado
    Then el resultado debe ser None
