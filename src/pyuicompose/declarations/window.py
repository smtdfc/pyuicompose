from typing import Type
from pyuicompose.render import RenderContext,render_content,ContentTypes
from .base import BaseDeclaration
from .layout import Layout

class Window(BaseDeclaration):
  def __init__(self,*childs,**props):
    self.childs = childs
    self.target = None
    self.props = props
    
  def attach(self,target: Type[Layout]) -> None:
    self.target = target
  
  def render(self,context) -> None:
    render_content(
      ContentTypes.APP,
      self,
      context
    )