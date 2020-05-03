from os.path import dirname

from turklirasi_bot.utils.loader import get_modules

ALL_MODULES = get_modules(dirname(__file__))
# __all__ = ALL_MODULES + ["ALL_MODULES"]
