food_category = Category("Food")
clothing_category = Category("Clothing")

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(150, "Groceries")
food_category.withdraw(50, "Eating out")

clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(200, "Clothes")
clothing_category.withdraw(100, "Shoes")

print(create_spend_chart([food_category, clothing_category]))
