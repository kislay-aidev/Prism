from .ratios import calculate
from .growth import growth_metrics
from .dividend import dividend_metrics
from .fundamental_score import score

def build(info):
    return {
      "ratios":calculate(info),
      "growth":growth_metrics(info),
      "dividend":dividend_metrics(info),
      "fundamental_score":score(info)
    }
