Feature: El usuario utiliza el LogOut del sitio

  Background:
    Given Usuario se loguea con user "standard_user" y password "secret_sauce"

  @smoke
  Scenario: El usuario Genera el LogOut
    When el usuario hace click en el burger menu
    And el usuario hace click LogOut
    Then el sistema hace logout al user y muestra la pantalla de login
