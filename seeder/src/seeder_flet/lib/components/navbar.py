import asyncio
import flet as ft

async def handle_logout(e: ft.ControlEvent, page: ft.Page):
    "Logout me!!!"
    ...
    page.go("/login")

async def navbar(page: ft.Page):
    return ft.Container(
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(src="/icons/core_icon.svg", width=40, height=40),
                        ft.Image(src="/icons/coreproject_text.svg", height=20),
                    ]
                ),
                ft.FilledButton(
                    content=ft.Text("Logout"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        color={"": ft.colors.WHITE},
                        bgcolor={
                            "": ft.colors.with_opacity(0.25, ft.colors.ERROR),
                            "hovered": ft.colors.with_opacity(0.5, ft.colors.ERROR),
                        },
                        animation_duration=300,
                    ),
                    on_click=lambda e: asyncio.run(handle_logout(e, page))
                ),
            ],
        ),
    )
