Feature: Calcular el cuadrado de un binomio

  Scenario: El usuario ingresa los valores 2 y 3
    Given ingreso los valores 2 y 3
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser 25

  Scenario: El usuario ingresa los valores -1 y 4
    Given ingreso los valores -1 y 4
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser 9

  Scenario: El usuario ingresa los valores 0 y 5
    Given ingreso los valores 0 y 5
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser 25


  Scenario: El usuario ingresa un valor no numérico
    Given ingreso los valores "a" y 3
    When calculo el cuadrado del binomio
    Then el resultado del binomio debe ser None
