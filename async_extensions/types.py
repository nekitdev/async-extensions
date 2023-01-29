from solus import Singleton

__all__ = ("NoDefault", "no_default")


class NoDefault(Singleton):
    """Represents the absence of default values."""


no_default = NoDefault()
