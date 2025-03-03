from typing import Type
from pyuicompose.render import RenderContext,render_content,ContentTypes
from .layout import Layout

class LinearLayout(Layout):
  def __init__(self,*childs):
    
    super().__init__(*childs)
    
  def render(self,context) -> None:
    render_content(
      ContentTypes.LINEAR_LAYOUT,
      self,
      context
    )