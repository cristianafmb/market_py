from typing import List, Dict
from time import sleep

from models.producto import Product
from utils.helper import convert_float_to_str

products: List[Product] = []
cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

'''
@return: None
main menu with list all options:
add product, list products, buy product, see shopping cart, close tab, out
'''
def menu() -> None:
    print('================================')
    print('========== Welcome =============')
    print('================================')

    print('Select one option: ')
    print('1 - Register product ')
    print('2 - Show all products in the shop')
    print('3 - Buy product')
    print('4 - Show Cart')
    print('5 - Close order')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        show_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        show_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Come back anytime!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()

'''
@return: None
add product into product's list with name and price
'''
def register_product() -> None:
    print('Register product')
    print('=======================')

    name: str = input("Product's name: ")
    price: float = float(input("Product's price: "))

    product: Product = Product(name, price)

    products.append(product)

    print(f'Product {product.name} was registered with success!')
    sleep(2)
    menu()

'''
@return: None
list products in product's list
'''
def show_products() -> None:
    if len(products) > 0 :
        print('List:')
        print('================================')
        for product in products:
            print(product)
            print('----------------------------')
            sleep(1)
    else:
        print('There are no registered products yet.')

    sleep(2)
    menu()

'''
@return: None
buy product - add product to cart by his code
Check if product exists in product's list
If there is not a product with that code, print a string with error
After check cart's length, if there is something then check if product is there
If true add one more to cart, if not add for the first time to cart
Give just two seconds after this checks and then show menu again
'''
def buy_product() -> None:
    if len(products) > 0:
        print('Enter the code of the product you want to add to the cart: ')
        print('-------------------------------------------------------------')
        print('=================== Available Products ====================')
        for product in products:
            print(product)
            print('----------------------------------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = search_by_code(code)

        if product:
            if len(cart) > 0:
                in_cart: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print((f'Product {product.name} now has {quant+1} units in cart.'))
                        in_cart = True
                        sleep(2)
                        menu()
                if not in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'Product {product.name} has been added to cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'Product {product.name} has been added to cart.')
                sleep(2)
                menu()
        else:
            print(f'Product with code {code} was not found.')
            sleep(2)
            menu()
    else:
        print('There are no products to sell yet.')

    sleep(2)
    menu()

'''
@return: None
show in screen all products in cart with their respective quantities,
then display the menu again
'''
def show_cart() -> None:
    if len(cart) > 0:
        print('Products in cart:')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('--------------------------')
                sleep(1)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()

'''
@return: None
close tab - sum of all objects in cart and print in the screen
'''
def close_order() -> None:
    if len(cart) > 0:
        total: float = 0

        print('Cart Products')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total += data[0].price * data[1]
                print('------------------------------')
                sleep(1)
        print(f'Your bill is {convert_float_to_str(total)}€.')
        print('Came back anytime!')
        cart.clear()
        sleep(5)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()

'''
@code: receive an code to look for
@return: Product with that code
Search product by code
'''
def search_by_code(code: int) -> Product:
    p: Product = None

    for product in products:

        if product.code == code:
            p = product
    return p

if __name__ == '__main__':
    main()