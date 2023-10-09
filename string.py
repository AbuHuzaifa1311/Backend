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

# def to_celsius(x):
#     return (x-32)*5/9
# for x in range(0,101,10):
#     print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))
# fruits = ["pineapple", "Banana", "Apple", "Melon"]
# fruits.insert(0,"orange")
# print(fruits)
# fruits = ["pineapple", "Banana", "Apple", "Melon"]
# fruits.pop(2)
# 'Apple'
# print(fruits)
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - houes * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
  result = convert_seconds (5000)
 print(result)

