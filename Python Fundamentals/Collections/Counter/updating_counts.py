from collections import Counter

stock=Counter({
    "laptop":5,
    "smartphone":5,
    "tablet":4,
    "monitor":3,
    "keyboard":6
})

monthly_delivery={"laptop":3,"smartphone":5}

# adds up in the existing stock
stock.update(monthly_delivery)
print(stock)


orders={"laptop":2,"smartphone":3}
stock.subtract(orders)
print(stock)