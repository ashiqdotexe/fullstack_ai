tea_prices_in_taka = {
    "Masala" : 50,
    "Malai" : 20,
    "Special" : 100
}
tea_prices_in_usd = {tea: round(price/121, 2) for tea, price in tea_prices_in_taka.items()}
print(tea_prices_in_usd)

squares_with_number = {number:number**2 for number in range(1,11)}
print(squares_with_number)

#number classification
number_classification = {number: "even" if number%2==0 else "odd" for number in range(1,11)}
print(number_classification)