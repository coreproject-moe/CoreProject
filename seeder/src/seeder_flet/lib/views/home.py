import flet as ft


async def home_view(page: ft.Page):
    return ft.Row(
        controls=[
            ft.Text("Home", color=ft.colors.BLUE_100),
            ft.TextButton("Login", on_click=lambda _: page.go("/")),
        ]
    )
