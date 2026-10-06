from .candlestick import build as _candlestick_build
from .ohlc import build as _ohlc_build
from .line import build as _line_build
from .area import build as _area_build

CHART_NAMES = ["Candlestick", "OHLC", "Line", "Area"]

_RENDERERS = {
    "Candlestick": _candlestick_build,
    "OHLC": _ohlc_build,
    "Line": _line_build,
    "Area": _area_build,
}


def get_renderer(chart_type: str):
    return _RENDERERS.get(chart_type, _candlestick_build)