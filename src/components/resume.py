"""Resume components for displaying experience, skills, and awards."""

from fasthtml.common import *
from monsterui.all import *


def ExperienceCard(experience: dict) -> FT:
    """Display an experience entry with company, position, dates, and details.

    Args:
        experience: Dictionary with company, position, start_date, end_date, and details.
    """
    return Card(
        Div(
            DivFullySpaced(
                Div(
                    H3(experience["position"], cls="font-semibold text-lg"),
                    P(experience["company"], cls=TextPresets.muted_sm),
                ),
                DivHStacked(
                    UkIcon("calendar", height=14),
                    P(
                        f"{experience['start_date']} - {experience['end_date']}",
                        cls=TextPresets.muted_sm,
                    ),
                ),
                cls="w-full items-start",
            ),
            Ul(
                *[Li(detail) for detail in experience.get("details", [])],
                cls="list-disc ml-6 mt-4 space-y-1 text-sm",
            ),
        ),
        cls=CardT.default,
    )


def ExperienceSection(experiences: list[dict]) -> FT:
    """Display all experience entries.

    Args:
        experiences: List of experience dictionaries.
    """
    return Div(
        DivHStacked(
            UkIcon("briefcase", height=24),
            H2("Experience", cls="text-2xl font-bold"),
        ),
        Div(
            *[ExperienceCard(exp) for exp in experiences],
            cls="space-y-4 mt-4",
        ),
        cls="mb-8",
    )


def EducationCard(education: dict) -> FT:
    """Display an education entry with school, major, dates, and details.

    Args:
        education: Dictionary with school, major, start_date, end_date, and details.
    """
    return Card(
        Div(
            DivFullySpaced(
                Div(
                    H3(education["major"], cls="font-semibold text-lg"),
                    P(education["school"], cls=TextPresets.muted_sm),
                ),
                DivHStacked(
                    UkIcon("calendar", height=14),
                    P(
                        f"{education['start_date']} - {education['end_date']}",
                        cls=TextPresets.muted_sm,
                    ),
                ),
                cls="w-full items-start",
            ),
            Ul(
                *[Li(detail) for detail in education.get("details", [])],
                cls="list-disc ml-6 mt-4 space-y-1 text-sm",
            )
            if education.get("details")
            else None,
        ),
        cls=CardT.default,
    )


def EducationSection(education_list: list[dict]) -> FT:
    """Display all education entries.

    Args:
        education_list: List of education dictionaries.
    """
    return Div(
        DivHStacked(
            UkIcon("graduation-cap", height=24),
            H2("Education", cls="text-2xl font-bold"),
        ),
        Div(
            *[EducationCard(edu) for edu in education_list],
            cls="space-y-4 mt-4",
        ),
        cls="mb-8",
    )


def SkillBadge(skill: dict) -> FT:
    """Display a single skill as a badge.

    Args:
        skill: Dictionary with name and category.
    """
    return Span(
        skill["name"],
        cls="px-3 py-1 rounded-full bg-primary/10 text-primary text-sm",
    )


def SkillsSection(skills: list[dict]) -> FT:
    """Display skills grouped by category.

    Args:
        skills: List of skill dictionaries with name and category.
    """
    # Group skills by category
    categories: dict[str, list[dict]] = {}
    for skill in skills:
        category = skill.get("category", "Other")
        if category not in categories:
            categories[category] = []
        categories[category].append(skill)

    return Div(
        DivHStacked(
            UkIcon("code", height=24),
            H2("Skills", cls="text-2xl font-bold"),
        ),
        Div(
            Card(
                Div(
                    *[
                        Div(
                            H4(category, cls="font-semibold mb-2"),
                            Div(
                                *[SkillBadge(skill) for skill in category_skills],
                                cls="flex flex-wrap gap-2",
                            ),
                            cls="mb-4 last:mb-0",
                        )
                        for category, category_skills in categories.items()
                    ],
                ),
                cls=CardT.default,
            ),
            cls="mt-4",
        ),
        cls="mb-8",
    )


def AwardCard(award: dict) -> FT:
    """Display a single award.

    Args:
        award: Dictionary with title, issuer, date, and description.
    """
    return Div(
        DivHStacked(
            UkIcon("trophy", height=20, cls="text-yellow-500 flex-shrink-0 mt-1"),
            Div(
                DivFullySpaced(
                    H4(award["title"], cls="font-semibold"),
                    P(award["date"], cls=TextPresets.muted_sm),
                    cls="w-full gap-4",
                ),
                P(award["issuer"], cls=TextPresets.muted_sm),
                P(award.get("description", ""), cls="text-sm mt-1") if award.get("description") else None,
                cls="flex-1",
            ),
            cls="items-start gap-3",
        ),
        cls="py-2",
    )


def AwardsSection(awards: list[dict]) -> FT:
    """Display all awards.

    Args:
        awards: List of award dictionaries.
    """
    return Div(
        DivHStacked(
            UkIcon("award", height=24),
            H2("Awards", cls="text-2xl font-bold"),
        ),
        Div(
            Card(
                Div(
                    *[AwardCard(award) for award in awards],
                    cls="divide-y divide-border",
                ),
                cls=CardT.default,
            ),
            cls="mt-4",
        ),
        cls="mb-8",
    )
