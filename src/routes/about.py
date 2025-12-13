"""About page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.layout import PageLayout


ar = APIRouter()


@ar
def about(sidebar_collapsed: str = None):
    """Display the about page."""
    collapsed = sidebar_collapsed == "true"

    return PageLayout(
        "About",
        Card(
            H2("FastHTML + MonsterUI Demo"),
            P(
                "This application demonstrates the power of building modern web interfaces "
                "using FastHTML and MonsterUI. It showcases a collapsible navigation sidebar, "
                "theme customization, and responsive design patterns.",
                cls="mb-4",
            ),
            P(
                "FastHTML allows you to build web applications entirely in Python, "
                "leveraging HTMX for dynamic interactions without writing JavaScript.",
                cls="mb-4",
            ),
            P(
                "MonsterUI provides a comprehensive set of pre-styled components built "
                "on Tailwind CSS and Franken UI, making it easy to create beautiful interfaces.",
            ),
            cls=CardT.default,
        ),
        Card(
            H3("Features", cls="mb-4"),
            Ul(
                Li(
                    DivLAligned(
                        UkIcon("panel-left", height=16),
                        Span("Collapsible sidebar navigation", cls="ml-2"),
                    ),
                    cls="mb-2",
                ),
                Li(
                    DivLAligned(
                        UkIcon("palette", height=16),
                        Span("Theme customization with ThemePicker", cls="ml-2"),
                    ),
                    cls="mb-2",
                ),
                Li(
                    DivLAligned(
                        UkIcon("database", height=16),
                        Span("LocalStorage persistence for preferences", cls="ml-2"),
                    ),
                    cls="mb-2",
                ),
                Li(
                    DivLAligned(
                        UkIcon("layout", height=16),
                        Span("Responsive layout components", cls="ml-2"),
                    ),
                    cls="mb-2",
                ),
            ),
            cls=(CardT.default, "mt-4"),
        ),
        collapsed=collapsed,
    )
