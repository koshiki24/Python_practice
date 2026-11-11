f1 = Flight("AI202", 100)
f2 = Flight("6E305", 50)

# Booking tickets
f1.book_ticket(20)
f1.book_ticket(30)

# Display flight details
f1.display_details()

# Cancelling tickets
f1.cancel_ticket(10)

# Display updated details
f1.display_details()

# Trying to overbook
f1.book_ticket(100)

# Display another flight
f2.display_details()