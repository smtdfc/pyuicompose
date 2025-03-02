from __future__ import annotations 
from typing import TYPE_CHECKING
from pyuicompose.exceptions import ContextError
from .content_types import ContentTypes

if TYPE_CHECKING:
  from pyuicompose.declarations import BaseDeclaration



def render_content(
  type_:ContentTypes=ContentTypes.APP,
  declaration:Declaration=None,
  context:RenderContext=None
 ) -> None:
   
   if not context:
     raise ContextError(
       "Cannot find context to render contents !"
     )
   
   