import os
from pyloid import Bridge, PyloidAPI, get_production_path


class URL(PyloidAPI):
    @Bridge(result=str)
    def get_production_path(self):
        production_path = get_production_path()

        if production_path is None:
            # not production env
            return None
        return str(os.path.join(production_path, "dist-front"))
