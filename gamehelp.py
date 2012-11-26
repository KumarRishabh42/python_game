from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP
import curses
def gamehelp():

        
	key=None
	initscr()
	welcome=newwin(200,200,0,0)
	welcome.erase()
	welcome.refresh()
#	key=welcome.getch()
	while(1):
#	        global welcome	
#	initscr()
#	key=welcome.getch()	
		curses.start_color()
		curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
		curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
		curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLUE)
#	welcome=newwin(100,100,0,0)
		welcome.bkgd(' ',curses.color_pair(2))
		welcome.addstr(0,0,'WELCOME TO HELP MENU')
		welcome.refresh()
#curses.flash()
		d=curses.color_pair(2)
		n=curses.A_NORMAL
#		curs_set(0)
		
		welcome.addstr(15,50,'USE ARROW KEYS TO MOVE THE ROBOT ',curses.color_pair(2))
		welcome.refresh()
		welcome.addstr(17,50,'USE P TO PAUSE AND ESC ANYTIME TO QUIT THE GAME',curses.color_pair(2))
		welcome.addstr(19,50,'USE OPTIONS TO MODIFY GAME',curses.color_pair(2))
		welcome.addstr(21,50,'COLLECT ALL CODES BEFORE GOING FOR BOMB TO WIN THE GAME',n)
		welcome.addstr(23,50,'IF ROBO COLLECTS THE BOMB BEFORE ALL CODES YOU LOOSE THE GAME',curses.color_pair(2))
		welcome.addstr(25,50,'PRESS Q TO GO BACK',curses.color_pair(3))
		welcome.addstr(27,50,'ENJOY THE GAME!!',curses.color_pair(3))
		welcome.addstr(29,50,'CREDITS RISHABH',curses.color_pair(3))
		if welcome.getch()==ord('q') or welcome.getch()==ord('Q'):
			break
		
					

