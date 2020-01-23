def audience_help(a, b, c, d, current_line, question, table_line_length, choises, shuffled_line):
    play_sound("./msc/kozonseg.mp3", 0)
    this_list=[a, b, c, d]
    for choise in this_list:
        if choise == current_line[0]:
            index_of_choise=this_list.index(choise)
            os.system('clear')
            percents=válogatós_függvény()
            index=index_of_choise
            a_percent=0
            b_percent=0
            c_percent=0
            d_percent=0
            mylist=[a_percent,b_percent,c_percent,d_percent]
            counter=1
            bet_lista=["A","B","C","D"]
            for each in range(len(mylist)):
                if mylist[each]==mylist[index]:
                    mylist[each]=percents[0]
                if mylist[each]!=mylist[index]:
                    mylist[each]=percents[counter]
                if counter < 3: 
                    counter+=1

            if mylist[0]+ mylist[1]+ mylist[2]+ mylist[3]!=100:
                print("FUCK")
            print(mylist)
            first_print=(bet_lista[index_of_choise] + str(mylist[0]))
            del bet_lista[index_of_choise]
            second_print=(bet_lista[0] + str(mylist[1]))
            third_print=(bet_lista[1] + str(mylist[2]))
            fourth_print=(bet_lista[2] + str(mylist[3]))
            for betu in ["A","B","C","D"]:
                for prints in [first_print,second_print,third_print,fourth_print]:
                    if betu in prints:
                        print(prints)