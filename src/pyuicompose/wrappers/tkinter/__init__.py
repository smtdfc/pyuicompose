from typing import TYPE_CHECKING
import pyuicompose.render as render  
from tkinter import *

class TkinterWindowRenderer:
  def __init__(self,declaration=None,context=None):
    self.element = Tk()

class TkinterLinearLayoutRenderer:
  def __init__(self,declaration ,context):
    self.element = Frame(
      context.root.element
    )
    
    self.context = render.RenderContext(
      self,
      context.renderer,
      context,
      {
        "type":"linear_layout"
      }
    )
    
    
class TkinterRenderer(render.BaseRenderer): 
    WINDOW = TkinterWindowRenderer
    LINEAR_LAYOUT = TkinterLinearLayoutRenderer