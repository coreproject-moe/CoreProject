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
                    ft.Text("Select a platform:", color=ft.colors.BLUE_200, size=15),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton(
                                content=ft.Text("Anime"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.with_opacity(
                                            0.25, ft.colors.PRIMARY
                                        )
                                    },
                                    side=ft.BorderSide(1, ft.colors.PRIMARY),
                                    padding=ft.padding.symmetric(horizontal=15),
                                ),
                                on_click=lambda _: page.go("/anime"),
                            ),
                            ft.FilledButton(
                                content=ft.Text("Manga"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.with_opacity(
                                            0.25, ft.colors.PRIMARY
                                        )
                                    },
                                    side=ft.BorderSide(1, ft.colors.PRIMARY),
                                    padding=ft.padding.symmetric(horizontal=15),
                                ),
                                on_click=lambda _: page.go("/manga"),
                            ),
                            ft.FilledButton(
                                content=ft.Text("Sound"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                    bgcolor={
                                        "": ft.colors.with_opacity(
                                            0.25, ft.colors.PRIMARY
                                        )
                                    },
                                    side=ft.BorderSide(1, ft.colors.PRIMARY),
                                    padding=ft.padding.symmetric(horizontal=15),
                                ),
                                on_click=lambda _: page.go("/sound"),
                            ),
                        ],
                    ),
                ],
            )
        ],
    )
