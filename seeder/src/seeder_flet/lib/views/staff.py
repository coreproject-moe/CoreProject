from datetime import datetime
import flet as ft

from shinobi.builder.staff import StaffBuilder

from ...models._models import Staff


def get_staff_data():
    return [
        {
            "data": {
                "mal_id": 1,
                "url": "https://myanimelist.net/people/1/Tomokazu_Seki",
                "website_url": None,
                "images": {
                    "jpg": {
                        "image_url": "https://cdn.myanimelist.net/images/voiceactors/1/55486.jpg"
                    }
                },
                "name": "Tomokazu Seki",
                "given_name": "智一",
                "family_name": "関",
                "alternate_names": ["Seki Mondoya", "門戸 開", "Monto Hiraku"],
                "birthday": "1972-09-08T00:00:00+00:00",
                "favorites": 6188,
                "about": "Hometown: Tokyo, Japan\nBlood type: AB\n\nTwitter: @seki0908\nInstagram: @sekitomokazu\nProfile: Atomic Monkey",
            }
        },
        {
            "data": {
                "mal_id": 2,
                "url": "https://myanimelist.net/people/2/Tomokazu_Sugita",
                "website_url": "https://agrs.co.jp/",
                "images": {
                    "jpg": {
                        "image_url": "https://cdn.myanimelist.net/images/voiceactors/1/81054.jpg"
                    }
                },
                "name": "Tomokazu Sugita",
                "given_name": "智和",
                "family_name": "杉田",
                "alternate_names": [],
                "birthday": "1980-10-11T00:00:00+00:00",
                "favorites": 47217,
                "about": "Hometown: Saitama, Japan\nBlood type: B\nHeight: 178 cm\nWeight: 57 kg\n\nTwitter: @sugitaLOV\nStaff Twitter: @AGRS_staff\nStaff Instagram: @agrs_staff\nYouTube: @agrs1011",
            }
        },
    ]


class StaffView(ft.Container):
    def __init__(self, session):
        super().__init__()

        self.session = session
        self.render()

    def did_mount(self):
        self.page.run_task(self.fetch_all_people)

    def will_unmount(self):
        pass

    async def fetch_all_people(self):
        builder = StaffBuilder()
        dictionary = builder.build_dictionary(sort=True)

        async with self.session() as _session:
            for i in dictionary:
                db_obs = Staff(mal_id=i)
                _session.add(db_obs)
            await _session.commit()

    def render(self):
        self.content = ft.DataTable(
            # events
            on_select_all=lambda e: print(e.data),
            # properties
            show_checkbox_column=True,
            border=ft.border.all(1, ft.colors.PRIMARY),
            vertical_lines=ft.BorderSide(1, ft.colors.with_opacity(0.5, ft.colors.PRIMARY)),
            horizontal_lines=ft.BorderSide(
                1, ft.colors.with_opacity(0.5, ft.colors.PRIMARY)
            ),
            heading_row_color=ft.colors.with_opacity(0.10, ft.colors.PRIMARY),
            data_row_color=ft.colors.with_opacity(0, ft.colors.PRIMARY),
            columns=[
                ft.DataColumn(ft.Text("mal_id")),
                ft.DataColumn(ft.Text("Staff")),
                ft.DataColumn(ft.Text("Birthday")),
                ft.DataColumn(ft.Text("Favorites")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item["data"]["mal_id"])),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.Image(
                                        src=item["data"]["images"]["jpg"]["image_url"],
                                    ),
                                    ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            ft.Text(item["data"]["name"]),
                                            ft.Text(
                                                ", ".join(item["data"]["alternate_names"]),
                                                color=ft.colors.with_opacity(
                                                    0.5, ft.colors.WHITE
                                                ),
                                            ),
                                        ],
                                    ),
                                ]
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                datetime.fromisoformat(item["data"]["birthday"]).strftime(
                                    "%b %d, %Y"
                                )
                            )
                        ),
                        ft.DataCell(ft.Text("{:,}".format(item["data"]["favorites"]))),
                    ],
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                )
                for item in get_staff_data()
            ],
        )
