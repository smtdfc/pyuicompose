#from .version import *
from .declarations import *
from .list_renderer import *
from .render import RenderContext

def render(layout,renderer):
  
  context = RenderContext(
    renderer.value.WINDOW(
      
    ),
    renderer.value,
    None,
    {
      "type":"root"
    }
  )
  
  layout.render(context)
  
  context.root.element.mainloop()
  