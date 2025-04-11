prices = {"veg": 150, "non-veg": 200, "combo": 300}

meal_type = input("Enter Meal Type (Veg/Non-Veg/Combo): ").strip().lower()
if meal_type not in prices:
    print("Invalid meal type selected!")
else:
    quantity = int(input("Enter Quantity: "))
    is_festival = input("Is today a festival (yes/no)? ").strip().lower()

    subtotal = prices[meal_type] * quantity
    if is_festival == "yes":
        subtotal *= 0.90 

    gst = subtotal * 0.05
    free_dessert = "Yes" if subtotal > 1000 else "No"
    total_bill = subtotal + gst

    print(f"\n===== Restaurant Bill =====")
    print(f"Meal Type: {meal_type.capitalize()}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"GST (5%): ₹{gst:.2f}")
    print(f"Total Bill: ₹{total_bill:.2f}")
    print(f"Free Dessert: {free_dessert}")
    print("===========================")
