# file = open(r"Python for AI/09_exception/order.txt", "w")
# try:
#     file.write("Masala tea- 4 cups")
# finally:
#     file.close()

#moder way to do so
with open(r"Python for AI/09_exception/order.txt", "w") as file:
    file.write("Masala Tea - 4 cups")