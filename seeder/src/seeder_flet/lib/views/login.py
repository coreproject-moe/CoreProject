import asyncio
import flet as ft


__all__ = ["login_view"]


async def handle_login_click(
    e: ft.ControlEvent, username: str, password: str, backend: str
):
    "Try to login with backend"
    ...


async def login_view():
    username_or_email_field = ft.TextField(
        autofocus=True,
        label="Username/Email address",
        width=400,
        height=50,
        hint_text="enter email address or username",
        bgcolor=ft.colors.TRANSPARENT,
        hover_color=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
        focused_bgcolor=ft.colors.with_opacity(0.25, ft.colors.PRIMARY),
        border_color=ft.colors.with_opacity(0.5, ft.colors.PRIMARY),
        focused_border_color=ft.colors.PRIMARY,
        border_radius=0,
        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
        hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.35, ft.colors.BLUE_100)),
    )
    password_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        hint_text="password#0000",
        width=400,
        height=50,
        bgcolor=ft.colors.TRANSPARENT,
        hover_color=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
        focused_bgcolor=ft.colors.with_opacity(0.25, ft.colors.PRIMARY),
        border_color=ft.colors.with_opacity(0.5, ft.colors.PRIMARY),
        focused_border_color=ft.colors.PRIMARY,
        border_radius=0,
        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
        hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.35, ft.colors.BLUE_100)),
    )
    backend_url_field = ft.TextField(
        label="Backend URL",
        hint_text="backend.coreproject.moe",
        width=400,
        height=50,
        bgcolor=ft.colors.TRANSPARENT,
        hover_color=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
        focused_bgcolor=ft.colors.with_opacity(0.25, ft.colors.PRIMARY),
        border_color=ft.colors.with_opacity(0.5, ft.colors.PRIMARY),
        focused_border_color=ft.colors.PRIMARY,
        border_radius=0,
        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
        hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.35, ft.colors.BLUE_100)),
    )

    return ft.Row(
        expand=True,
        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src="/icons/coreseeder_text.svg", height=20),
                        margin=ft.margin.only(bottom=40),
                    ),
                    username_or_email_field,
                    password_field,
                    backend_url_field,
                    ft.FilledButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(name=ft.icons.LOGIN, size=20),
                                ft.Text("Login", size=15),
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
                        ),
                        on_click=lambda e: asyncio.run(
                            handle_login_click(
                                e,
                                username_or_email_field.value,
                                password_field.value,
                                backend_url_field.value,
                            )
                        ),
                        height=40,
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
    )
