pizzas = ['Pineapple', 'Pepperoni', 'Vegetarian', 'Cookie']

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I love pizza!!!!")

friends_pizza = pizzas[0:3]
print(friends_pizza)

friends_pizza = pizzas[2:]
print(friends_pizza)

friends_pizza = pizzas[:]
print(friends_pizza)

friends_pizza.append('Yum')

print(friends_pizza)
