"""Layout wrapper component for the application."""

from fasthtml.common import *
from monsterui.all import *

from components.sidebar import MobileNav, Sidebar


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
            # Mobile header with hamburger menu
            Div(
                MobileNav(),
                cls="p-2 border-b border-border md:hidden sticky top-0 bg-background z-50",
            ),
            Container(
                H1(title, cls="text-3xl font-bold mb-6"),
                *content,
                cls="py-8",
            ),
            cls="flex-1 overflow-auto",
        ),
        cls="flex h-screen bg-background",
    )
