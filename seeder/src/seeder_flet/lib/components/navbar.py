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
        border=ft.border.all(1, ft.colors.with_opacity(0.5, ft.colors.PRIMARY)),
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
                        ft.FilledButton(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.icons.LOGOUT, size=15),
                                    ft.Text("Logout"),
                                ],
                                width=75,
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                                color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                bgcolor={
                                    "": ft.colors.with_opacity(0.25, ft.colors.PRIMARY)
                                },
                                side=ft.BorderSide(1, ft.colors.PRIMARY),
                                padding=ft.padding.symmetric(horizontal=15),
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
