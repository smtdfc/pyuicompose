from typing import Type,TYPE_CHECKING,Any,Callable, Optional
from dataclasses import dataclass
from tkinter import *
from pyuicompose.render import RenderContext,BaseRenderer
from pyuicompose.declarations import  BaseDeclaration

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
