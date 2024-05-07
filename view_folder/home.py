import flet as ft


class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.ElevatedButton(text="Hi", on_click=lambda _: self.page.go("/login"))
            ]
        )


def home_view(page):
    return ft.View(route="/", controls=[Home(page)])
