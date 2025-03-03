from typing import Type
from pyuicompose.render import RenderContext,render_content,ContentTypes
from .base import BaseDeclaration

class Text(BaseDeclaration):
  def __init__(self,**kargs):
    self.props = kargs
  
  def render(self,context:RenderContext) -> None:
    
    render_content(
      ContentTypes.TEXT,
      self,
      context
    )