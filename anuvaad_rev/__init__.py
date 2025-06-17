"""anuvaad-rev - Indian Language Translation Module"""

from .translator import IndicTranslator
from .constants import SUPPORTED_LANGUAGES

__version__ = "0.1.2"
__all__ = ["IndicTranslator", "SUPPORTED_LANGUAGES"]