"""Read-only forum fixture for issue #186."""

from machina.apps.forum.models import Forum


def fixture_forum_names():
    """Return fixture forum names in deterministic primary-key order."""
    return Forum.objects.order_by("pk").values_list("name", flat=True)


FIXTURE_FORUM_LABELS = (
    "Community announcements",
    "Community introductions",
    "Support and troubleshooting",
    "Feature requests and feedback",
    "Project documentation",
    "Project release notes",
    "Community showcase",
    "Local events and meetups",
    "Accessibility discussion",
    "Translations and localization",
    "Community guidelines",
    "Moderation discussions",
    "Account setup and questions",
    "Privacy and notifications",
    "Developer discussion",
    "Extension development",
    "Integration examples",
    "Testing and quality",
    "Search and discovery",
    "Community help and resources",
    "Getting started guides",
    "Project announcements",
    "Community questions",
    "Project planning",
    "Design and usability",
    "Contributor onboarding",
    "Community knowledge base",
    "Support case studies",
    "Integration support",
    "General discussion",
    "Weekly project updates",
    "Community archive",
    "Contributor resources",
)
