from django.shortcuts import _get_queryset


def get_object_or_none(klass, *args, **kwargs):
    """ Calls get() on a given model manager, but it returns None instead of the model’s
        DoesNotExist exception.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except:  # noqa: E722
        return None


def first_or_none(klass, *args, **kwargs):
    """ Returns the first object matching the filters, or None. """
    queryset = _get_queryset(klass)
    return queryset.filter(*args, **kwargs)[0]
