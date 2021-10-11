from nsetools import Nse
from pprint import pprint
from platform import python_version
nse = Nse()
print (nse)

print("1. For stock info            2. For all stock codes")
print("3. For index price           4. For index list")
print("5. For top gainers           6. For top losers")
print("7. For lot size              8. For advance decline")

num = int(input("Choose any number from above: "))

def stock_info():
    code = input("Enter The Stock Code of your Stock: ")
    if nse.is_valid_code(code) == True:
        pass
    else:
        print("Entered Stock code is invalid!")
    stock = nse.get_quote(code)
    pprint(stock)

def stock_code():
    stock_codes = nse.get_stock_codes()
    pprint(stock_codes)

def index_code():
    quote = input("Enter The Index Quote of your Stock: ")
    if nse.is_valid_index(quote) == True:
        pass
    else:
        print("Entered Stock code is invalid!")
    index_codes = nse.get_index_quote(quote)
    pprint(index_codes)

def index_lists():
    index_list = nse.get_index_list()
    pprint(index_list)

def top_gainer():
    top_gainers = nse.get_top_gainers()
    pprint(top_gainers)

def top_loser():
    top_losers = nse.get_top_losers()
    pprint(top_losers)

def lot_sizes():
    lot_size = nse.get_fno_lot_sizes()
    pprint(lot_size)

def adv_declines():
    adv_decline = nse.get_advances_declines()
    pprint(adv_decline)


if num == 1:
    stock_info()
elif num == 2:
    stock_code()
elif num == 3:
    index_code()
elif num == 4:
    index_lists()
elif num == 5:
    top_gainer()
elif num == 6:
    top_loser()
elif num == 7:
    lot_sizes()
elif num == 8:
    adv_declines()
else:
    print("Entered Number is not valid!")
