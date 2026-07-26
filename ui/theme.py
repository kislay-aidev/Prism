from __future__ import annotations

import streamlit as st

from core.state import get_state
from ui.css import generate_css
from ui.plotly_theme import build_chart_tokens
from ui.themes.light import LIGHT
from ui.themes.dark import DARK
from ui.themes.amoled import AMOLED

_THEMES = {"light": LIGHT, "dark": DARK, "amoled": AMOLED}
_CSS_INJECTED_KEY = "__theme_css_injected"


def get_theme(name: str | None = None):
    if name is None:
        name = st.session_state.get("app_theme", "light")
    return _THEMES.get(name, LIGHT)


def get_current_theme():
    return get_theme()


def available_themes() -> list[str]:
    return list(_THEMES.keys())


def get_chart_theme(theme_name: str | None = None) -> dict:
    t = get_theme(theme_name)
    return build_chart_tokens(t)


def set_theme(name: str) -> None:
    if name in _THEMES:
        st.session_state["app_theme"] = name


def cycle_theme() -> None:
    names = list(_THEMES.keys())
    current = st.session_state.get("app_theme", "light")
    try:
        idx = (names.index(current) + 1) % len(names)
    except ValueError:
        idx = 0
    st.session_state["app_theme"] = names[idx]


def _build_inline_js(t) -> str:
    ib = t.input_bg
    ib_border = t.input_border
    txt = t.text
    muted = t.text_muted
    card = t.card
    border = t.border
    surf = t.surface
    surf2 = t.surface_secondary
    hover = t.hover if t.hover.startswith("rgba") else "transparent"

    return (
        '(function(){'
        'var C={'
        '  ib:"' + ib + '",'
        '  ibb:"' + ib_border + '",'
        '  tx:"' + txt + '",'
        '  mt:"' + muted + '",'
        '  cd:"' + card + '",'
        '  bd:"' + border + '",'
        '  sf:"' + surf + '",'
        '  s2:"' + surf2 + '"'
        '};'
        'function set(el,props){for(var k in props)el.style.setProperty(k,props[k],"important");}'
        'function paint(){'
        '  var p=window.parent.document;'
        '  p.querySelectorAll(\'div[data-baseweb="select"]\').forEach(function(el){'
        '    set(el,{"background-color":C.ib,"border-color":C.ibb,"color":C.tx});'
        '    el.querySelectorAll("*").forEach(function(c){'
        '      if(c.tagName==="SPAN")set(c,{"color":C.tx});'
        '      if(c.tagName==="SVG")set(c,{"fill":C.mt,"color":C.mt});'
        '      if(c.tagName==="INPUT"){set(c,{"background":"transparent","color":C.tx});}'
        '    });'
        '  });'
        '  p.querySelectorAll(\'div[data-baseweb="popover"]\').forEach(function(el){'
        '    set(el,{"background":C.s2,"border-color":C.bd,"color":C.tx});'
        '  });'
        '  p.querySelectorAll(\'div[data-baseweb="popover"] li\').forEach(function(el){'
        '    set(el,{"background":"transparent","color":C.tx});'
        '  });'
        '  p.querySelectorAll(\'div[data-baseweb="menu"]\').forEach(function(el){'
        '    set(el,{"background":C.s2,"border-color":C.bd});'
        '  });'
        '  p.querySelectorAll(\'div[data-baseweb="menu"] li\').forEach(function(el){'
        '    set(el,{"background":"transparent","color":C.tx});'
        '  });'
        '  p.querySelectorAll(\'[data-testid="stExpander"] summary\').forEach(function(el){'
        '    set(el,{"background":C.cd,"color":C.tx,"border-color":C.bd});'
        '  });'
        '  p.querySelectorAll(\'[data-testid="stExpander"] summary + div\').forEach(function(el){'
        '    set(el,{"background":C.sf});'
        '  });'
        '  p.querySelectorAll(\'span[data-baseweb="tag"]\').forEach(function(el){'
        '    set(el,{"color":C.tx});'
        '  });'
        '  p.querySelectorAll(\'span[data-baseweb="tag"] span[role="button"]\').forEach(function(el){'
        '    set(el,{"color":C.mt});'
        '  });'
        '  p.querySelectorAll(\'[data-testid="stSidebar\"]\').forEach(function(el){'
        '    set(el,{"background":C.s2});'
        '  });'
        '}'
        'paint();'
        'var mo=new MutationObserver(paint);'
        'try{mo.observe(p.body,{childList:true,subtree:true});}catch(e){}'
        'setInterval(paint,500);'
        '})()'
    )


def inject_theme_css() -> None:
    t = get_theme()
    css = generate_css(t)
    js = _build_inline_js(t)
    st.markdown(
        f'<style id="prism-theme">{css}</style>'
        f'<script id="prism-theme-js">{js}</script>',
        unsafe_allow_html=True,
    )


def render_theme_selector() -> None:
    state = get_state()
    current = state.theme
    names = available_themes()

    if st.button(
        f"Switch to {' / '.join(n for n in names if n != current)}",
        key="theme_cycle_selector_btn",
        use_container_width=True,
    ):
        cycle_theme()
        st.rerun()


def render_theme_switcher_compact() -> None:
    state = get_state()
    current = state.theme
    icons = {"light": "☀", "dark": "🌙", "amoled": "⚫"}
    mode_names = {"light": "Light mode", "dark": "Dark mode", "amoled": "AMOLED mode"}
    icon = icons.get(current, "☀")
    label = mode_names.get(current, "Light mode")

    if st.button(
        f"{icon} {label}",
        key="theme_cycle_btn",
        use_container_width=True,
        type="secondary",
    ):
        cycle_theme()
        st.rerun()
