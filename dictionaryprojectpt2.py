wares = [{
    "name": "6in Tungsten Cube",
    "price": 9689.99,
    "mass": "65 kilograms, 143.3 pounds",
}, 
{
    "name": "55 Gallon Drum of Apple Juice",
    "price": 799.99,
    "mass": "220 kilograms, 485.02 pounds",
},
{
    "name": "Number #2 HB Pencil",
    "price": 0.19,
    "mass": "0.05 kilograms, 0.11 pounds",
},
{
    "name": "The Sun",
    "price": 5.13,
    "mass": "1,900,000,000,000,000,000,000,000,000,000 kilograms, 4188782981512674000000000000000 pounds",
},
{
    "name": "TON 618",
    "price": 15.99,
    "mass": "66 billion solar masses, 2.8939798982e+41 pounds",
}]
print("Welcome to my humble store! Here are my wares:")
for index, item in enumerate(wares):
    print((index + 1), ":", item["name"])
cart = []
total = 0
request = 0
while request != "Exit":
    request = input("What would you like to purchase, 1 through 5? Or enter \"Exit\" to leave.     ")
    if request != "Exit":
        request = int(request)
    else:
        break
    if request > 0 and request < 6:
        cart.append(wares[request - 1]["name"])
        total += wares[request - 1]["price"]
        print(wares[request - 1]["name"], "added to cart.")
    else:
        print("Item not found.")
print("Cart: ", cart)
print("Your total comes down to: $", total)