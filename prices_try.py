def válogatós_függvény(choise):
    percents= []
    percents.append(random.randrange(40, 89))
    percents.append(random.randrange(0, 100-percents[0]))
    percents.append(random.randrange(0, 100-percents[0]-percents[1]))
    percents.append(100-(percents[0]+percents[1]+percents[2]))
    if percents[0]+percents[1]+percents[2]+percents[3] != 100:
        print(" AUDIENCE HELP IS BROKEN!!!")
    return percents



def audience_help(a, b, c, d, current_line, question, table_line_length, choises, shuffled_line):
    play_sound("./msc/kozonseg.mp3", 0)
    this_list=[a, b, c, d]
    for choise in this_list:
        if choise == current_line[0]:
            index_of_choise=this_list.index(choise)
            percents=válogatós_függvény(choise)
            os.system('clear')
            for choise_ in [a, b, c, d]:
                if choise == current_line[0]:
                    if choise_ == a:
                        fake_a_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_a_percent))
                        fake_c_percent = random.randrange(0, (100-fake_a_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent + fake_b_percent + fake_c_percent)
                    if choise_ == b:
                        fake_b_percent = random.randrange(40, 89)
                        fake_a_percent = random.randrange(0, (100-fake_b_percent))
                        fake_c_percent = random.randrange(0, (100-fake_b_percent-fake_a_percent))
                        fake_d_percent = 100-(fake_a_percent+fake_b_percent+fake_c_percent)
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
                time.sleep(1)
                os.system('clear')
                sys.stdout.write("\033[F")
            a_percent=0
            b_percent=0
            c_percent=0
            d_percent=0
            elems = [a_percent, b_percent, c_percent, d_percent]
            print(current_line[0])
            print(choise)
            elems[index_of_choise]=percents[0]
            del elems[index_of_choise]
            elems[0]=percents[1]
            elems[1]=percents[2]
            elems[2]=percents[3]
            """  del elems[index_of_choise]
            percents[1]=random.choice(elems)
            del elems[(percents[1])]
            percents[2]=random.choice(elems)
            del elems[percents[2]]
            percents[3]=elems[0] """
            max_element = 30
            elem=["a","b","c","d"][index_of_choise]
            if ["a","b","c","d"][index_of_choise]=="a":
                a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+elems[0]*" "+bg.black+fg.rs+str(elems[0])}%')
                b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+elems[1]*" "+bg.black+fg.rs+str(elems[0])}%')
                c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+elems[2]*" "+bg.black+fg.rs+str(elems[0])}%')
                d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+elems[3]*" "+bg.black+fg.rs+str(elems[0])}%')

            if ["a","b","c","d"][index_of_choise]=="b":
                b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+elems[0]*" "+bg.black+fg.rs+str(elems[0])}%')
                a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+elems[1]*" "+bg.black+fg.rs+str(elems[0])}%')
                c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+elems[2]*" "+bg.black+fg.rs+str(elems[0])}%')
                d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+elems[3]*" "+bg.black+fg.rs+str(elems[0])}%')
            if ["a","b","c","d"][index_of_choise]=="c":
                c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+elems[0]*" "+bg.black+fg.rs+str(elems[0])}%')
                a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+elems[1]*" "+bg.black+fg.rs+str(elems[0])}%')
                b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+elems[2]*" "+bg.black+fg.rs+str(elems[0])}%')
                d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+elems[3]*" "+bg.black+fg.rs+str(elems[0])}%')
            if ["a","b","c","d"][index_of_choise]=="d":
                d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+elems[0]*" "+bg.black+fg.rs+str(elems[0])}%')
                b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+elems[1]*" "+bg.black+fg.rs+str(elems[0])}%')
                c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+elems[2]*" "+bg.black+fg.rs+str(elems[0])}%')
                a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+elems[3]*" "+bg.black+fg.rs+str(elems[0])}%')
            print((table_line_length+1)*" " + bg.black + (max_element+11)*"-" + bg.rs)
            print(a__+(((max_element)-a_percent)+3)*" "+"|"+bg.rs)
            time.sleep(1)
            print(b__+(((max_element)-b_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(c__+(((max_element)-c_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(d__+(((max_element)-d_percent)+3)*" "+"|"+bg.rs)
            print((table_line_length+1)*" "+bg.black+(max_element+11)*"-" + bg.rs)
            time.sleep(10)