def dividend_metrics(info):
    return {
      "Dividend Yield":info.get("dividendYield"),
      "Payout Ratio":info.get("payoutRatio"),
      "Ex-Dividend Date":info.get("exDividendDate")
    }
