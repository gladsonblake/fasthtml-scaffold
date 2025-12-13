"""Collapsible sidebar navigation component."""

from fasthtml.common import *
from monsterui.all import *


def SidebarItem(icon: str, text: str, href: str, collapsed: bool = False) -> FT:
    """Create a sidebar navigation item with icon and text."""
    text_cls = "hidden" if collapsed else "ml-3 whitespace-nowrap"

    return Li(
        A(
            DivLAligned(
                UkIcon(icon, height=20, cls="flex-shrink-0"),
                Span(text, cls=text_cls),
            ),
            href=href,
            cls="flex items-center p-2 rounded-lg hover:bg-muted transition-colors",
        )
    )


def SidebarToggle(collapsed: bool = False) -> FT:
    """Create the sidebar toggle button using HTMX."""
    icon = "panel-left-open" if collapsed else "panel-left-close"

    return Button(
        UkIcon(icon, height=20),
        cls="p-2 rounded-lg hover:bg-muted transition-colors",
        hx_post="/toggle-sidebar",
        hx_target="#sidebar",
        hx_swap="outerHTML",
    )


def Sidebar(collapsed: bool = False) -> FT:
    """Create a collapsible sidebar navigation."""
    nav_items = [
        ("home", "Home", "/home"),
        ("info", "About", "/about"),
        ("user", "Profile", "/profile"),
    ]

    width_cls = "w-16" if collapsed else "w-48"
    header_text_cls = "hidden" if collapsed else "font-semibold text-lg"

    return Div(
        Div(
            # Header with toggle
            DivFullySpaced(
                Span("Menu", cls=header_text_cls),
                SidebarToggle(collapsed),
                cls="p-4 border-b border-border",
            ),
            # Navigation items
            DivVStacked(
                *[SidebarItem(*item, collapsed=collapsed) for item in nav_items],
                cls=(NavT.primary, "space-y-2 p-4 list-none"),
            ),
            cls="h-full flex flex-col",
        ),
        id="sidebar",
        cls=f"{width_cls} h-screen bg-background border-r border-border flex-shrink-0 overflow-hidden transition-all duration-300",
    )
