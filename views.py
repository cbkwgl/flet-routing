import flet as ft
from view_folder.home import *
from view_folder.login import *
from data.buttons import buttons

button_dict = {label: message for label, message in buttons}

print(button_dict)


def views_handler(page):
    return {
        "/": home_view(page),
        "/login": login_view(page),
    }
