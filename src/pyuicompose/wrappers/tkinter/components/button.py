from typing import Type,TYPE_CHECKING,Any,Callable, Optional
from dataclasses import dataclass
from tkinter import *
from pyuicompose.render import RenderContext
from pyuicompose.declarations import BaseDeclaration

@dataclass
class TkinterButtonProps:
    text: str = "No text"
    onClick: Optional[Callable[[], None]] = None
    width: int = 10
    height: int = 2
    backgroundColor: str = "#f0f0f0"
    foregroundColor: str = "#000000"
    fontFamily: str = "Arial"
    fontSize: int = 12
    fontWeight: str = "normal"  # Options: "normal", "bold"
    borderWidth: int = 2
    borderType: str = "raised"  # Options: "flat", "raised", "sunken", "ridge", "solid", "groove"
    paddingX: int = 5
    paddingY: int = 5
    state: str = "normal"  # Options: "normal", "disabled", "active"
    textAlign: str = "center"  # Options: "n", "s", "e", "w", "center"
    cursorType: str = "hand2"  # Options: "arrow", "hand2", etc.
    activeBackgroundColor: str = "#d9d9d9"
    activeForegroundColor: str = "#000000"
    disabledForegroundColor: str = "#a3a3a3"
    underlineIndex: int = -1  # -1 means no underline
    textWrapLength: int = 0  # 0 means no wrapping
    focusable: bool = True
    repeatDelay: int = 500  # In milliseconds
    repeatInterval: int = 100  # In milliseconds


class TkinterButtonRenderer:
    def __init__(self, declaration: Type[BaseDeclaration] = None, context: RenderContext = None):
        self.element = Button(
            context.root.element,
            text=declaration.props.get("text", "No text"),
            command=declaration.props.get("onClick", lambda: None),
            width=declaration.props.get("width", 10),
            height=declaration.props.get("height", 2),
            bg=declaration.props.get("backgroundColor", "#f0f0f0"),
            fg=declaration.props.get("foregroundColor", "#000000"),
            font=(
                declaration.props.get("fontFamily", "Arial"),
                declaration.props.get("fontSize", 12),
                declaration.props.get("fontWeight", "normal"),
            ),
            borderwidth=declaration.props.get("borderWidth", 2),
            relief=declaration.props.get("borderType", "raised"),
            padx=declaration.props.get("paddingX", 5),
            pady=declaration.props.get("paddingY", 5),
            state=declaration.props.get("state", "normal"),
            anchor=declaration.props.get("textAlign", "center"),
            cursor=declaration.props.get("cursorType", "hand2"),
            activebackground=declaration.props.get("activeBackgroundColor", "#d9d9d9"),
            activeforeground=declaration.props.get("activeForegroundColor", "#000000"),
            disabledforeground=declaration.props.get("disabledForegroundColor", "#a3a3a3"),
            underline=declaration.props.get("underlineIndex", -1),
            wraplength=declaration.props.get("textWrapLength", 0),
            takefocus=declaration.props.get("focusable", 1),
            repeatdelay=declaration.props.get("repeatDelay", 500),
            repeatinterval=declaration.props.get("repeatInterval", 100)
        )

        
        context.root.add_child(self.element)