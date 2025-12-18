"""Resume page routes."""

from fasthtml.common import *
from monsterui.all import *

from components.layout import PageLayout
from components.resume import AwardsSection, EducationSection, ExperienceSection, SkillsSection
from services.resume import get_awards, get_education, get_experience, get_skills

ar = APIRouter()


@ar
def about(sidebar_collapsed: str = None):
    """Display the resume page."""
    collapsed = sidebar_collapsed == "true"

    experience = get_experience()
    education = get_education()
    skills = get_skills()
    awards = get_awards()

    return PageLayout(
        "Resume",
        ExperienceSection(experience),
        EducationSection(education),
        SkillsSection(skills),
        AwardsSection(awards),
        collapsed=collapsed,
    )
