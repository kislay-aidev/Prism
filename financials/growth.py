def growth_metrics(info):
    return {
      "Revenue Growth":info.get("revenueGrowth"),
      "Earnings Growth":info.get("earningsGrowth"),
      "Profit Margins":info.get("profitMargins"),
      "Operating Margins":info.get("operatingMargins")
    }
