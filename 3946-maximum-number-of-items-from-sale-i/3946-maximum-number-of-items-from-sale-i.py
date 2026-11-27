from typing import List
# xItems(sde  

class Solution:

  def maximumSaleItems(sf, items: List[List[int]], budget: int) -> int:
    max_val = 1500
    div_count = [0] * (max_val + 1)

    for factor, _ in items:
      d = 1
      while d * d <= factor:
        if factor % d == 0:
          div_count[d] += 1
          if d * d != factor:
            div_count[factor // d] += 1
        d += 1

    dp = [0] * (budget + 1)

    for factor, price in items:
      if price > budget:
        continue
      gain = div_count[factor]
      for b in range(budget, price - 1, -1):
        if dp[b - price] + gain > dp[b]:
          dp[b] = dp[b - price] + gain

    for _, price in items:
      if price > budget:
        continue
      for b in range(price, budget + 1):
        if dp[b - price] + 1 > dp[b]:
          dp[b] = dp[b - price] + 1

    return max(dp)