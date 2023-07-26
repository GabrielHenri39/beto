import re
from django.contrib import messages
from django.contrib.messages import constants



def password_is_valid(request, password, confirm_password):
    """
    Verifica se a senha é válida.

    Parâmetros:
    request -- O objeto de requisição do Django
    password -- A senha a ser validada
    confirm_password -- A confirmação da senha

    Retorna:
    True se a senha for válida, False caso contrário
    """

    if len(password.strip()) < 8:
        messages.add_message(request, constants.ERROR,
                             'Sua senha deve conter 8 ou mais caracteres')
        return False

    if not password.strip() == confirm_password.strip():
        messages.add_message(request, constants.ERROR,
                             'As senhas não coincidem!')
        return False

    if not re.search(r'[A-Z]', password.strip()):
        messages.add_message(request, constants.ERROR,
                             'Sua senha não contém letras maiúsculas')
        return False

    if not re.search(r'[a-z]', password.strip()):
        messages.add_message(request, constants.ERROR,
                             'Sua senha não contém letras minúsculas')
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password.strip()):
        messages.add_message(request, constants.ERROR,
                             'Sua senha não contém caracteres especiais')
        return False

    return True



