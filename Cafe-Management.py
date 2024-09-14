Menu = {
    "Samosa":10,
    "Bread":15,
    "Chai": 20
}
print("Welcome in Cafe")
print("Samosa = Rs10\nBread = RS15\nChai = RS20")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} has been not available")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter your second order =")
    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f"Your orderded {item_2} has been added")
    else:
        print(f"Ordered item {item_2} has been not available")

    print(f"The total amount has to be paid {order_total}")