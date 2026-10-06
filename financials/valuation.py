def metrics(info):
    return {
      "Market Cap":info.get("marketCap"),
      "Enterprise Value":info.get("enterpriseValue"),
      "Price/Sales":info.get("priceToSalesTrailing12Months"),
      "Price/Book":info.get("priceToBook"),
      "EV/EBITDA":info.get("enterpriseToEbitda")
    }
