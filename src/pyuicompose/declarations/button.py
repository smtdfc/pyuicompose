from typing import Type
from pyuicompose.render import RenderContext,render_content,ContentTypes
from .base import BaseDeclaration

class Button(BaseDeclaration):
  def __init__(self,**kargs):
    self.props = kargs


  def render(self,context:RenderContext) -> None:
    
    render_content(
      ContentTypes.BUTTON,
      self,
      context
    )