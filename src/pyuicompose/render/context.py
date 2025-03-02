from __future__ import annotations 
from typing import TYPE_CHECKING,Any,Type


class RenderContext:
  def __init__(self,root:Any=None,renderer:Type[BaseRenderer]=None, parent:RenderContext=None,data:dict={}):
    self.root = root
    self.parent = parent
    if not renderer and parent:
      self.renderer = parent.renderer
    else:
      self.renderer = renderer