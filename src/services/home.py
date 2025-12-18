"""Home service for loading and parsing home page data."""

import json
from pathlib import Path


def load_home_data() -> dict:
    """Load home page data from JSON file.

    Returns:
        Dictionary containing home page personal information.
    """
    data_path = Path(__file__).parent.parent / "data" / "home.json"
    with open(data_path, "r") as f:
        return json.load(f)


def get_home_section() -> dict:
    """Get the home section from home data."""
    return load_home_data().get("introduction", {})
