wares = [{
    "name": "6\" Tungsten Cube",
    "price": 9689.99,
    "mass": "65 kilograms, 143.3 pounds",
    "stock": 9223372036854775807
}, 
{
    "name": "55 Gallon Drum of Apple Juice",
    "price": 799.99,
    "mass": "220 kilograms, 485.02 pounds",
    "stock": 340282366920938463463374607431768211456

},
{
    "name": "Number #2 HB Pencil",
    "price": 0.19,
    "mass": "0.05 kilograms, 0.11 pounds",
    "stock": 2
},
{
    "name": "The Sun",
    "price": 5.13,
    "mass": "1,900,000,000,000,000,000,000,000,000,000 kilograms, 4188782981512674000000000000000 pounds",
    "stock": 1
},
{
    "name": "TON 618",
    "price": 15.99,
    "mass": "66 billion solar masses, 2.8939798982e+41 pounds",
    "stock": 3
}]
print("Welcome to my humble store! Here are my wares:")
for i in range(5):
    print((i + 1), ": ", wares[i]["name"])
