from typing import Type,TYPE_CHECKING
from tkinter import *
from pyuicompose.render import RenderContext,BaseRenderer
from pyuicompose.declarations import  BaseDeclaration

class TkinterWindowRenderer:
  def __init__(self,declaration:Type[BaseDeclaration]=None,context:RenderContext=None):
    self.element = Tk()

class TkinterLinearLayoutRenderer:
  def __init__(self,declaration:Type[BaseDeclaration]=None ,context:RenderContext=None):
    self.element = Frame(
      context.root.element
    )
    
    self.context = RenderContext(
      self,
      context.renderer,
      context,
      {
        "type":"linear_layout"
      }
    )
    
    
class TkinterRenderer(BaseRenderer): 
    WINDOW = TkinterWindowRenderer
    LINEAR_LAYOUT = TkinterLinearLayoutRenderer