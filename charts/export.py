def png(fig):
    return fig.to_image(format="png")

def html(fig):
    return fig.to_html(include_plotlyjs="cdn")
