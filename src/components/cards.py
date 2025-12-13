"""Card components for the application."""

from fasthtml.common import *
from monsterui.all import *


def WelcomeCard(title: str, message: str) -> FT:
    """Display a welcome card with title and message."""
    return Card(
        H2(title), P(message), footer=DivRAligned(Button("Get Started", cls=ButtonT.primary)), cls=CardT.default
    )


def InfoCard(title: str, content: str, icon: str = "info") -> FT:
    """Display an info card with an icon."""
    return Card(
        DivHStacked(UkIcon(icon, height=24), Div(H3(title), P(content, cls=TextPresets.muted_sm))), cls=CardT.hover
    )
