from behave import *

@When('el usuario selecciona el artículo del inventario en la posición "{id}"')
def addToCartByID(context, id):
    context.InventoryPage.addToCartByID(id)

@When('el usuario ingresa al carrito de compras')
def goToCart(context):
    context.InventoryPage.goToCart()