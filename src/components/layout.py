"""Layout wrapper component for the application."""

from fasthtml.common import *
from monsterui.all import *

from components.sidebar import Sidebar


def PageLayout(title: str, *content, collapsed: bool = False) -> FT:
    """
    Wrap page content with the sidebar layout.
    
    Args:
        title: Page title
        *content: Page content components
        collapsed: Whether the sidebar is collapsed
    """
    return Title(title), Div(
        Sidebar(collapsed=collapsed),
        Div(
            Container(
                H1(title, cls="text-3xl font-bold mb-6"),
                *content,
                cls="py-8",
            ),
            cls="flex-1 overflow-auto",
        ),
        cls="flex h-screen bg-background",
    )
