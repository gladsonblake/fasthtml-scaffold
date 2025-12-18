"""Personal page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.layout import PageLayout
from components.personal import PersonalPageContent
from services.personal import get_personal_section

ar = APIRouter()


@ar
def profile(sidebar_collapsed: str = None):
    """Display the personal page with family info and theme picker."""
    collapsed = sidebar_collapsed == "true"
    personal_data = get_personal_section()

    return PageLayout(
        "Personal",
        Grid(
            PersonalPageContent(personal_data),
            Card(
                DivCentered(
                    DivHStacked(
                        UkIcon("palette", height=24),
                        H2("Personalize this Page", cls="text-2xl font-bold text-center"),
                    )
                ),
                P(
                    "Customize the look and feel of the application. These settings are automatically saved.",
                    cls=TextPresets.muted_sm + " mb-4",
                ),
                ThemePicker(
                    color=True,
                    radii=True,
                    shadows=True,
                    font=True,
                    mode=True,
                    cls="",
                ),
                cls=CardT.default,
            ),
            cols_sm=1,
            cols_md=1,
            cols_lg=2,
        ),
        collapsed=collapsed,
    )
