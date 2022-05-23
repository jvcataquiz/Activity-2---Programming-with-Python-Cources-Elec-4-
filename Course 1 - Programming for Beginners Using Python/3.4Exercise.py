class Customers:
    greeting = "welcome to Coffee Palace!!!"

customer_1 = Customers()
customer_1.Name = "Samirah"
customer_1.Beverage = "Iced Coffee Latte"
customer_1.Food = "Cinnamon Roll"
customer_1.Total = 225

customer_2 = Customers()
customer_2.Name = "Jerry"
customer_2.Beverage = "Caramel Macchiato"
customer_2.Food = "Glazed Doughnut"
customer_2.Total = 230

print(Customers.greeting)
print(customer_1.Beverage)
print(customer_2.Food)