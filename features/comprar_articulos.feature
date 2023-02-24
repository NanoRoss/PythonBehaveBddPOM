Feature: Comprar uno o varios articulos

  Background:
    Given Usuario se loguea con user "standard_user" y password "secret_sauce"

  @smoke
  Scenario: Comprar los primeros 2 Articulos
    When el usuario selecciona el artículo del inventario en la posición "1"
    And el usuario selecciona el artículo del inventario en la posición "2"
    And el usuario ingresa al carrito de compras
    And el usuario ingresa a checkout
    And el usuario completa el checkout
    Then el usuario finaliza su compra


