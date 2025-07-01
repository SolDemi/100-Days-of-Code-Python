from art import logo

print(logo)

exist_other = "y"
name_price = {}

while exist_other == "yes" or exist_other == "y":
    name = input("What is your name? \n")
    price = int(input("How many dollars will you bid? \n$"))
    name_price[name] = price
    exist_other = input("Is someone else want to bid?\n")
    if exist_other != "yes" and exist_other != "y":
        max_price = 0
        max_name = ""
        for key,value in name_price.items():
            if value > max_price:
                max_price = value
                max_name = key
        print(f"出价最高的人是：{max_name}，出价${max_price}")
