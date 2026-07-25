LAYOUTS={
'Compact':['Chart','AI'],
'Standard':['Chart','Financials','News'],
'Professional':['Chart','Technical','Financials','Portfolio','AI']
}

def get_layout(name='Standard'):
    return LAYOUTS.get(name,LAYOUTS['Standard'])
