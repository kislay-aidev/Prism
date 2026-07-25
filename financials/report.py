from .dashboard import build
from .valuation import metrics
from .quality import company_quality

def generate(info):
    return {
      "dashboard":build(info),
      "valuation":metrics(info),
      "quality":company_quality(info)
    }
