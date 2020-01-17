prices=["5.000 Ft","10.000 Ft", "25.000 Ft","50.000 Ft","100.000 Ft","200.000 Ft","300.000 Ft","500.000 Ft","800.000 Ft","1.500.000 Ft","3.000.000 Ft","5.000.000 Ft","10.000.000 Ft","20.000.000 Ft","40.000.000 Ft"]
counter=0
for i in range(len(prices)):
    for round_ in range(len(prices)):
        if counter==round_:
            print(prices[counter])
        if counter == 5:
            print("You have guaranteed 100.000 Ft" )
        elif counter == 10:
            print("You have guaranteed 1.500.000 Ft" )
        elif counter == 15:
            print("Congratulations!\nYou've just won the unbelivable 40.000.000 Ft\n"+"You became the new Millionaire!!!" )
        counter += 1 