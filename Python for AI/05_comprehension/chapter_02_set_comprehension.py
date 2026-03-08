recipes = {
    "Masala" : ["Ginger", "Cardamom", "Cloves"],
    "Lemon" : ["Lemon", "Sugar", "Cloves"],
    "Spicy" : ["Ginger", "Black Peper", "Sugar"],
}
unique_ingredients = {spices for ingredients in recipes.values() for spices in ingredients}
print(unique_ingredients)

nums = [1,2,3]
letters = ["a","b"]
cartesian_product_pair = {(number, letter) for number in nums for letter in letters}
print(cartesian_product_pair)

even_number_square = {number**2 for number in range(1,20) if number%2==0}
print(sorted(even_number_square))