import flet as ft


async def home_view(page: ft.Page):
    return ft.Row(
        expand=True,
        controls=[
            ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Welcome to core-seeder", color=ft.colors.BLUE_100, size=20
                    ),
                    ft.Text("Select a platform:", color=ft.colors.BLUE_200, size=15),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton(
                                content=ft.Text("Anime"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    color={"": ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.BLUE_900,
                                        "hovered": ft.colors.PRIMARY,
                                    },
                                    animation_duration=300,
                                ),
                                on_click=lambda _: page.go("/anime"),
                            ),
                            ft.FilledButton(
                                content=ft.Text("Manga"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    color={"": ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.BLUE_900,
                                        "hovered": ft.colors.PRIMARY,
                                    },
                                ),
                                on_click=lambda _: page.go("/manga"),
                            ),
                            ft.FilledButton(
                                content=ft.Text("Sound"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    color={"": ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.BLUE_900,
                                        "hovered": ft.colors.PRIMARY,
                                    },
                                ),
                                on_click=lambda _: page.go("/sound"),
                            ),
                        ],
                    ),
                ],
            )
        ],
    )
