from typing import Type
from pyuicompose.render import RenderContext,render_content,ContentTypes
from .layout import Layout

class App:
  def __init__(self):
    self.context = None
    self.target = None
  
  def attach(self,target: Type[Layout]) -> None:
    self.target = target
  
  def render(self) -> None:
    render_content(
      ContentTypes.APP,
      self,
      None
    )