"""Example service demonstrating business logic separation."""


def get_welcome_message() -> str:
    """Generate a welcome message for the home page."""
    return (
        "This project uses FastHTML with MonsterUI for building "
        "server-rendered web applications with Python. "
        "Components are styled using Tailwind CSS and DaisyUI."
    )


def process_data(data: dict) -> dict:
    """Example data processing function.
    
    Args:
        data: Raw input data to process.
        
    Returns:
        Processed data ready for use in components.
    """
    # Business logic goes here
    return data

