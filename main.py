import flet as ft
from views import views_handler


def main(page: ft.Page):
    pass

    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )

    page.on_route_change = route_change
    page.go('/')


ft.app(main)
