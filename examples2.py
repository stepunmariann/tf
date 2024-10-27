from ton_fragment.usernames.usernames import Usernames
from ton_fragment.numbers.numbers import Numbers
from ton_fragment.numbers.number import Number

price_high_to_low_auction_numbers = Numbers('auction')
print(price_high_to_low_auction_numbers.result)

price_low_to_high_auction_numbers = Numbers('auction', 'price_asc')
print(price_low_to_high_auction_numbers.result)

listed_auction_numbers = Numbers('auction', 'listed')
print(listed_auction_numbers.result)

ending_auction_numbers = Numbers('auction', 'ending')
print(ending_auction_numbers.result)

price_high_to_low_sold_numbers = Numbers('sold')
print(price_high_to_low_sold_numbers.result)

price_low_to_high_sold_numbers = Numbers('sold', 'price_asc')
print(price_low_to_high_sold_numbers.result)

listed_sold_numbers = Numbers('sold', 'listed')
print(listed_sold_numbers.result)

ending_sold_numbers = Numbers('sold', 'ending')
print(ending_sold_numbers.result)

price_high_to_low_sale_numbers = Numbers('sale')
print(price_high_to_low_sale_numbers.result)

price_low_to_high_sale_numbers = Numbers('sale', 'price_asc')
print(price_low_to_high_sale_numbers.result)

