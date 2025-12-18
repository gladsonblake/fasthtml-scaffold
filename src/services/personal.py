"""Personal service for loading and parsing personal page data."""

import json
from pathlib import Path


def load_personal_data() -> dict:
    """Load personal page data from JSON file.

    Returns:
        Dictionary containing personal page information.
    """
    data_path = Path(__file__).parent.parent / "data" / "personal.json"
    with open(data_path, "r") as f:
        return json.load(f)


def get_personal_section() -> dict:
    """Get the personal section from personal data."""
    return load_personal_data().get("personal", {})
