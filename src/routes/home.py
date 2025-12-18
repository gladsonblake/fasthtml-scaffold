"""Home page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.home import HomePageContent
from components.layout import PageLayout
from services.home import get_home_section

ar = APIRouter()


@ar
def home(sidebar_collapsed: str = None):
    """Display the home page."""
    home_data = get_home_section()
    collapsed = sidebar_collapsed == "true"

    return PageLayout(
        "Introduction",
        HomePageContent(home_data=home_data),
        collapsed=collapsed,
    )
