from pyuicompose.declarations import BaseDeclaration
from pyuicompose.exceptions import ContextError
from .content_types import ContentTypes

def render_content(
  type_:ContentTypes=ContentTypes.APP,
  declaration:Declaration=None,
  context:RenderContext=None
 ) -> None:
   
   if not context:
     raise ContextError(
       "Cannot find context to render contents !"
     )
   
   