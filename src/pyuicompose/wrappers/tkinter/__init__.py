from typing import Type,TYPE_CHECKING,Any
from tkinter import *
from pyuicompose.render import RenderContext,BaseRenderer
from pyuicompose.declarations import  BaseDeclaration

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
 
class TkinterTextRenderer:
  def __init__(self,declaration:Type[BaseDeclaration]=None,context:RenderContext=None):
    self.element = Label(
      context.root.element,
      text=declaration.props.get("text","No text")
    )
    
    context.root.add_child(self.element)

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
    
    
    for child in declaration.childs:
      child.render(self.context)
    context.root.add_child(self.element)
    
  def add_child(self,child:Any) -> None:
    child.pack()
 
class TkinterRenderer(BaseRenderer): 
    WINDOW = TkinterWindowRenderer
    LINEAR_LAYOUT = TkinterLinearLayoutRenderer
    TEXT=TkinterTextRenderer