import flet as ft

from seeder_flet.lib.views.login import login_view
from seeder_flet.lib.views.home import home_view
from seeder_flet.lib.components.navbar import navbar


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
            secondary="#03020c",
            tertiary="#1E2036",
            primary="#7569E1",
        ),
    )

    async def route_change(event: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [await navbar(page), await home_view(page)],
                bgcolor=ft.colors.SECONDARY,
                padding=0,
            )
        )
        if event.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        await login_view(),
                    ],
                    bgcolor=ft.colors.SECONDARY,
                    padding=0,
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


if __name__ == "__main__":
    ft.app(main, assets_dir="assets/")
