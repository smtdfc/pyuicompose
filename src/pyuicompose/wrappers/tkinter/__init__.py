from typing import Type,TYPE_CHECKING,Any
from tkinter import *
from pyuicompose.render import RenderContext,BaseRenderer
from pyuicompose.declarations import  BaseDeclaration
from .components import *

class TkinterWindowRenderer:
  def __init__(self,declaration:Type[BaseDeclaration]=None,context:RenderContext=None):
    self.element = Tk()
    self.context = RenderContext(
      self,
      context.renderer,
      context,
      {
        "type":"window"
      }
    )
    
    for child in declaration.childs:
      child.render(self.context)
  
    context.root.add_child(self)

  def show(self) -> None:
    self.element.mainloop()
  
  def add_child(self,child:Any) -> None:
    child.pack()
 
class TkinterRenderer(BaseRenderer): 
    WINDOW = TkinterWindowRenderer
    LINEAR_LAYOUT = TkinterLinearLayoutRenderer
    TEXT=TkinterTextRenderer
    BUTTON=TkinterButtonRenderer