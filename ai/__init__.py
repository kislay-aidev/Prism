from .scoring import score
from .recommendation import recommend
from .risk import classify, label as risk_label
from .targets import suggest
from .rating import stars
from .portfolio_score import calculate as portfolio_score
from .weights import WEIGHTS
from .summary import build as build_summary
from .dashboard import build as build_dashboard

__all__ = [
    "score",
    "recommend",
    "classify",
    "risk_label",
    "suggest",
    "stars",
    "portfolio_score",
    "WEIGHTS",
    "build_summary",
    "build_dashboard",
]
