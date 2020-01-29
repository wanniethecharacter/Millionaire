from sty import Style, RgbFg, fg, bg
a=bg.black+"▏"+fg.orange+"3"+fg.rs+>+bg.rs
fg.orange=Style(RgbFg(148, 0, 211))
'\x1b[38;2;255;150;50m\x1b[40m◆ A: \x1b[39m297 meters  \x1b[49m'
'\x1b[38;2;255;150;50m\x1b[40m◆ A: \x1b[39m297 meters  \x1b[49m'
'\x1b[38;2;255;150;50m\x1b[40m◆ A: \x1b[39m297 meters  \x1b[49m'
'\x1b[38;2;255;150;50m\x1b[40m◆ A: \x1b[39m297 meters  \x1b[49m'
bg.orange=bg(255, 150, 50)
x1b='\x1b'
black_orange='[38;2;255;150;50m'
orange='[40m'
first_string="◆ A: "
orange2='[39m'
second_string="297 meters  "
záróakkord='[49m'
fg.orange = Style(RgbFg(255, 150, 50))






print(x1b+black_orange+x1b+orange+first_string+x1b+orange2+second_string+x1b+záróakkord)
print('\x1b[39m297 meters  \x1b[49m')
first_part_of_first_letter='\x1b[38;2;255;150;50m\x1b[40m'
second_part_of_first_letter='\x1b[39m'
last_part_of_first_letter='\x1b[49m'
print(first_part_of_first_letter+"A: "+second_part_of_first_letter)
mark_string='\x1b[38;2;255;150;50m\x1b[40m◆ A: \x1b[49m'
print('\x1b[38;2;255;150;50m\x1b[40m'+"◆ A: "+'\x1b[49m')
c=bg.black+fg.orange+"◆ A: "+bg.rs+fg.rs+bg.rs
d=bg.black+"297 meters"+bg.rs
print(c)
print(d)
print("ok")
""" '\x1b[40m\x1b[38;2;255;150;50m◆ A: \x1b[49m\x1b[39m\x1b[49m' c
'\x1b[40m297 meters\x1b[49m' d """
asd=bg.orange
mark="◆"
a=fg.black+" A: "+fg.rs
e="297 meters"+bg.rs   
print(e)
print(asd+mark+a+e)
'\x1b[48;2;255;150;50m'
'◆'
'\x1b[30m A: \x1b[39m'
'297 meters\x1b[49m'
s=bg.orange+"◆"+fg.black+" A: "+fg.rs+"297 meters"+bg.rs
print(bg.orange+"◆"+fg.black+" A: "+fg.rs+"297 meters"+bg.rs)
d=bg.green+"◆"+fg.black+" A: "+fg.rs+"297 meters"+bg.rs
print(bg.green+"◆"+fg.black+" A: "+fg.rs+"297 meters"+bg.rs)
print('\x1b[42m◆\x1b[30m A: \x1b[39m297 meters\x1b[49m')
