def levels(high, low):
    diff=high-low
    return {k:high-diff*v for k,v in [("23.6%",0.236),("38.2%",0.382),("50%",0.5),("61.8%",0.618),("78.6%",0.786)]}
