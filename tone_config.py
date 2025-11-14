"""Pastel tone configuration with emoji and visual formatting."""

EMOTION_EMOJI = {
    "지침": "○",
    "회피": "●",
    "성취": "◆",
    "기대": "▲",
    "불안": "▼",
    "고요": "★",
}


def get_emotion_emoji(emotion: str) -> str:
    """Return emoji for emotion type (minimal)."""
    return EMOTION_EMOJI.get(emotion, "■")


def get_intensity_bar(intensity: int) -> str:
    """Return visual intensity bar (1-5)."""
    filled = "●" * intensity
    empty = "○" * (5 - intensity)
    return f"{filled}{empty}"


def pastel_format_card(title: str, emoji: str, content: str) -> str:
    """Format a pastel-styled card message."""
    return f"{emoji} **{title}**\n\n{content}"
