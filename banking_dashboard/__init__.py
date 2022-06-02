"""Project main source package."""
import warnings

try:
    from importlib.metadata import version as __get_version
    __version__ = __get_version('banking_dashboard')
    del __get_version
except ImportError:
    warnings.warn("Missing package version metadata for `banking_dashboard`!")
    __version__ = "UNKNOWN_PACKAGE_METADATA"
