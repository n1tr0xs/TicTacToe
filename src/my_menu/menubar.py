from .widget import Widget
from .actions import *
from ._types import *


class MenuBar(Widget):
    def __init__(
        self,
        title: str = '',
    ):
        super().__init__(title)

    def render(self):
        return self.render_string()
