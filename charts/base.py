import plotly.graph_objects as go

def apply_layout(fig,title):
    fig.update_layout(title=title,template="plotly_dark",height=650,
                      margin=dict(l=20,r=20,t=50,b=20),
                      legend_orientation="h")
    return fig
