try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._reader import napari_get_reader
from ._sample_data import make_sample_data

__all__ = (
    "napari_get_reader",
    "make_sample_data",
)
