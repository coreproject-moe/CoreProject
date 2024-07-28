import flet as ft


async def home_view(page: ft.Page):
    return ft.Row(
        controls=[
            ft.Text("Home", color=ft.colors.BLUE_100),
            ft.TextButton("Anime", on_click=lambda _: page.go("/anime")),
            ft.TextButton("Manga", on_click=lambda _: page.go("/manga")),
            ft.TextButton("Sound", on_click=lambda _: page.go("/sound")),
        ]
    )
