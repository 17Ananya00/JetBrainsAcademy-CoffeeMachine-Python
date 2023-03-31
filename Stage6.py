pre_water = 400
pre_milk = 540
pre_beans = 120
pre_cups = 9
pre_money = 550
running = True
while running:
    print("Write action (buy, fill, take, remaining, exit):")

    action = input();
    if action == "exit":
        running = False
    elif action == "take":
        print("I gave you $" + str(pre_money))
        pre_money = 0
    elif action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        command = input()
        if command == "1":
            esp_water = 250
            esp_beans = 16
            esp_money = 4
            esp_cup = 1
            if pre_water > esp_water and pre_beans > esp_beans and pre_cups > esp_cup:
                print("I have enough resources, making you a coffee!")
                pre_water = pre_water - esp_water
                pre_beans = pre_beans - esp_beans
                pre_cups = pre_cups - 1
                pre_money = pre_money + esp_money
            else:
                if pre_water < esp_water:
                    print("Sorry, not enough water!")
                elif esp_beans > pre_beans:
                    print("Sorry, not enough beans!")
                elif esp_cup > pre_cups:
                    print("Sorry, not enough cups!")

        elif command == "2":
            lat_water = 350
            lat_milk = 75
            lat_beans = 20
            lat_money = 7
            if pre_water > lat_water and pre_milk > lat_milk and pre_beans > lat_beans and pre_cups > 1:
                print("I have enough resources, making you a coffee!")
                pre_water = pre_water - lat_water
                pre_milk = pre_milk - lat_milk
                pre_beans = pre_beans - lat_beans
                pre_cups = pre_cups - 1
                pre_money = pre_money + lat_money
            else:
                if pre_water < lat_water:
                    print("Sorry, not enough water!")
                    pre_water = pre_water
                elif pre_milk < lat_milk:
                    print("Sorry, not enough milk!")
                    pre_milk = pre_milk
                elif pre_beans < lat_beans:
                    print("Sorry, not enough beans!")
                    pre_beans = pre_beans
                elif pre_cups < 1:
                    print("Sorry, not enough cups!")
                    pre_beans = pre_beans
        elif command == "3":
            cap_milk = 100
            cap_water = 200
            cap_beans = 12
            cap_money = 6
            if pre_milk > cap_milk and pre_water > cap_water and pre_beans > cap_beans and pre_cups > 1:
                print("I have enough resources, making you a coffee!")

            else:
                if pre_milk < cap_milk:
                    print("Sorry, not enough milk!")
                elif pre_water < cap_water:
                    print("Sorry, not enough water!")
                elif pre_beans < cap_beans:
                    print("Sorry, not enough beans!")
                elif pre_cups < 1:
                    print("Sorry, not enough cups!")
            pre_water = pre_water - cap_water
            pre_milk = pre_milk - cap_milk
            pre_beans = pre_beans - cap_beans
            pre_cups = pre_cups - 1
            pre_money = pre_money + cap_money
        elif command == "back":
            continue


    elif action == "fill":
        print("Write how many ml of water you want to add:");
        add_water = int(input())
        print("Write how many ml of milk you want to add:");
        add_milk = int(input())
        print("Write how many grams of coffee beans you want to add:");
        add_beans = int(input())
        print("Write how many disposable cups of coffee you want to add:");
        add_cups = int(input())
        pre_water = pre_water + add_water
        pre_milk = pre_milk + add_milk
        pre_beans = pre_beans + add_beans
        pre_cups = pre_cups + add_cups

    elif action == "remaining":
        print("The coffee machine has:")
        print(str(pre_water) + " ml of water")
        print(str(pre_milk) + " ml of milk")
        print(str(pre_beans) + " g of beans")
        print(str(pre_cups) + " disposable cups")
        print("$" + str(pre_money) + " of money")

