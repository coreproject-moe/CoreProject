import os
from pyloid import Pyloid, get_production_path, is_production
from .bridge import JSApi
from .functions import find_free_port

PORT = find_free_port()

app = Pyloid(app_name="Pyloid-App", single_instance=True)
production_path = get_production_path()


if is_production() and production_path:
    app.set_icon(os.path.join(production_path, "icons/icon.png"))
    app.set_tray_icon(os.path.join(production_path, "icons/icon.png"))
else:
    app.set_icon("src-pyloid/icons/icon.png")
    app.set_tray_icon("src-pyloid/icons/icon.png")


if is_production() and production_path:
    # production
    window = app.create_window(
        title="Pyloid Browser-production",
        js_apis=[JSApi()],
        dev_tools=True,
    )
    window.load_file(os.path.join(production_path, "dist-front/index.html"))
else:
    window = app.create_window(
        title="Pyloid Browser-dev",
        js_apis=[JSApi()],
        dev_tools=True,
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()
