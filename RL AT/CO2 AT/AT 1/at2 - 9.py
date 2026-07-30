stock_price = 500
future_price = 550

if future_price > stock_price:
    action = "BUY"
    reward = future_price - stock_price

elif future_price < stock_price:
    action = "SELL"
    reward = stock_price - future_price

else:
    action = "HOLD"
    reward = 0

print("Current Price:", stock_price)
print("Future Price:", future_price)
print("Action:", action)
print("Reward:", reward)
