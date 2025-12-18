"""Home page components for displaying personal information."""

from fasthtml.common import *
from monsterui.all import *


def IdentitySection(name: str, headline: str, summary: str) -> FT:
    """Display identity section with name, headline, and summary."""
    return Div(
        H1(name, cls="text-4xl font-bold mb-2"),
        H2(headline, cls="text-2xl text-muted-foreground mb-2"),
        P(summary, cls="text-lg text-muted-foreground"),
        cls="mb-8",
    )


def HowIWorkSection(philosophy_summary: str, principles: list[dict]) -> FT:
    """Display how I work section with philosophy summary and principles."""
    return Card(
        H2("How I Work", cls="text-2xl font-bold mb-4 text-center"),
        P(philosophy_summary, cls="mb-4 text-center"),
        DivVStacked(
            *[
                Div(
                    H3(principle.get("title", ""), cls="text-lg font-semibold mb-1 text-center"),
                    P(principle.get("description", ""), cls="text-muted-foreground text-center"),
                )
                for principle in principles
                if principle.get("title") or principle.get("description")
            ],
            cls="space-y-4",
        ),
        cls=CardT.default,
    )


def CallsToActionSection(ctas: list[dict]) -> FT:
    """Display calls to action section with external link buttons."""

    def get_icon_for_cta(target: str, label: str) -> str:
        """Determine appropriate icon based on target URL or label."""
        target_lower = target.lower()
        label_lower = label.lower()

        if "linkedin" in target_lower or "linkedin" in label_lower:
            return "linkedin"
        elif "mailto:" in target_lower or "email" in label_lower:
            return "mail"
        else:
            return "external-link"

    return Div(
        H2("Connect", cls="text-2xl font-bold mb-4"),
        DivHStacked(
            *[
                A(
                    Button(
                        DivLAligned(
                            UkIcon(get_icon_for_cta(cta["target"], cta["label"]), height=18, cls="flex-shrink-0"),
                            Span(cta["label"]),
                            cls="gap-2",
                        ),
                        cls=ButtonT.primary,
                    ),
                    href=cta["target"],
                    target="_blank",
                    rel="noopener noreferrer",
                )
                for cta in ctas
                if cta.get("label") and cta.get("target")
            ],
            cls="flex-wrap gap-4",
        ),
        cls="mb-8",
    )


def ContactInfoSection(email: str = "", phone: str = "", location: str = "") -> FT:
    """Display contact information section with email, phone, and location."""
    contact_items = []

    if email:
        contact_items.append(
            DivLAligned(
                UkIcon("mail", height=20, cls="flex-shrink-0"),
                A(
                    P(email, cls="text-muted-foreground hover:text-foreground"),
                    href=f"mailto:{email}",
                ),
                cls="gap-2",
            )
        )

    if phone:
        contact_items.append(
            DivLAligned(
                UkIcon("phone", height=20, cls="flex-shrink-0"),
                A(
                    P(phone, cls="text-muted-foreground hover:text-foreground"),
                    href=f"tel:{phone}",
                ),
                cls="gap-2",
            )
        )

    if location:
        contact_items.append(
            DivLAligned(
                UkIcon("map-pin", height=20, cls="flex-shrink-0"),
                P(location, cls="text-muted-foreground"),
                cls="gap-2",
            )
        )

    if not contact_items:
        return Div()

    return Card(
        H2("Contact Information", cls="text-2xl font-bold mb-4 text-center"),
        DivVStacked(
            *contact_items,
            cls="space-y-3",
        ),
        cls=CardT.default,
    )


def HomePageContent(home_data: dict) -> FT:
    """Main component that assembles all home page sections."""
    identity = home_data.get("identity", {})
    how_i_work = home_data.get("how_i_work", {})
    calls_to_action = home_data.get("calls_to_action", [])
    contact_info = home_data.get("contact_info", {})

    return Div(
        IdentitySection(
            name=identity.get("name", ""),
            headline=identity.get("headline", ""),
            summary=identity.get("summary", ""),
        ),
        HowIWorkSection(
            philosophy_summary=how_i_work.get("philosophy_summary", ""),
            principles=how_i_work.get("principles", []),
        ),
        ContactInfoSection(
            email=contact_info.get("email", ""),
            phone=contact_info.get("phone", ""),
            location=contact_info.get("location", ""),
        ),
        CallsToActionSection(ctas=calls_to_action),
        cls="space-y-6",
    )
