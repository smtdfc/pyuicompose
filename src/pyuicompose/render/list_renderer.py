from enum import Enum
from typing import Type
from pyuicompose.wrappers.tkinter import TkinterRenderer
from .Renderer import BaseRenderer

class ListRenderer(Enum):
    TKINTER_RENDERER = TkinterRenderer 

def get_renderer_instance(name: ListRenderer) -> Type[BaseRenderer]:
    return name.value()  
