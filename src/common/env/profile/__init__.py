from .BaseProfileConfig import BaseProfileConfig
from .DevProfileConfig import DevProfileConfig
from .ProdProfileConfig import ProdProfileConfig
from .TestProfileConfig import TestProfileConfig
from typing import Type

PROFILE_CLASS_MAP: dict[str, Type[BaseProfileConfig]] = {
    "dev": DevProfileConfig,
    "prod": ProdProfileConfig,
    "test": TestProfileConfig
}