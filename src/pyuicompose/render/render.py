from __future__ import annotations 
from typing import TYPE_CHECKING
from pyuicompose.exceptions import ContextError
from .content_types import ContentTypes
from .context import RenderContext

if TYPE_CHECKING:
  from pyuicompose.declarations import BaseDeclaration

def render_content(
  type_:ContentTypes=ContentTypes.APP,
  declaration:Declaration=None,
  context:RenderContext=None
 ) -> None:
   
   renderer = context.renderer
   if type_ == ContentTypes.APP:
     renderer.WINDOW(declaration,context)
     
   if type_ == ContentTypes.LINEAR_LAYOUT:
      renderer.LINEAR_LAYOUT(declaration,context)
   
   if type_ == ContentTypes.TEXT:
      renderer.TEXT(declaration,context)