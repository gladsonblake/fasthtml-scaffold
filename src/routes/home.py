"""Home page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.cards import WelcomeCard
from components.layout import PageLayout
from services.example import get_welcome_message


ar = APIRouter()


@ar
def home(sidebar_collapsed: str = None):
    """Display the home page."""
    message = get_welcome_message()
    collapsed = sidebar_collapsed == "true"

    return PageLayout(
        "Home",
        WelcomeCard(title="FastHTML + MonsterUI", message=message),
        collapsed=collapsed,
    )
