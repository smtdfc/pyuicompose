from enum import Enum
from typing import Type,TYPE_CHECKING
from .wrappers.tkinter import TkinterRenderer
from .render import BaseRenderer

class ListRenderer(Enum):
    TKINTER_RENDERER = TkinterRenderer 

def get_renderer_instance(name: ListRenderer) -> Type[BaseRenderer]:
    return name.value()  
