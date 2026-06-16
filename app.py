print("learning python!")


def multiply(x): return x * 2


print(multiply(5))

# names = ["Charlie", "Alice", "Bob"]

# sorted_names = sorted(names, key=lambda name: len(name))

# print(sorted_names)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers))


words = ["hello", "world", "python"]

upper_words = map(lambda word: word.upper(), words)

print(list(upper_words))

players = [
    {"name": "Alice", "score": 45},
    {"name": "Bob", "score": 12},
    {"name": "Charlie", "score": 33}
]

lowest_player = min(players, key=lambda player: player["score"])

print(lowest_player)


prices = [10, 20, 30, 40, 50]

return_prices = map(lambda price: price * 1.10, prices)

print(list(return_prices))

words = ["crane", "hi", "apple", "ok", "piano"]

return_words = filter(lambda word: len(word) == 5, words)

print(list(return_words))


products = [
    {"name": "Apple", "price": 1.99},
    {"name": "Banana", "price": 0.50},
    {"name": "Cherry", "price": 3.99}
]

return_products = sorted(
    products, key=lambda product: product["price"], reverse=True)

print(list(return_products))


games = [
    {"player": "Alice", "attempts": 3},
    {"player": "Bob", "attempts": 6},
    {"player": "Charlie", "attempts": 1}
]

return_games = max(games, key=lambda game: game["attempts"])

print(return_games)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

return_numbers = filter((lambda number: number % 2 == 0)
                        (lambda number: number * 2), numbers)

print(list(return_numbers))
