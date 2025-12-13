# FastHTML + MonsterUI Application

A server-rendered web application built with FastHTML and MonsterUI.

## Project Structure

```
fasthtml_components/
├── main.py           # Application entry point
├── routes/           # Route handlers (HTTP endpoints)
├── components/       # Reusable UI components
├── services/         # Business logic layer
└── .cursor/rules/    # Development guidelines
```

## Setup

1. Install dependencies with uv:
```bash
uv sync
```

2. Run the development server:
```bash
uv run python main.py
```

3. Open http://localhost:5001 in your browser

## Development Guidelines

- **Routes**: HTTP handlers in `routes/` - keep them thin, delegate to services
- **Components**: Reusable UI in `components/` - return FT objects
- **Services**: Business logic in `services/` - database, APIs, processing
- **Styling**: Use Tailwind/DaisyUI via `cls` parameter - no vanilla CSS

See `.cursor/rules/fasthtml-monsterui.mdc` for detailed conventions.

