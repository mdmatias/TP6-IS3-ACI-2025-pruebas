# features/addition.feature
# esto es Gherkin

Feature: Suma de dos números

  Scenario: Sumar dos números positivos
    Given tengo los números 3 y 5
    When los sumo
    Then el resultado debe ser 8

  Scenario: Sumar un número positivo y un número negativo
    Given tengo los números 7 y -2
    When los sumo
    Then el resultado debe ser 5

  Scenario: Sumar dos números negativos
    Given tengo los números -4 y -6
    When los sumo
    Then el resultado debe ser -10