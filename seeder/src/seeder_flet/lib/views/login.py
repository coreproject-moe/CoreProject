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
        border_color=ft.colors.TERTIARY,
        focused_border_color=ft.colors.PRIMARY,
        border_radius=10,
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
        border_color=ft.colors.TERTIARY,
        focused_border_color=ft.colors.PRIMARY,
        border_radius=10,
        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
        hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.35, ft.colors.BLUE_100)),
    )
    backend_url_field = ft.TextField(
        label="Backend URL",
        hint_text="backend.coreproject.moe",
        width=400,
        height=50,
        border_color=ft.colors.TERTIARY,
        focused_border_color=ft.colors.PRIMARY,
        border_radius=10,
        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
        hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.35, ft.colors.BLUE_100)),
    )

    return ft.Row(
        expand=True,
        controls=[
            ft.Column(
                [
                    ft.Container(content=ft.Text("Login to Continue", color=ft.colors.BLUE_100, size=20), margin=ft.margin.only(bottom=20)),
                    username_or_email_field,
                    password_field,
                    backend_url_field,
                    ft.FilledButton(
                        content=ft.Text("Continue", size=18),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                            bgcolor=ft.colors.PRIMARY,
                        ),
                        on_click=lambda e: asyncio.run(
                            handle_login_click(
                                e,
                                username_or_email_field.value,
                                password_field.value,
                                backend_url_field.value,
                            )
                        ),
                        height=50,
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
    )
