"""Read-only forum fixture for issue #186."""

from machina.core.db.models import get_model

Forum = get_model("forum", "Forum")


def fixture_forum_names():
    """Return fixture forum names in deterministic primary-key order."""
    return Forum.objects.order_by("pk").values_list("name", flat=True)
