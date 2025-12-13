"""Profile page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.layout import PageLayout

ar = APIRouter()


# Fake user data
FAKE_USER = {
    "name": "Blake Gladson",
    "email": "gladsonblake@gmail.com",
    "bio": "Solutions for the oil and gas industry",
    "role": "Solutions Analyst",
    "location": "Midland, TX",
}


def UserProfileCard() -> FT:
    """Display user profile information with fake data."""
    return Card(
        DivVStacked(
            UkIcon("user", height=50),
            H2(FAKE_USER["name"], cls="mt-4"),
            P(FAKE_USER["role"], cls=TextPresets.muted_sm),
            cls="items-center mb-6",
        ),
        Div(
            DivLAligned(
                UkIcon("mail", height=16),
                Span(FAKE_USER["email"], cls="ml-2"),
                cls="mb-3",
            ),
            DivLAligned(
                UkIcon("map-pin", height=16),
                Span(FAKE_USER["location"], cls="ml-2"),
                cls="mb-3",
            ),
            P(FAKE_USER["bio"], cls="text-sm mt-4"),
        ),
        cls=CardT.default,
    )


@ar
def profile(sidebar_collapsed: str = None):
    """Display the profile page with theme picker."""
    collapsed = sidebar_collapsed == "true"

    return PageLayout(
        "Profile",
        Grid(
            UserProfileCard(),
            Card(
                H2("Appearance", cls="mb-4"),
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
