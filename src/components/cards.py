"""Card components for the application."""

from fasthtml.common import *
from monsterui.all import *


def InfoCard(title: str, content: str, icon: str = "info") -> FT:
    """Display an info card with an icon."""
    return Card(
        DivHStacked(UkIcon(icon, height=24), Div(H3(title), P(content, cls=TextPresets.muted_sm))), cls=CardT.hover
    )
