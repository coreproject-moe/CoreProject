import flet as ft


def get_staff_data():
    return [
        {
            "data": {
                "mal_id": 1,
                "url": "https:\/\/myanimelist.net\/people\/1\/Tomokazu_Seki",
                "website_url": None,
                "images": {
                    "jpg": {
                        "image_url": "https:\/\/cdn.myanimelist.net\/images\/voiceactors\/1\/55486.jpg"
                    }
                },
                "name": "Tomokazu Seki",
                "given_name": "\u667a\u4e00",
                "family_name": "\u95a2",
                "alternate_names": [
                    "Seki Mondoya",
                    "\u9580\u6238 \u958b",
                    "Monto Hiraku",
                ],
                "birthday": "1972-09-08T00:00:00+00:00",
                "favorites": 6188,
                "about": "Hometown: Tokyo, Japan\nBlood type: AB\n\nTwitter: @seki0908\nInstagram: @sekitomokazu\nProfile: Atomic Monkey",
            }
        },
        {
            "data": {
                "mal_id": 2,
                "url": "https:\/\/myanimelist.net\/people\/2\/Tomokazu_Sugita",
                "website_url": "https:\/\/agrs.co.jp\/",
                "images": {
                    "jpg": {
                        "image_url": "https:\/\/cdn.myanimelist.net\/images\/voiceactors\/1\/81054.jpg"
                    }
                },
                "name": "Tomokazu Sugita",
                "given_name": "\u667a\u548c",
                "family_name": "\u6749\u7530",
                "alternate_names": [],
                "birthday": "1980-10-11T00:00:00+00:00",
                "favorites": 47217,
                "about": "Hometown: Saitama, Japan\nBlood type: B\nHeight: 178 cm\nWeight: 57 kg\n\nTwitter: @sugitaLOV\nStaff Twitter: @AGRS_staff\nStaff Instagram: @agrs_staff\nYouTube: @agrs1011",
            }
        },
    ]


class StaffView(ft.Container):
    def __init__(self):
        super().__init__()

        self.content = self.create_datatable()

    def create_datatable(self):
        return ft.DataTable(
            show_checkbox_column=True,
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
                        ft.DataCell(ft.Text(item["data"]["name"])),
                        ft.DataCell(ft.Text(item["data"]["birthday"])),
                        ft.DataCell(ft.Text(item["data"]["favorites"])),
                    ]
                )
                for item in get_staff_data()
            ],
        )
