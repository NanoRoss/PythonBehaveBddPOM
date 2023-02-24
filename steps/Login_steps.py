from behave import *


@Given('Usuario se loguea con user "{username}" y password "{password}"')
def login(context, username, password):
    context.LoginPage.login(username, password)





