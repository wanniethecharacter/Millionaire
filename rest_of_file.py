"""     """ print(answers)
    play_sound("./msc/jo valasz.mp3", 0)
    fg.green = Style(RgbFg(0, 255, 0))
    print(fg.green + "Well done!" + fg.rs)
    time.sleep(2)
    os.system('clear')
    else:
        print(answer)
        print()
        print(current_line[0])
        print(answers)
        play_sound("./msc/rossz valasz.mp3", 0)
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        sys.exit(0) """ """
   
    if answer == answers[0]:
        if answers[0] == current_line[0]:
            choises[0] = bg.green + fg.orange + '◆ A: ' + fg.rs + ''.join(answers[0]) + "  " + bg.black
        else:
            choises[0] = bg.red + fg.orange + '◆ A: ' + fg.rs + ''.join(answers[0]) + "  " + bg.black
    if answer == answers[1]:
        if answers[1] == current_line[0]:
            choises[1] = bg.green + fg.orange + '◆ B: ' + fg.rs + ''.join(answers[1]) + "  " + bg.black
        else:
            choises[1] = bg.red + fg.orange + '◆ B: ' + fg.rs + ''.join(answers[1]) + "  " + bg.black
    if answer == answers[2]:
        if answers[2] == current_line[0]:
            choises[2] = bg.green + fg.orange + '◆ C: ' + fg.rs + ''.join(answers[2]) + "  " + bg.black
        else:
            choises[2] = bg.red + fg.orange + '◆ C: ' + fg.rs + ''.join(answers[2]) + "  " + bg.black
    if answer == answers[3]:
        if answers[3] == current_line[0]:
            choises[3] = bg.green + fg.orange + '◆ D: ' + fg.rs + ''.join(answers[3]) + "  " + bg.black
        else:
            choises[3] = bg.red + fg.orange + '◆ D: ' + fg.rs + ''.join(answers[3]) + "  " + bg.black
    if answer != current_line[0]:
        for pos in [answers]:
            if pos == current_line[0]:
                if pos == answers[0]:
                    choises[0] = bg.green + choises[0] + "  " + bg.black
                if pos == answers[1]:
                    choises[1] = bg.green + choises[1] + "  " + bg.black
                if pos == answers[2]:
                    choises[2] = bg.green + choises[2] + "  " + bg.black
                if pos == answers[3]:
                    choises[3] = bg.green + choises[3] + "  " + bg.black
    time.sleep(1)
    os.system('clear')
    if answer == current_line[0]:
        play_sound("./msc/jo valasz.mp3", 0)
        fg.green = Style(RgbFg(0, 255, 0))
        print(fg.green + "Well done!" + fg.rs)
        time.sleep(2)
        os.system('clear')
    else:
        play_sound("./msc/rossz valasz.mp3", 0)
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        sys.exit(0)
        """   print("  "+bg.black+"/"+"‾"*(table_line_length)+"\\"+bg.rs)
    width = table_line_length
    print("-"+bg.black+"‹"+''.join(question).center((width), ' ')+"›"+bg.rs+"-")
    print("  "+bg.black+"\\"+"_"*(table_line_length)+"/"+bg.rs)
    upper_line_first_second_choise = "  "+bg.black+"/"+(len(shuffled_line[0])+5)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+21)))+bg.black+"/"+len(shuffled_line[1])*"‾"+"\\"+bg.rs
    under_line_first_second_choise = "  "+bg.black+"\\"+(len(shuffled_line[0])+5)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+21)))+bg.black+"\\"+len(shuffled_line[1])*"_"+"/"+bg.rs
    upper_line_third_fourth_choise = "  "+bg.black+"/"+(len(shuffled_line[3])+5)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+21)))+bg.black+"/"+len(shuffled_line[3])*"‾"+"\\"+bg.rs
    under_line_third_fourth_choise = "  "+bg.black+"\\"+(len(shuffled_line[3])+5)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+21)))+bg.black+"\\"+len(shuffled_line[3])*"_"+"/"+bg.rs
    print(upper_line_first_second_choise)
    print("-"+bg.black+"‹ " + choises[0] + " ›" + bg.rs + ("-"*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+20))) + bg.black+"‹ "+choises[1] + " ›"+bg.rs+"-")
    print(under_line_first_second_choise)
    print(upper_line_third_fourth_choise)
    print("-"+bg.black+"‹ " + choises[2] + " ›" + bg.rs + ("-"*(table_line_length-(len(shuffled_line[1])+len(shuffled_line[3])+20)))+bg.black+"‹ "+choises[3] + " ›"+bg.rs+"-")
    print(under_line_third_fourth_choise)"""