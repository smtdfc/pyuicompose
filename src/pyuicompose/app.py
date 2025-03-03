from typing import Any

class AppRootElement:
  def __init__(self):
    self.childs = []
    self.element = None
    
  def add_child(self,child:Any) -> None:
    self.childs.append(child)