from collections import Counter
import random 

tickets=Counter({
    "p1":5,
    "p2":2,
    "p3":3
})


ticket_pool=list(tickets.elements())
print("Ticket pool: ",ticket_pool)

winner=random.choice(ticket_pool)
print("winner: ",winner)