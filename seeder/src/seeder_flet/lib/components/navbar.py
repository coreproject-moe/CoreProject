import asyncio
import flet as ft


async def handle_logout(e: ft.ControlEvent, page: ft.Page):
    "Logout me!!!"
    ...
    page.go("/login")


async def navbar(page: ft.Page):
    return ft.Container(
        padding=10,
        height=55,
        border=ft.border.all(0.75, ft.colors.with_opacity(1, ft.colors.PRIMARY)),
        content=ft.Stack(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Image(src="/icons/core_icon.svg", width=25),
                            ]
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("Logout"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                                color=ft.colors.WHITE,
                                bgcolor=ft.colors.PRIMARY,
                                padding=ft.padding.symmetric(horizontal=20),
                                animation_duration=300,
                            ),
                            on_click=lambda e: asyncio.run(handle_logout(e, page)),
                        ),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="/icons/coreseeder_text.svg", height=18
                            ),
                            margin=ft.margin.only(top=7),
                        ),
                    ],
                ),
            ],
        ),
    )
