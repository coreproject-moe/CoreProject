import flet as ft

from seeder_flet.lib.views.login import login_view


async def main(page: ft.Page):
    page.title = "Flet counter example"

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
                [
                    await login_view(),
                ],
                bgcolor=ft.colors.SECONDARY,
                padding=0,
            )
        )
        if event.route == "/home":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("Home", color=ft.colors.BLUE_100),
                        ft.TextButton("Login", on_click=lambda _: page.go("/")),
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
