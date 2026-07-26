def generate_css(t) -> str:
    return f""":root {{
  --bg: {t.surface};
  --bg2: {t.surface_secondary};
  --sidebar-bg: {t.sidebar};
  --text: {t.text};
  --muted: {t.text_muted};
  --border: {t.border};
  --border-light: {t.border_light};
  --card-bg: {t.card};
  --accent: {t.primary};
  --accent-hover: {t.primary_hover};
  --hover: {t.hover};
  --selected: {t.selected};
  --success: {t.success};
  --warning: {t.warning};
  --danger: {t.danger};
  --info: {t.info};
  --input-bg: {t.input_bg};
  --input-border: {t.input_border};
  --input-text: {t.input_text};
  --input-placeholder: {t.input_placeholder};
  --focus: {t.border_focus};
  --grid: {t.chart_grid};
  --shadow-sm: {t.shadow_sm};
  --shadow-md: {t.shadow_md};
  --shadow-lg: {t.shadow_lg};
  --radius-sm: {t.radius_sm};
  --radius-md: {t.radius_md};
  --radius-lg: {t.radius_lg};
  --font-xs: {t.font_size_xs};
  --font-sm: {t.font_size_sm};
  --font-md: {t.font_size_md};
  --font-lg: {t.font_size_lg};
  --font-xl: {t.font_size_xl};
  --font-family: {t.font_family};
  --transition: {t.transition_normal};
  --transition-fast: {t.transition_fast};
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 16px;
  --spacing-xl: 24px;
  --spacing-2xl: 32px;
}}

/* ===== BASE ===== */
.stApp {{ background: var(--bg); color: var(--text); font-family: var(--font-family); }}
.stApp > header {{ background: transparent !important; }}
.st-caption, .stCaption, .caption {{ color: var(--muted) !important; font-size: var(--font-xs) !important; }}
.st-subheader {{ color: var(--text); font-weight: 600; }}
a {{ color: var(--accent); transition: opacity var(--transition-fast); }}
a:hover {{ opacity: 0.8; }}
hr {{ border-color: var(--border) !important; opacity: 1; }}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {{
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border);
}}
section[data-testid="stSidebar"] > div {{
  padding-top: var(--spacing-lg);
}}
section[data-testid="stSidebar"] hr {{
  border-color: var(--border);
  margin: var(--spacing-md) 0;
  opacity: 0.6;
}}
button[data-testid="baseButton-sidebar"] {{ z-index: 999 !important; }}

/* Sidebar branding */
section[data-testid="stSidebar"] h4 {{
  margin: 0 0 2px 0 !important;
  font-size: var(--font-lg) !important;
  font-weight: 700 !important;
  letter-spacing: -0.3px;
}}
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
  margin: 0 0 var(--spacing-md) 0 !important;
  font-size: var(--font-sm) !important;
  opacity: 0.6;
}}

/* ===== BUTTONS ===== */
.stButton > button {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: var(--radius-md);
  padding: var(--spacing-sm) var(--spacing-lg);
  font-family: var(--font-family);
  font-size: var(--font-sm);
  font-weight: 500;
  transition: all var(--transition-fast);
  cursor: pointer;
}}
.stButton > button:hover {{
  border-color: var(--accent);
  background: var(--hover);
}}
.stButton > button:focus-visible {{
  outline: none;
  box-shadow: 0 0 0 2px var(--focus);
}}
.stButton > button:disabled {{
  opacity: 0.4;
  cursor: not-allowed;
}}

button[data-testid="baseButton-secondary"] {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: var(--radius-md);
  padding: var(--spacing-sm) var(--spacing-lg);
  font-family: var(--font-family);
  font-size: var(--font-sm);
  font-weight: 500;
  transition: all var(--transition-fast);
  cursor: pointer;
}}
button[data-testid="baseButton-secondary"]:hover {{
  border-color: var(--accent);
  background: var(--hover);
}}
button[data-testid="baseButton-secondary"]:focus-visible {{
  outline: none;
  box-shadow: 0 0 0 2px var(--focus);
}}
button[data-testid="baseButton-secondary"]:disabled {{
  opacity: 0.4;
  cursor: not-allowed;
}}

button[data-testid="baseButton-primary"] {{
  background: var(--accent);
  border: 1px solid var(--accent);
  color: {t.text_inverse};
  border-radius: var(--radius-md);
  padding: var(--spacing-sm) var(--spacing-lg);
  font-family: var(--font-family);
  font-size: var(--font-sm);
  font-weight: 600;
  transition: all var(--transition-fast);
  cursor: pointer;
}}
button[data-testid="baseButton-primary"]:hover {{
  background: var(--accent-hover);
  border-color: var(--accent-hover);
}}
button[data-testid="baseButton-primary"]:focus-visible {{
  outline: none;
  box-shadow: 0 0 0 2px var(--focus);
}}
button[data-testid="baseButton-primary"]:disabled {{
  opacity: 0.4;
  cursor: not-allowed;
}}

button[data-testid="baseButton-secondaryFormSubmit"] {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
}}
button[data-testid="baseButton-secondaryFormSubmit"]:hover {{
  border-color: var(--accent);
}}

/* ===== THEME SWITCHER ===== */
section[data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {{
  font-size: var(--font-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  min-height: 34px;
  border-radius: var(--radius-md);
  text-align: left;
  justify-content: flex-start;
}}

/* ===== TEXT INPUTS ===== */
.stTextInput input {{
  background: var(--input-bg) !important;
  border: 1px solid var(--input-border) !important;
  color: var(--input-text) !important;
  border-radius: var(--radius-md) !important;
  padding: var(--spacing-sm) var(--spacing-md) !important;
  font-family: var(--font-family);
  font-size: var(--font-sm);
  transition: all var(--transition-fast);
}}
.stTextInput input:focus {{
  border-color: var(--focus) !important;
  box-shadow: 0 0 0 3px {t.primary}22 !important;
}}
.stTextInput input::placeholder {{
  color: var(--input-placeholder) !important;
  opacity: 1;
}}
.stTextInput input:disabled {{
  opacity: 0.4;
  background: var(--bg2) !important;
}}
.stTextInput > div > div > input {{
  background: var(--input-bg) !important;
}}

.st-emotion-cache-1kyxreq, .st-emotion-cache-1dp5vir,
.st-emotion-cache-16idsys, .st-emotion-cache-13kjsby {{
  background: var(--input-bg) !important;
  border-color: var(--input-border) !important;
  color: var(--input-text) !important;
  border-radius: var(--radius-md) !important;
}}

/* ===== NUMBER / DATE INPUTS ===== */
.stNumberInput input {{
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  color: var(--input-text);
  border-radius: var(--radius-md);
  font-family: var(--font-family);
  font-size: var(--font-sm);
}}
.stNumberInput input:focus {{
  border-color: var(--focus);
  box-shadow: 0 0 0 3px {t.primary}22;
}}
.stNumberInput button {{
  border-color: var(--border) !important;
  color: var(--text) !important;
  background: var(--card-bg) !important;
  border-radius: var(--radius-sm);
}}
.stNumberInput button:hover {{
  background: var(--hover) !important;
}}

.stDateInput input {{
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  color: var(--input-text);
  border-radius: var(--radius-md);
  font-family: var(--font-family);
}}
.stDateInput input:focus {{
  border-color: var(--focus);
  box-shadow: 0 0 0 3px {t.primary}22;
}}

.stTextArea textarea {{
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  color: var(--input-text);
  border-radius: var(--radius-md);
  font-family: var(--font-family);
}}
.stTextArea textarea:focus {{
  border-color: var(--focus);
  box-shadow: 0 0 0 3px {t.primary}22;
}}

/* ===== SELECTBOX ===== */
div[data-baseweb="select"] {{
  background: var(--input-bg) !important;
  border-color: var(--input-border) !important;
  border-radius: var(--radius-md) !important;
  transition: all var(--transition-fast);
}}
div[data-baseweb="select"] > div {{
  background: transparent !important;
  border-color: transparent !important;
}}
div[data-baseweb="select"]:hover {{
  border-color: var(--accent) !important;
}}
div[data-baseweb="select"]:focus-within {{
  border-color: var(--focus) !important;
  box-shadow: 0 0 0 3px {t.primary}22 !important;
}}
div[data-baseweb="select"] span {{
  color: var(--text) !important;
}}
div[data-baseweb="select"] svg {{
  fill: var(--muted) !important;
  color: var(--muted) !important;
}}
div[data-baseweb="select"] input {{
  background: transparent !important;
  color: var(--text) !important;
}}
div[data-baseweb="select"] input::placeholder {{
  color: var(--input-placeholder) !important;
}}

/* ===== POPOVER / DROPDOWN ===== */
div[data-baseweb="popover"] {{
  background: var(--card-bg) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  box-shadow: var(--shadow-lg) !important;
  z-index: 999999 !important;
  overflow: hidden;
}}
div[data-baseweb="popover"] ul {{
  background: transparent !important;
  padding: var(--spacing-xs);
}}
div[data-baseweb="popover"] li[role="option"] {{
  color: var(--text) !important;
  background: transparent !important;
  border-radius: var(--radius-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  transition: background var(--transition-fast);
  cursor: pointer;
  font-size: var(--font-sm);
}}
div[data-baseweb="popover"] li[role="option"]:hover {{
  background: var(--hover) !important;
}}
div[data-baseweb="popover"] li[role="option"][aria-selected="true"] {{
  background: var(--selected) !important;
  color: var(--text) !important;
}}

.stSelectbox div[data-baseweb="select"],
.stSelectbox div[data-baseweb="select"] > div {{
  background: var(--input-bg) !important;
  border: 1px solid var(--input-border) !important;
}}
.stSelectbox div[data-baseweb="select"] span {{
  color: var(--text);
}}

/* ===== MULTISELECT ===== */
.stMultiSelect div[data-baseweb="select"] {{
  background: var(--input-bg) !important;
  border: 1px solid var(--input-border) !important;
  border-radius: var(--radius-md) !important;
}}
.stMultiSelect div[data-baseweb="select"]:focus-within {{
  border-color: var(--focus) !important;
}}
.stMultiSelect div[data-baseweb="select"] span {{
  color: var(--text);
}}
.stMultiSelect div[data-baseweb="select"] input::placeholder {{
  color: var(--input-placeholder) !important;
}}

/* Multiselect tags (Indicator pills) */
span[data-baseweb="tag"] {{
  background-color: {t.primary}22 !important;
  color: var(--text) !important;
  border-radius: var(--radius-sm) !important;
  border: 1px solid {t.primary}44 !important;
  transition: all var(--transition-fast);
  font-size: var(--font-xs);
  font-weight: 500;
}}
span[data-baseweb="tag"]:hover {{
  background-color: {t.primary}33 !important;
  border-color: {t.primary}66 !important;
}}
span[data-baseweb="tag"] span[role="button"] {{
  color: var(--muted) !important;
  cursor: pointer;
  transition: color var(--transition-fast);
}}
span[data-baseweb="tag"] span[role="button"]:hover {{
  color: var(--danger) !important;
}}

/* ===== RADIO BUTTONS ===== */
div[data-testid="stRadio"] label {{
  color: var(--text) !important;
  cursor: pointer;
  font-size: var(--font-sm);
  transition: color var(--transition-fast);
}}
div[data-testid="stRadio"] label:hover {{
  color: var(--accent) !important;
}}
div[data-testid="stRadio"] [data-baseweb="radio"] {{
  transition: all var(--transition-fast);
}}
div[data-testid="stRadio"] [data-baseweb="radio"]:hover {{
  border-color: var(--accent) !important;
}}
div[data-testid="stRadio"] [aria-checked="true"] [data-baseweb="radio"] {{
  border-color: var(--accent) !important;
}}
div[data-testid="stRadio"] [aria-checked="true"] span {{
  color: var(--accent) !important;
}}

/* ===== CHECKBOXES ===== */
div[data-testid="stCheckbox"] label {{
  color: var(--text) !important;
  cursor: pointer;
  font-size: var(--font-sm);
}}

/* ===== SLIDER ===== */
div[data-testid="stSlider"] div[data-baseweb="slider"] {{
  background: var(--border) !important;
}}
div[data-testid="stSlider"] div[data-baseweb="slider"] > div:first-child {{
  background: var(--accent) !important;
}}
div[data-testid="stSlider"] div[role="slider"] {{
  background: var(--accent) !important;
  border: 2px solid var(--bg) !important;
}}
div[data-testid="stSlider"] div[role="slider"]:focus-visible {{
  box-shadow: 0 0 0 2px var(--focus) !important;
}}

/* ===== EXPANDER ===== */
[data-testid="stExpander"] {{
  background: transparent !important;
  margin: var(--spacing-sm) 0;
}}
[data-testid="stExpander"] summary {{
  background: var(--card-bg) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  padding: var(--spacing-md) var(--spacing-lg) !important;
  transition: all var(--transition-fast);
  font-weight: 500;
  font-size: var(--font-sm);
}}
[data-testid="stExpander"] summary:hover {{
  background: var(--hover) !important;
  border-color: var(--accent) !important;
}}
[data-testid="stExpander"] summary svg {{
  fill: var(--muted) !important;
  color: var(--muted) !important;
  transition: transform var(--transition-fast);
}}
[data-testid="stExpander"][aria-expanded="true"] summary svg {{
  transform: rotate(90deg);
}}
[data-testid="stExpander"] summary + div {{
  border: 1px solid var(--border);
  border-top: none;
  border-radius: 0 0 var(--radius-md) var(--radius-md);
  background: var(--card-bg) !important;
  padding: var(--spacing-md);
}}

/* ===== TABS ===== */
.stTabs [data-baseweb="tab-list"] {{
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  gap: 0;
}}
.stTabs [data-baseweb="tab"] {{
  color: var(--muted);
  transition: all var(--transition-fast);
  padding: var(--spacing-md) var(--spacing-lg);
  font-size: var(--font-sm);
  font-weight: 500;
}}
.stTabs [data-baseweb="tab"]:hover {{
  color: var(--text);
}}
.stTabs [aria-selected="true"] {{
  color: var(--accent) !important;
  border-bottom-color: var(--accent) !important;
  font-weight: 600;
}}

/* ===== METRICS ===== */
div[data-testid="stMetric"] {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
}}
div[data-testid="stMetric"]:hover {{
  border-color: var(--accent);
}}
div[data-testid="stMetricLabel"] {{
  color: var(--muted) !important;
  font-size: var(--font-xs) !important;
  font-weight: 500;
}}
div[data-testid="stMetricValue"] {{
  font-size: var(--font-lg) !important;
  font-weight: 600;
}}
div[data-testid="stMetricDelta"][data-direction="up"] {{
  color: var(--success) !important;
}}
div[data-testid="stMetricDelta"][data-direction="down"] {{
  color: var(--danger) !important;
}}

/* ===== DATAFRAME ===== */
.stDataFrame {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  overflow: hidden;
}}
.stDataFrame [data-testid="stDataFrameResizable"] {{
  border: none;
}}
.stDataFrame table {{
  color: var(--text);
}}
.stDataFrame thead tr th {{
  background: var(--bg2);
  color: var(--muted);
  border-bottom: 1px solid var(--border);
  font-size: var(--font-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}
.stDataFrame tbody tr td {{
  border-bottom: 1px solid var(--border-light);
  font-size: var(--font-sm);
}}
.stDataFrame tbody tr:hover {{
  background: var(--hover);
}}
.stDataFrame tbody tr td:first-child {{
  font-weight: 600;
}}

/* ===== ALERTS ===== */
.stAlert {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  color: var(--text);
  padding: var(--spacing-md) var(--spacing-lg);
}}
.stAlert.st-info {{
  border-color: var(--info) !important;
  background: {t.info_bg} !important;
}}
.stAlert.st-success {{
  border-color: var(--success) !important;
  background: {t.success_bg} !important;
}}
.stAlert.st-warning {{
  border-color: var(--warning) !important;
  background: {t.warning_bg} !important;
}}
.stAlert.st-error {{
  border-color: var(--danger) !important;
  background: {t.danger_bg} !important;
}}

/* ===== PROGRESS ===== */
.stProgress > div > div {{
  background: var(--accent);
  border-radius: var(--radius-sm);
}}
.stProgress > div {{
  background: var(--border);
  border-radius: var(--radius-sm);
}}

/* ===== TOOLTIPS ===== */
div[data-testid="stTooltip"], div[role="tooltip"] {{
  background: var(--card-bg) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  box-shadow: var(--shadow-lg) !important;
  z-index: 999999 !important;
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: var(--font-xs);
}}

/* ===== SCROLLBARS ===== */
::-webkit-scrollbar {{
  width: 6px;
  height: 6px;
}}
::-webkit-scrollbar-track {{
  background: var(--bg);
}}
::-webkit-scrollbar-thumb {{
  background: var(--border);
  border-radius: 3px;
}}
::-webkit-scrollbar-thumb:hover {{
  background: var(--muted);
}}

/* ===== PLOTLY ===== */
.stPlotlyChart {{
  margin: 0;
  padding: 0;
}}
.js-plotly-plot {{
  margin: 0;
}}
.js-plotly-plot .plot-container {{
  border: none;
}}
.js-plotly-plot .svg-container {{
  border-radius: var(--radius-md);
}}

/* ===== SEARCH COMPONENT ===== */
.search-results {{
  margin-top: var(--spacing-sm);
}}
.search-results button[data-testid="baseButton-secondary"] {{
  text-align: left !important;
  justify-content: flex-start !important;
  background: transparent !important;
  border: none !important;
  border-radius: var(--radius-md) !important;
  padding: var(--spacing-md) var(--spacing-lg) !important;
  transition: all var(--transition-fast) !important;
  border: 1px solid transparent !important;
}}
.search-results button[data-testid="baseButton-secondary"]:hover {{
  background: var(--hover) !important;
  border-color: var(--border) !important;
}}
.search-results button[data-testid="baseButton-secondary"]:focus-visible {{
  outline: none;
  box-shadow: 0 0 0 2px var(--focus) !important;
}}
.search-results button[data-testid="baseButton-secondary"] p {{
  margin: 0 !important;
}}
.search-results button[data-testid="baseButton-secondary"] strong {{
  font-weight: 600;
  font-size: var(--font-sm);
}}
.search-results hr {{
  border-color: var(--border-light) !important;
  margin: var(--spacing-xs) var(--spacing-lg);
  opacity: 0.5;
}}
.search-recent-label {{
  margin: var(--spacing-sm) 0 var(--spacing-xs) 0;
  font-size: var(--font-xs);
  opacity: 0.5;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-weight: 600;
}}
.search-no-matches {{
  font-size: var(--font-sm);
  opacity: 0.45;
  padding: var(--spacing-sm);
  text-align: center;
}}

/* ===== FOCUS RINGS ===== */
*:focus-visible {{
  outline: none !important;
  box-shadow: 0 0 0 2px var(--focus) !important;
}}
*:focus:not(:focus-visible) {{
  outline: none !important;
  box-shadow: none !important;
}}

/* ===== BASEWEB OVERRIDES ===== */
div[data-baseweb="popover"],
div[data-baseweb="popover"] * {{
  background-color: var(--card-bg) !important;
  color: var(--text) !important;
}}
div[data-baseweb="popover"] li {{
  background-color: transparent !important;
}}
div[data-baseweb="popover"] li:hover {{
  background-color: var(--hover) !important;
}}
div[data-baseweb="popover"] li[aria-selected="true"] {{
  background-color: var(--selected) !important;
}}

div[data-baseweb="menu"] {{
  background: var(--card-bg) !important;
  border-color: var(--border) !important;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
}}
div[data-baseweb="menu"] ul {{
  background: transparent !important;
}}
div[data-baseweb="menu"] li {{
  background: transparent !important;
  color: var(--text) !important;
  padding: var(--spacing-sm) var(--spacing-md);
}}
div[data-baseweb="menu"] li:hover {{
  background: var(--hover) !important;
}}

div[data-baseweb="side-nav"] {{
  background: var(--sidebar-bg) !important;
}}
[data-baseweb="tab-border"] {{
  background-color: var(--border) !important;
}}
[data-baseweb="tab-list"] {{
  background-color: var(--bg2) !important;
}}
[role="tablist"] {{
  background-color: var(--bg2) !important;
}}
[role="tab"] {{
  color: var(--text) !important;
}}
[role="tab"][aria-selected="true"] {{
  color: var(--accent) !important;
}}
[data-baseweb="tab-panel"] {{
  background: transparent !important;
}}

div[data-baseweb="notification"] {{
  background: var(--card-bg) !important;
  color: var(--text) !important;
}}
div[data-baseweb="modal"] {{
  background: var(--card-bg) !important;
}}
div[data-baseweb="modal"] * {{
  color: var(--text) !important;
}}

/* ===== MARKET STATUS ===== */
section[data-testid="stSidebar"] .stMarkdown p {{
  font-size: var(--font-sm);
}}

/* ===== DIVIDER OVERRIDE ===== */
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] hr {{
  border-color: var(--border);
  opacity: 0.4;
  margin: var(--spacing-md) 0;
}}

/* ===== WATCHLIST / FAVORITES ===== */
section[data-testid="stSidebar"] [data-testid="stExpander"] {{
  margin: var(--spacing-sm) 0;
}}
"""