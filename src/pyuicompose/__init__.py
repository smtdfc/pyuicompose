#from .version import *
from .declarations import *
from .list_renderer import *
from .render import RenderContext
from .app import AppRootElement

def render(layout,renderer):
  root = AppRootElement()
  context = RenderContext(
    root,
    renderer.value,
    None,
    {
      "type":"app"
    }
  )
  print(layout)
  layout.render(context)
  root.childs[0].show()