import nonebot
import os
from configs.config import Config


Config.add_plugin_config(
    "ishop",
    "IMPORT_ISHOP_GOODS",
    True,
    help_="私人商店",
    default_value=True
)

nonebot.load_plugins(os.path.join(os.path.dirname(__file__)))
