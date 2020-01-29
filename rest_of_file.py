def audience_help(answers, current_line, question, table_line_length, choises, shuffled_line):
    
    play_sound("./msc/kozonseg.mp3", 0)
    for choise in [answers]:
        if choise == current_line[0]:
            if choise == a:
                a_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-a_percent))
                c_percent = random.randrange(0, (100-a_percent-b_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == b:
                b_percent = random.randrange(40, 89)
                a_percent = random.randrange(0, (100-b_percent))
                c_percent = random.randrange(0, (100-b_percent-a_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == c:
                c_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-c_percent))
                a_percent = random.randrange(0, (100-c_percent-b_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == d:
                d_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-d_percent))
                c_percent = random.randrange(0, (100-d_percent-b_percent))
                a_percent = 100-(d_percent+b_percent+c_percent)
            time.sleep(4)
            os.system('clear')
            for choise_ in [answers]:
                if choise == current_line[0]:
                    if choise_ == a:
                        fake_a_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100 - fake_a_percent))
                        fake_c_percent = random.randrange(0, (100 - fake_a_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent + fake_b_percent + fake_c_percent)
                    if choise_ == b:
                        fake_b_percent = random.randrange(40, 89)
                        fake_a_percent = random.randrange(0, (100 - fake_b_percent))
                        fake_c_percent = random.randrange(0, (100 - fake_b_percent-fake_a_percent))
                        fake_d_percent = 100 - (fake_a_percent+fake_b_percent + fake_c_percent)
                    if choise_ == c:
                        fake_c_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_c_percent))
                        fake_a_percent = random.randrange(0, (100-fake_c_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_ == d:
                        fake_d_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_d_percent))
                        fake_c_percent = random.randrange(0, (100-fake_d_percent-fake_b_percent))
                        fake_a_percent = 100-(fake_d_percent+fake_b_percent+fake_c_percent)
                    if fake_a_percent+fake_b_percent+fake_c_percent+fake_d_percent != 100:
                        print("Sheibe")
                print("A:"+bg.blue+fake_a_percent*" "+" "+str(fake_a_percent)+"%"+"\n"+bg.rs+"B:"+bg.blue+fake_b_percent*" "+" "+str(fake_b_percent)+"%"+"\n"+bg.rs+"C:"+bg.blue+fake_c_percent*" "+" "+str(fake_c_percent)+"%"+"\n"+bg.rs+"D:"+bg.blue+fake_d_percent*" "+" "+str(fake_d_percent)+"%"+"\n"+bg.rs)
                time.sleep(4)
                os.system('clear')
                sys.stdout.write("\033[F")
            elems = [a_percent, b_percent, c_percent, d_percent]
            max_element = max(elems[0], elems[1], elems[2], elems[3])
            a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+a_percent*" "+bg.black+fg.rs+str(a_percent)}%')
            b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+b_percent*" "+bg.black+fg.rs+str(b_percent)}%')
            c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+c_percent*" "+bg.black+fg.rs+str(c_percent)}%')
            d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+d_percent*" "+bg.black+fg.rs+str(d_percent)}%')
            print((table_line_length+1)*" " + bg.black + (max_element+11)*"-" + bg.rs)
            print(a__+(((max_element)-a_percent)+3)*" "+"|"+bg.rs)
            time.sleep(1)
            print(b__+(((max_element)-b_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(c__+(((max_element)-c_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(d__+(((max_element)-d_percent)+3)*" "+"|"+bg.rs)
            print((table_line_length+1)*" "+bg.black+(max_element+11)*"-" + bg.rs)
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
        