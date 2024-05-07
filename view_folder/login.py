import flet as ft


class Login(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(controls=[ft.Container(height=800, width=350, bgcolor="blue")])


def login_view(page):
    return ft.View(route="/login", controls=[Login(page)])
