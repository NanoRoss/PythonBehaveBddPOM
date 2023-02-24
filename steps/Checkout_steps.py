from behave import *

@When('el usuario ingresa a checkout')
def goToCheckout(context):
    context.CheckoutPage.goToCheckout()

@When('el usuario completa el checkout')
def completeCheckoutAndOverview(context):
    context.CheckoutPage.completeCheckoutAndOverview()

@Then('el usuario finaliza su compra')
def validateSuccessfulPurchase(context):
    result = context.CheckoutPage.validateSuccessfulPurchase()
    assert result == True, "La compra no fue exitosa"