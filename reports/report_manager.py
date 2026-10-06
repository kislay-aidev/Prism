from .executive_summary import build as executive
from .technical_report import build as technical
from .financial_report import build as financial
from .portfolio_report import build as portfolio


def build_complete_report(
    technical_data: dict, financial_data: dict, portfolio_data: dict
) -> dict:
    return executive(
        technical(technical_data),
        financial(financial_data),
        portfolio(portfolio_data),
    )
