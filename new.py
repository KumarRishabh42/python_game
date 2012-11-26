from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP,start_color
import curses
from random import randrange
initscr()
start_color()
curs_set(0)
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
win = newwin(30,80,5,5)
win.keypad(1)
win.nodelay(1)
win.border()


#def menu()
#	win.addstr(5,10,"level")
#	win.addstr(6,10,"robo size")
#	win.addstr(7,10,"number of codes")
#	win.addstr(8,10,"arena size")
#	level=["Beginner","Intermediate","PRO","INSANE"]
#	robo =["2X2","3X3","4X4","5X5"]
#	noofcodes=[3,4,5,6,7,8,9,10]
#	arenasize=["small","intermediate","large"]
#	x=win.getch()
#	while(x='\n'):
#		if(x==KEY_DOWN):

#win.addstr( "Hello world", curses.color_pair(3) )
#win.refresh()
#pad = curses.newpad(100, 100)
#pad.refresh( 0,0, 5,5, 20,75)
#win.addch(1,44,'O')
snake = [ [30,7]]#,[29,8],[28,7],[27,7],[26,7],[25,7] ]
key = KEY_RIGHT
print KEY_RIGHT
d=3
cOFd=[n for n in [[randrange(1,29,1),randrange(1,79,1)] for x in range(d) ] if n not in snake]
#print cOFd[0][1],cOFd[0][0]
for x in range(0,len(cOFd)):
	win.addch(cOFd[x][0],cOFd[x][1],'C')
win.addch(randrange(1,14,1),randrange(1,58,1),'B')
#print cOFd
count=0
flag=0

win.addch(snake[0][1],snake[0][0],'X')
while key != 27:
    win.addstr(0,32,' code point' + ' : '+str(count*10)+' ',curses.color_pair(1))
    win.timeout(180)#+ ( (len(snake)-6) % 10- (len(snake)-6) ) * 3 )
    getkey = win.getch()
    key = key if getkey==-1 else getkey
    
    
#   snake.insert(0,[snake[0][0]+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), snake[0][1]+(key==KEY_DOWN and 1 or key==KEY_UP and -1)])
    
    win.addch(snake[len(snake)-1][1],snake[len(snake)-1][0],' ')
    #print win.inch(snake[0][1],snake[0][0])
    if win.inch(snake[0][1],snake[0][0]) & 255 == 32: 
	win.addch(snake[0][1],snake[0][0],'X')
	snake.pop()
    
    elif win.inch(snake[0][1],snake[0][0]) & 255 == ord('C'):  
 	win.addch(snake[0][1],snake[0][0],'X')
	snake.pop()
	count=count+1       
#	c = [n for n in [[randrange(1,58,1),randrange(1,14,1)] for x in range(len(snake))] if n not in snake]
#	print c
#       win.addch(c == [] and 4 or c[0][1],c == [] and 44 or c[0][0],'C')
    elif count!=d and win.inch(snake[0][1],snake[0][0]) & 255 == ord('B'):
	    flag=0
	    break
    elif count==d and win.inch(snake[0][1],snake[0][0]) & 255 == ord('B'):
	    flag=1
	    break
    else:
	flag=0
	break

endwin()
if flag==1:
	print "Mission successful"
	print "Number of codes collected",str(count),"and your score is",str(count*10)
	print "new snake.py","(by Kumar Rishabh)","thanks for playing"
else:
	print "Mission fucked"
	print "Number of codes collected",str(count),"and your score is",str(count*10)
	print "new snake.py","(by Kumar Rishabh)","thanks for playing anyway"
#print '\n  Snake.PY (by Kumar Rishabh),\, n  Thanks for playing, your score: '+str(len(snake)-7)+'\n'
