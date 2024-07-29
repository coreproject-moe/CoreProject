import flet as ft

from .lib.views.login import login_view
from .lib.views.home import home_view
from .lib.components.navbar import navbar


async def main(page: ft.Page):
    page.title = "coreproject seeder"

    page.fonts = {
        "Kokoro": "fonts/Kokoro/Regular.ttf",
        "Kokoro-Medium": "fonts/Kokoro/Medium.ttf",
        "Kokoro-Bold": "fonts/Kokoro/Bold.ttf",
    }
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        font_family="Kokoro",
        color_scheme=ft.ColorScheme(
            secondary="#070519",
            primary="#7569E1",
            error="#EB5757",
        ),
    )
    page.padding = ft.padding.all(10)

    async def route_change(event: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [await navbar(page=page), await home_view(page=page)],
                bgcolor=ft.colors.SECONDARY,
                padding=10,
            )
        )
        if event.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [await login_view(page)],
                    bgcolor=ft.colors.SECONDARY,
                    padding=10,
                )
            )

        page.update()

    async def view_pop(event: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
