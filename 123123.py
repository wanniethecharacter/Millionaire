
""" shuffled_line = ["14343", "1212", "334343", "343434"]
table_line_length = len(
    shuffled_line[0])+len(shuffled_line[1])+len(shuffled_line[2])+len(shuffled_line[3])
upper_line_first_second_choise = "  "+"/"+len(shuffled_line[0])*"‾"+"\\"+(table_line_length-(
    len(shuffled_line[0])+len(shuffled_line[1])))*" "+"/"+(len(shuffled_line[1]))*"‾"+"\\"
under_line_first_second_choise = "  "+"\\"+len(shuffled_line[0]*"_"+"/"(table_line_length-(
    len(shuffled_line[0])+len(shuffled_line[1])))*" "+"\\"+(len(shuffled_line[1]))*"_"+"/"
upper_line_third_fourth_choise = "  "+"/"+len(shuffled_line[2])*"‾"+"\\"(table_line_length-(
    len(shuffled_line[2])+len(shuffled_line[3])))*" "+"/"+len(shuffled_line[3])*"‾"+"\\"
under_line_third_fourth_choise = "  "+"\\"+len(shuffled_line[2])*"_"+"/"(table_line_length-(
    len(shuffled_line[2])+len(shuffled_line[3])))*" "+"\\"+(len(shuffled_line[3]))*"_"+"/"

print(upper_line_first_second_choise)
print(under_line_first_second_choise)
print(upper_line_third_fourth_choise)
print(under_line_third_fourth_choise) """
""" word=[123,345,567]
line_new = '%12s  %12s  %12s' % (word[0], word[1], word[2])
print(line_new)
 print(table_line_length*("‾"))
    print("-"+bg.black+"‹"+''.join(question).center((table_line_length), ' ')+"›"+bg.rs+"-")
    hossz=table_line_length//2
    lstr = "I love geeksforgeeks"
    print (lstr.ljust(40, '-')) 
    print("-"+bg.black+"‹"+''.join(shuffled_line[0]).ljust((hossz), ' ')+''.join(shuffled_line[1]).rjust((hossz), ' ')+"›"+bg.rs+"-")
    print("-"+bg.black+"‹"+''.join(question).ljust((table_line_length), ' ')+"›"+bg.rs+"-")

    print('   '+'{:<15.5}  {:>15.5}'.format(shuffled_line[0], shuffled_line[1]))
    print('   '+'{:<15.5}  {:>15.5}'.format(shuffled_line[1], shuffled_line[2]))
    

    print(table_line_length*("‾"))
    print("-"+bg.black+"‹"+''.join(question).center((table_line_length), ' ')+"›"+bg.rs+"-")
    hossz=table_line_length//2
    print (shuffled_line[0].ljust(hossz, '-')+shuffled_line[1].ljust(hossz, '-')) 
    print("-"+bg.black+"‹"+''.join(shuffled_line[0]).ljust((hossz), '-')+''.join(shuffled_line[1]).rjust((hossz), '-')+"›"+bg.rs+"-")
    print("-"+bg.black+"‹"+''.join(question).ljust((table_line_length), '-')+"›"+bg.rs+"-")
    print("{0:.<20} {1:.>20} {2:.^20} ".format("Product", "Price", "Sum"))

    print('{:<45} {:<:<} {:>15}'.format(shuffled_line[0],"-", shuffled_line[1],))
    print('{:<45} {} {:>15}'.format(shuffled_line[1],"-", shuffled_line[2]))
    #{:<15}{:^10}{:>15} """
""" from stringcolor import * 

# a few examples without background colors.   
# for color names see CLI usage below. 

print(len("here we go"))
mystring_= "here we go"
mystring=str(cs("here we go", "orchid"))
print(len(mystring))
cs("here we go", "orchid")
print(len(mystring_))   
print(cs(mystring_, "#ffff87"))   

# bold and underline also available.  
print(cs("purple number 4, bold", "purple4").bold())  
print(cs("blue, underlined", "blue").underline())  
print(bold("bold AND underlined!").underline().cs("red", "gold"))
print(underline("the bottom line."))
print()

# yellow text with a red background.   
# color names, hex values, and ansi numbers will work.   
print(cs("warning!", "yellow", "#ff0000")) 
print()

# concat
print(cs("wild", "pink")+" stuff")
print("nothing "+cs("something", "DarkViolet2", "lightgrey6"))
print()

# use any working rgb or hex values.
# it will find the closest color available.
print(cs("this will show up red", "#ff0009"))
print(cs("so will this", "rgb(254, 0, 1)"))
print()

# use with format and f-strings
print(f"this is a test {cs('to check formatting with f-strings', 'yellow', 'grey').bold().underline()}")
print("this is a test {}".format(cs('to check the format function', 'purple', 'lightgrey11').bold().underline()))
 """
""" print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
CWHITE  = '\33[107m'
CEND = '\033[0m'
print(CWHITE+"HI" + CEND)
tzrj="HI"
trzl=CWHITE+"HI" + CEND
print(len(tzrj))
print(len(trzl)) """
def colorize(token, bold_and_al='', fg_color='', bg_color=''):
    prefix = '\x1b['
    suffix = 'm'
    reset = '\x1b[0m'

    return '\x1b[' + bold_and_al + ";" + fg_color + ";" + bg_color + "m" + token + reset


a = 'thisisjustadummystringfortestingpurposes'
print(colorize(a, bold_and_al='1', fg_color='34', bg_color='42'))

print(''.join([colorize(a[:5], bold_and_al='1', fg_color='', bg_color='\33[38m'), a[5:10], colorize(a[10:], bold_and_al='1', fg_color='', bg_color='44')]))
print(len(a))

""" x = 0
for i in range(24):
  colors = ""
  for j in range(5):
    code = str(x+j)
    colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
  print(colors)
  x=x+5 """
""" class colors:
    '''Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
 """
class Stuff():
    def __init__(self):
         self.str = "maybach"
    def __len__(self):
         return 9

s = Stuff()
print(len(s))
class Stuff():
        def __init__(self):
            self.str = choises[0]
        def color(self):
            self.color="orange"
        def __len__(self):
        
            return len(self)
    class Stuff_():
        def __init__(self):
            self.str=choises[1]
            
        def __len__(self):
            return len(self)
    class Stuffx():
        def __init__(self):
            self.str=choises[2]
        def __len__(self):
            return len(self)
    class Stuffs():
        def __init__(self):
            self.str=choises[3]
        def __len__(self):
            return len(self)
    s = Stuff()
    s_ = Stuff_()
    sx = Stuffx()
    ss=Stuffs()
    stuff_list=[s,s_,sx,ss]
    for character in range(4):
        spaces_up[character]=len(stuff_list[character])*"‾"
        spaces_down[character]=len(stuff_list[character])*"_"
    print(spaces_down[0].ljust((hossz), ' ')+spaces_down[1].rjust((hossz), ' ')+"›")
    print("-"+"‹"+s.str.ljust((hossz), '-')+s_.str.rjust((hossz), '-')+"›"+"-")#
    print(spaces_up[0].ljust((hossz), ' ')+spaces_up[1].rjust((hossz), ' ')+"›")
    print(spaces_down[2].ljust((hossz), ' ')+spaces_down[3].rjust((hossz), ' ')+"›")
    print("-"+"‹"+sx.str.ljust((hossz), '-')+ss.str.rjust((hossz), '-')+"›"+"-")#
    print(spaces_up[2].ljust((hossz), ' ')+spaces_up[3].rjust((hossz), ' ')+"›")



