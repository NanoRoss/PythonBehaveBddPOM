from behave import *


@When('el usuario hace click en el burger menu')
def openBurgerMenu(context):
    context.InventoryPage.openBurgerMenu()

@When('el usuario hace click LogOut')
def clickLogOut(context):
    context.InventoryPage.clickLogOut()

@Then('el sistema hace logout al user y muestra la pantalla de login')
def validateUserAreInLogin(context):
    result = context.LoginPage.validateUserAreInLogin()
    assert result == True, "La compra no fue exitosa"


