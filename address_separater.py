import sys
from datetime import datetime

name = ('akshat','dinesh','manibalan','mohan','senthil')
t_mark = ('70','75','80','90','34')
e_mark = ('79','73','89','89','100')
m_mark = ('7','71','88','90','78')
min_mark = 50
for name , t_mark , e_mark , m_mark in zip (name , t_mark , e_mark , m_mark) :
    print(name,':',t_mark,':',e_mark,':',m_mark)
    t_mark = int(t_mark)
    if t_mark <= min_mark :
        print('fail')
    else :
            print('pass')
    
    e_mark = int(e_mark)
    if e_mark <= min_mark :
        print('fail')
    else :
            print('pass')

    m_mark = int(m_mark)
    if m_mark <= min_mark :
        print('fail')
    else :
            print('pass')




