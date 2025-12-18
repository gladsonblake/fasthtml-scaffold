"""Personal page components for displaying family and personal information."""

from fasthtml.common import *
from monsterui.all import *


def PersonalPageContent(personal_data: dict) -> FT:
    """Main component that displays personal information section.

    Args:
        personal_data: Dictionary containing personal page data with title and content.
    """
    title = personal_data.get("title", "Personal")
    content = personal_data.get("content", "")

    return Card(
        DivVStacked(
            DivHStacked(
                UkIcon("users", height=24),
                H2(title, cls="text-2xl font-bold"),
            ),
            P(content, cls="text-sm mt-4 whitespace-pre-line") if content else None,
            cls="space-y-4",
        ),
        cls=CardT.default,
    )
