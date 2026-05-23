"""Generate UG mathematics tutorial sheets from a syllabus."""

from __future__ import annotations

SYSTEM_PROMPT = (
    "You are an expert in mathematics courses, your job is to prepare tutorial "
    "sheets based on the syllabus provided for UG Students."
)


def _extract_topics(syllabus: str) -> list[str]:
    normalized = syllabus.replace("\n", ",").replace(";", ",")
    topics = [topic.strip() for topic in normalized.split(",") if topic.strip()]
    return topics


def prepare_tutorial_sheet(syllabus: str) -> str:
    """Create a markdown tutorial sheet from a syllabus string."""
    topics = _extract_topics(syllabus)
    if not topics:
        raise ValueError("Syllabus must include at least one topic.")

    lines = [
        "# UG Mathematics Tutorial Sheet",
        "",
        f"**Guiding role:** {SYSTEM_PROMPT}",
        "",
        "## Syllabus Topics",
    ]
    lines.extend(f"- {topic}" for topic in topics)
    lines.append("")
    lines.append("## Practice Questions")

    for index, topic in enumerate(topics, start=1):
        lines.extend(
            [
                f"### Topic {index}: {topic}",
                f"1. Define key concepts from **{topic}** in your own words.",
                f"2. Solve one foundational problem on **{topic}**.",
                f"3. Solve one application-focused problem on **{topic}**.",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python tutorial_sheet_maker.py '<syllabus topics>'")

    print(prepare_tutorial_sheet(sys.argv[1]), end="")
