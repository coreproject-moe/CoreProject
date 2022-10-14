from fastapi.templating import Jinja2Templates

from settings import TEMPLATE_DIR

templates = Jinja2Templates(directory=TEMPLATE_DIR)
