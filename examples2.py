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

 
 
Mon Oct 28 04:44:38 UTC 2024
 
 
Tue Oct 29 04:43:31 UTC 2024
 
 
Wed Oct 30 04:43:56 UTC 2024
 
 
Thu Oct 31 04:44:20 UTC 2024
 
 
Fri Nov  1 04:43:48 UTC 2024
