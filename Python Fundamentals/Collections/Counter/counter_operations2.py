from collections import Counter

stock=Counter({
    "laptop":5,
    "smartphone":5,
    "tablet":4,
    "monitor":-3,
    "keyboard":-6
})

available_inventory= +stock
print(available_inventory)

backeorderd_inventory= -stock
print(backeorderd_inventory)