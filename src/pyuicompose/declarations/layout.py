from .base import BaseDeclaration

class Layout(BaseDeclaration):
  def __init__(self,*childs):
    self.childs = childs