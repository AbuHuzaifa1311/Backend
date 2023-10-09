# x ="huzaifa"
# y =(huz)
# print(" ".join(["huzaifa,huz"]))

# new_list = "This is another example"
# print(new_list.split('a'))

# name = input("Enter a name: ")
# number = len(name) *3
# print("Hello {number}, your lucky number is {name}".format (name=name,number=number))
# price = 7.5
# with_tax = price * 1.09
# print(price,with_tax)
# print("Base price: ${:.2f},with tax: ${:.2f}".format(price,with_tax))

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))
