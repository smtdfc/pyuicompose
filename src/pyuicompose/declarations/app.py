from typing import *
from pyuicompose.render import RenderContext,render_content,ContentTypes

class App:
  def __init__(self):
    self.context = None
    self.target = None
  
  def attach(self,target: Layout):
    self.target = target
  
  def render(self).-> None:
    render_content(
      ContentTypes.APP,
      self,
      None
    )