def ft_filter(func, ite):
    """Filters elements from an iterable based on a function."""
    if func is None:
        func = bool
    yield from (x for x in ite if func(x))
