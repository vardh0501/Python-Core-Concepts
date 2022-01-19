###List Comprehension:
'''List comprehensions is a pythonic way of expressing a ‘for-loop’ that appends to a list in a single line of code.
It provides a concise way to create lists from other iterables

The first expression generates the element in the list where as the second expression generates "for" loop and the third expression 
evaluates the expression for every item in collection.

List comprehensions can also be used for mapping and filtering.

Why:
List comprehensions are also more declarative than loops, which means they’re easier to read and understand.
They can limit the number of lines used in your program.

Disadvantages:
They might make your code run more slowly or use more memory.'''


##Example 1:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

##Example 2: Using map method, create a regular list to calculate the price after tax for a list of transactions
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08
def get_price_with_tax(txn):
    return txn*(1+TAX_RATE)
final_prices = map(get_price_with_tax,txns)
print(list(final_prices))

##Example 3: Use the above code and write the logic in list comprehension
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08
def get_price_with_tax(txn):
    return txn*(1+TAX_RATE)
final_prices = [get_price_with_tax(i) for i in txns]
print(list(final_prices))
