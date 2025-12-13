"""FastHTML + MonsterUI Application Entry Point."""

from fasthtml.common import *
from monsterui.all import *
from starlette.responses import HTMLResponse

from components.sidebar import Sidebar
from routes.about import ar as about_router
from routes.home import ar as home_router
from routes.profile import ar as profile_router

# Initialize app with MonsterUI theme
app, rt = fast_app(hdrs=Theme.green.headers())

# Register route modules
home_router.to_app(app)
about_router.to_app(app)
profile_router.to_app(app)


@rt
def index():
    """Root route redirects to home."""
    return RedirectResponse("/home")


@rt("/toggle-sidebar", methods=["POST"])
def toggle_sidebar(sidebar_collapsed: str = None):
    """Toggle the sidebar collapsed state and return updated sidebar."""
    # Read current state from cookie (default to expanded)
    is_collapsed = sidebar_collapsed == "true"

    # Toggle the state
    new_collapsed = not is_collapsed

    # Create the sidebar HTML
    sidebar_html = to_xml(Sidebar(collapsed=new_collapsed))

    # Return response with cookie
    response = HTMLResponse(content=sidebar_html)
    response.set_cookie(
        key="sidebar_collapsed",
        value="true" if new_collapsed else "false",
        path="/",
        samesite="lax",
    )
    return response


serve()
