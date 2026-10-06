import streamlit as st


def render(metrics: dict, cols: int = 4):
    items = list(metrics.items())
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    for row in rows:
        columns = st.columns(len(row))
        for col, (key, value) in zip(columns, row):
            col.metric(key, value)


def metric_card(label: str, value, delta=None, help_text: str = ""):
    st.metric(label=label, value=value, delta=delta, help=help_text)
