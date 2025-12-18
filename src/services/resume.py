"""Resume service for loading and parsing resume data."""

import json
from pathlib import Path


def load_resume() -> dict:
    """Load resume data from JSON file.

    Returns:
        Dictionary containing experience, skills, and awards data.
    """
    data_path = Path(__file__).parent.parent / "data" / "resume.json"
    with open(data_path, "r") as f:
        return json.load(f)


def get_experience() -> list[dict]:
    """Get experience entries from resume data."""
    return load_resume().get("experience", [])


def get_skills() -> list[dict]:
    """Get skills from resume data."""
    return load_resume().get("skills", [])


def get_awards() -> list[dict]:
    """Get awards from resume data."""
    return load_resume().get("awards", [])


def get_education() -> list[dict]:
    """Get education entries from resume data."""
    return load_resume().get("education", [])
