from typing import Type,TYPE_CHECKING,Any
from tkinter import *
from pyuicompose.render import RenderContext,BaseRenderer
from pyuicompose.declarations import  BaseDeclaration


class TkinterTextRenderer:
  def __init__(self,declaration:Type[BaseDeclaration]=None,context:RenderContext=None):
    self.element = Label(
      context.root.element,
      text=declaration.props.get("text","No text")
    )
    
    context.root.add_child(self.element)
