from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP
from random import randrange
import curses
import gamehelp
initscr()
welcome=newwin(200,200,0,0)

#def gamehelp1():

        
#	key=None
#	initscr()
#	global welcome
#	welcome.erase()
#	welcome.refresh()
#	key=welcome.getch()
#	while(1):
#	        global welcome	
#	initscr()
#	key=welcome.getch()	
#		curses.start_color()
#		curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
#		curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
#		curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLUE)
#	welcome=newwin(100,100,0,0)
#		welcome.bkgd(' ',curses.color_pair(2))
#		welcome.addstr(0,0,'WELCOME TO HELP MENU')
#		welcome.refresh()
#curses.flash()
#		d=curses.color_pair(2)
#		n=curses.A_NORMAL
#		curs_set(0)
#		
#		welcome.addstr(15,50,'USE ARROW KEYS TO MOVE THE ROBOT ',curses.color_pair(2))
#		welcome.refresh()
#		welcome.addstr(17,50,'USE P TO PAUSE AND ESC ANYTIME TO QUIT THE GAME',curses.color_pair(2))
#		welcome.addstr(19,50,'USE OPTIONS TO MODIFY GAME',curses.color_pair(2))
#		welcome.addstr(21,50,'COLLECT ALL CODES BEFORE GOING FOR BOMB TO WIN THE GAME',n)
#		welcome.addstr(23,50,'IF ROBO COLLECTS THE BOMB BEFORE ALL CODES YOU LOOSE THE GAME',curses.color_pair(2))
#		welcome.addstr(25,50,'PRESS Q TO GO BACK',curses.color_pair(3))
#		welcome.addstr(27,50,'ENJOY THE GAME!!',curses.color_pair(3))
#		welcome.addstr(29,50,'CREDITS RISHABH',curses.color_pair(3))
#		if welcome.getch()==ord('q') or welcome.getch()==ord('Q'):
#			break
		
#	welcome1()				

arrofcodes=[' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10']	
codes=10
arroflevels=["Rookie      ","Intermediate","Pro         "]
levelx=1
arrofspeed=["slow  ","fast  ","medium","insane "]
speed=1
arrofrobo=["2X2","3X3","4X4"]
robonumber=1
countturn=1
def options():
	global arrofcodes
	global levelx
	global arrofspeed
	global codes
	global arroflevels
	global speed
	global arrofrobo
	global robonumber
	global welcome
	global countturn
	
	welcome=newwin(200,200,0,0)
	welcome.erase()
	welcome.refresh()
	
#	key=None
	welcome.addstr(19,80,arroflevels[0])
	welcome.addstr(21,80,str(arrofcodes[0]))
	welcome.addstr(23,80,arrofspeed[0])
	welcome.addstr(25,80,arrofrobo[0])
	
	def mainfunc():
	     key=0
	     global countturn
#	     countturn=1
	     
	     while(key & 255!=10):
		
		initscr()
		
		curses.start_color()
		curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
		curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
		curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLUE)
	        welcome.bkgd(' ',curses.color_pair(1))
#curses.flash()
		d=curses.color_pair(2)
		n=curses.A_NORMAL
		curs_set(0)
		welcome.keypad(1)
#		print countturn	
		#welcome.addstr(1,1,str(countturn))
		welcome.addstr(17,60,'PLEASE SELECT AN OPTION',curses.color_pair(2))
		if countturn==1:
			welcome.addstr(19,60,'LEVEL',d)
		else:
			welcome.addstr(19,60,'LEVEL',n)
		if countturn==2:
			welcome.addstr(21,60,'NUMBER OF CODES',d)
		else:
			welcome.addstr(21,60,'NUMBER OF CODES',n)
		if countturn==3:
			welcome.addstr(23,60,'SPEED',d)
		else:
                	welcome.addstr(23,60,'SPEED',n)
		if countturn==4:
			welcome.addstr(25,60,'ROBO SIZE',d)
		else:
			welcome.addstr(25,60,'ROBO SIZE',n)
		if countturn==5:
			welcome.addstr(27,60,'BACK',d)
		else:
			welcome.addstr(27,60,'BACK',n)

        
		key=welcome.getch()

		if key==KEY_DOWN:
			countturn=countturn+1
			if(countturn>5):
				countturn=1
				
		if key==KEY_UP:
			countturn=countturn-1
			if(countturn==0):
				countturn=5
	        
#y=None

#		 while(y!='\n'):
#			if key==KEY_UP:
#				countcodes=countcodes-1
#				if(countcodes==-1):
#					countcodes=7
		
#	   			welcome.addch(21,70,lofd[countcodes])
#				welcome.refresh()
				
	mainfunc()
	if countturn==5:
			welcome.erase()
	    		welcome.refresh()
	    		welcome1()

		
	while countturn!=5:
		if(countturn==1):
			y=0
			x=0
			while(y & 255!=10 ):
				welcome.addstr(19,80,arroflevels[x])
				#welcome.addstr(19,95,str(countturn))
				levelx=x
				#welcome.addstr(2,2,str(levelx))
				welcome.refresh()
				y=welcome.getch()
			
				if y==KEY_DOWN:
					x=x+1
					if(x==3):
						x=0
				if y==KEY_UP:
			  		x=x-1
			  		if(x<0):
						x=2
			welcome.refresh()	
			mainfunc()
	        if (countturn==2):
			y=0
			x=0
			while(y & 255 != 10):
				welcome.addstr(21,80,arrofcodes[x])
				codes=int(arrofcodes[x])
				#welcome.addstr(21,95,str(countturn))
				welcome.refresh()
				y=welcome.getch()
				if y==KEY_DOWN:
					x=x+1
					if(x==10):
						x=0
				elif y==KEY_UP:
					x=x-1
					if(x<0):
						x=9
			welcome.refresh()
			mainfunc()
		if countturn==3:
	    		y=0
	    		x=0
	    		while(y & 255!= 10):
				welcome.addstr(23,80,arrofspeed[x])
				speed=x
				welcome.refresh()
				y=welcome.getch()

				if y==KEY_DOWN:
					x=x+1
					if(x==4):
						x=0
				elif y==KEY_UP:
			  		x=x-1
			  		if x<0:
			  			x=3

			welcome.refresh()
			mainfunc()

		if countturn==4:
			y=0
			x=0
			while(y & 255 != 10):
				welcome.addstr(25,80,arrofrobo[x])
				robonumber=x
#	welcome.addstr(25,90,str(robonumber))
				welcome.refresh()
				y=welcome.getch()
				if y==KEY_DOWN:
					x=x+1
					if(x==3):
						x=0
				elif y==KEY_UP:
			  		x=x-1
			  		if x<0:
			  			x=2
			welcome.refresh()
			mainfunc()
		if countturn==5:
	    		welcome.erase()
	    		welcome.refresh()
	    		welcome1()
#mainfunc()
#if key==ord('c') or key==ord('C'):
#			return 
#		elif key==ord('e') or key==ord('E'):
#			endwin()
#			exit()



 
	
speedarr=[180,140,100,60]	

	
def welcome1():
	global welcome
	welcome.erase()
	welcome.refresh()
	countturn=1
	key=0
#	global robo
#welcome.addstr(2,2,str(robo))

	while(key & 255!=10):
		
		initscr()
		
		curses.start_color()
		curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
		curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
		curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLUE)
	        welcome.bkgd(' ',curses.color_pair(1))
#curses.flash()
		d=curses.color_pair(2)
		n=curses.A_NORMAL
		curs_set(0)
		welcome.keypad(1)
		welcome.addstr(30,50,'copyright (Kumar Rishabh) ',curses.color_pair(3))
		welcome.addstr(32,50,'TO BE PUBLISHED UNDER GNU LICENSE ON GITHUB SOON',curses.color_pair(3))
		welcome.addstr(34,50,'WITH LOTS OF MODIFICATIONS',curses.color_pair(3))
		welcome.addstr(15,60,'WELCOME TO ROBO BOMB DEFUSER',n)
		welcome.addstr(17,60,'PLEASE SELECT AN OPTION',curses.color_pair(2))
		if countturn==1:
			welcome.addstr(19,60,'NEW GAME',d)
		else:
			welcome.addstr(19,60,'NEW GAME',n)
		if countturn==2:
			welcome.addstr(21,60,'HIGHSCORE',d)
		else:
			welcome.addstr(21,60,'HIGHSCORE',n)
		if countturn==3:
			welcome.addstr(23,60,'HELP',d)
		else:
                	welcome.addstr(23,60,'HELP',n)
		if countturn==4:
			welcome.addstr(25,60,'OPTIONS',d)
		else:
			welcome.addstr(25,60,'OPTIONS',n)
		if countturn==5:
			welcome.addstr(27,60,'EXIT',d)
		else:
			welcome.addstr(27,60,'EXIT',n)

        
		key=welcome.getch()
		if key==KEY_DOWN:
			countturn=countturn+1
			if(countturn>5):
				countturn=1
		if key==KEY_UP:
			countturn=countturn-1
			if(countturn==0):
				countturn=5
	if countturn==1:
	   	welcome.erase()
	   	welcome.refresh()
	   
	   	return
	if countturn==5:
	   	endwin()
	   	exit()
	if countturn==4:
	   	welcome.erase()
	   	welcome.refresh()
	   	
	   	options()
	if countturn==3:
	   	welcome.erase()
	   	welcome.refresh()
		
	   	gamehelp.gamehelp()
		welcome1()
	if countturn==2:
#welcome.erase()
	   	welcome.refresh()
		welcome.addstr(2,2,"High Score function not functional till now")		
#		endwin()

#if key==ord('c') or key==ord('C'):
#			return 
#		elif key==ord('e') or key==ord('E'):
#			endwin()
#			exit()


		


welcome1()	
welcome.erase()
welcome.refresh()
#gamehelp()
initscr()
curses.start_color()
curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_CYAN,curses.COLOR_BLACK)
curses.init_pair(5,curses.COLOR_BLACK,curses.COLOR_CYAN)
curs_set(0)
hnw=[[30,80],[40,90],[50,100]]
height=40
width=90
if levelx==0:
	height=hnw[0][0]
	width=hnw[0][1]
elif levelx==1:
	height=hnw[1][0]
	width=hnw[1][1]
elif levelx==2:
	height=hnw[2][0]
	width=hnw[2][1]

#win = newwin(30,80,5,5)
win=newwin(height,width,5,5)
#test= newwin(30,30,40,80)
#test.border()
#if levelx==1:
#	win.bkgd(' ',curses.color_pair(5))
#	curses.init_pair(2,curses.COLOR_RED,curses.COLOR_CYAN)
#	curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_CYAN)
#else:
win.bkgd(' ',curses.color_pair(1))

win.keypad(1)
win.nodelay(1)
win.border()
#win.addch(29,44,'O')





snake = [ [30,7],[30,6],[30,5],[30,4],[29,7],[29,6],[29,5],[29,4],[28,7],[28,6],[28,5],[28,4],[27,7],[27,6],[27,5],[27,4] ]
robocoord=[[30,7],[30,6],[29,7],[29,6]]
robomedcoord=[[30,7],[30,6],[30,5],[29,7],[29,6],[29,5],[28,7],[28,6],[28,5]]
key = KEY_RIGHT
#print KEY_RIGHT
d=codes
#win.addch(60,20,'T')
decision=0
cOFd=[n for n in [[randrange(1,height-1,1),randrange(1,width-1,1)] for x in range(d) ] if n not in snake]
#print cOFd[0][1],cOFd[0][0]
cOFo=[n for n in [[randrange(1,height-1,1),randrange(1,width-1,1)] for x in range(codes/2)] if n not in snake if n not in cOFd]
#for x in range(0,len(cOFd)):
#print cOFd
#	win.addch(cOFd[x][0],cOFd[x][1],'C',curses.color_pair(2))
#if levelx==1:
#	for x in range(0,len(cOFo)):
#		win.addch(cOFo[x][0],cOFo[x][1],'A',curses.color_pair(3))

posy=0
posx=0
#for i in xrange(0,height):
#	for j in xrange(0,width):
#	 	if win.inch(i,j)==ord('B'):
#	 		posy=i
#
#	 		posx=j
	 
#win.addstr(2,2,str(posy)+str(posx))
ancount=codes/2-1
antiscore=0              
class level:
	def __init__(self,height,width,levelx,count,ancount,antiscore,d):
		self.height=height
		self.width=width
		self.levelx=levelx
		self.ancount=ancount
		self.antiscore=antiscore
		self.count=count
		self.d=d
	def placecodes(self,win,cOFd):
		for x in range(0,len(cOFd)):
			win.addch(cOFd[x][0],cOFd[x][1],'C',curses.color_pair(3))
	def placebomb(self,win):
		
		win.addch(randrange(1,self.height-1,1),randrange(1,self.width-1,1),'B',curses.A_REVERSE)
	def placeobstacle(self,win,cOFo):
		for x in xrange(0,len(cOFo)):
			win.addch(cOFo[x][0],cOFo[x][1],'A',curses.color_pair(2))
	def inccount(self):
		self.count=self.count+1
	def decancount(self):
		self.ancount=self.ancount-1
	def incantiscore(self):
		self.antiscore=self.antiscore+1

      	def checksm(self,robocoord):
			
	    		global count
#			global robosmall
			
#			global robosmall2
#global levelx
			global antiscore
			global ancount
	    		status=0
			
	    		for i in xrange(0,len(robocoord)):
		    		if(win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('C')):
					    self.inccount()
					    # win.addch(5,5,count)
	    	    		elif(self.count==d and win.inch(robocoord[i][1],robocoord[i][0]) & 255 ==ord('B')):
			    		    status=1
					    return status
		    		elif(self.count!=d and win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('B')):
			    		    status=-1
	    				    return status				    
			
				elif(self.levelx==1 and win.inch(robocoord[i][1],robocoord[i][0]) & 255 ==ord('A') and self.ancount!=0):
					    self.decancount()
					    self.incantiscore()
					    
# win.addch(5,5,str(ancount))
				elif(self.levelx==1 and win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('A') and self.ancount==0):
					    status=-1
					    return status

	    		return status
	


count=0
a=level(height,width,levelx,count,ancount,antiscore,d)
a.placecodes(win,cOFd)
a.placebomb(win)
win.addstr(2,2,str(levelx))
if levelx==1:
	a.placeobstacle(win,cOFo)
#print cOFd
count=0
flag=0
decision=0
#status=0
#snake=map(lambda x:[x[0]+1,x[1]],snake)
#print snake
#for x in range(0,len(snake)):
#   win.addch(snake[x][1],snake[x][0],'X')
robo=['\\','|',']','/',' ','_','@','i',' ','_','@','i','/','|','[','\\']
robo2=['|','|',']','/',' ','_',' ','i',' ','_',' ','i','|','|','[','\\']
robo3=['|','|',']','/',' ','_','@',' ',' ','_','@',' ','|','|','[','\\']

robosmall=['@','/','@','\\']
robosmall1=[' ','/',' ','\\']
robomed=['\\','/','-',' ','R','@','/','\\','-']
robomed1=['|','/','>',' ','R','@','|','\\','-']
robomed2=['|','\\','>',' ','R','@','|','/','<']

def robomedfunc():
	global speed
	global speedarr
	global robomedcoord
	global key
	global robomed
	global flag
	global decision
	global count
	global robomed1
	global robomed2
	global height
	global width
	global levelx
	global codes
	global ancount
	global antiscore
	prev=None
	for i in xrange(0,len(robomedcoord)):
		win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed[i])

	countleft=0
	countright=0
	countup=0
	countdown=0
	while key != 27:

    		if(robomedcoord[0][0]==width-1 or robomedcoord[8][0]==0):
			flag=-1    
			break
    		elif(robomedcoord[0][1]==height-1 or robomedcoord[2][1]==0):
			flag=-1
			break
    		win.addstr(0,width/2-9,' code points' + ' : '+str(a.count*10-a.antiscore*10)+' ')
    		win.timeout(speedarr[speed]-count*10)#+ ( (len(snake)-6) % 10- (len(snake)-6) ) * 3 )
    		prev=key
		getkey = win.getch()
    		key = key if getkey==-1 else getkey

    		def check():
	    		global robomedcoord
	    		global count
			global robomed
			global robomed1
			global robomed2
			global ancount
			global levelx
			global antiscore
#		win.addstr(3,3,str(levelx))
	    		status=0
	    		for i in xrange(0,len(robomedcoord)):
		    		if(win.inch(robomedcoord[i][1],robomedcoord[i][0]) & 255 == ord('C')):
					    count=count+1
					    # win.addch(5,5,count)
	    	    		elif(count==d and win.inch(robomedcoord[i][1],robomedcoord[i][0]) & 255 ==ord('B')):
			    		    status=1
					    return status
		    		elif(count!=d and win.inch(robomedcoord[i][1],robomedcoord[i][0]) & 255 == ord('B')):
			    		    status=-1
	    				    return status				    
				elif(levelx==1 and win.inch(robomedcoord[i][1],robomedcoord[i][0]) & 255 ==ord('A') and ancount!=0):
					    ancount=ancount-1
					    antiscore=antiscore+1
					    
# win.addch(5,5,str(ancount))
				elif(levelx==1 and win.inch(robomedcoord[i][1],robomedcoord[i][0]) & 255 == ord('A') and ancount==0):
					    status=-1
					    return status
	    		return status
	

    		if(key==KEY_RIGHT):
			robomedcoord=map(lambda x:[x[0]+1,x[1]] , robomedcoord)
			

			decision=a.checksm(robomedcoord)
			if(decision==0):
		

				for i in xrange(0,len(robomedcoord)):
					if countright==0:
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed[i],curses.color_pair(2))
					elif countright==1:
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed1[i])
				for i in xrange(6,9):
					win.addch(robomedcoord[i][1],robomedcoord[i][0]-1,' ')
				if(countright==0):
					countright=1
				else:
				 	countright=0
        		else:
				break
    		elif(key==KEY_LEFT):
			robomedcoord=map(lambda x:[x[0]-1,x[1]],robomedcoord)
	
#	print snake
			decision=a.checksm(robomedcoord)
	
			if(decision==0):
#		for i in xrange(0,4):
#			win.addch(snake[i][1],snake[i][0]+1,' ')
#		for i in xrange(4,8):
#	 		win.addch(snake[i][1],snake[i][0],'X')
				for i in xrange(0,len(robomedcoord)):
					if countleft==1:
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed1[i])
						win.addch(robomedcoord[8][1],robomedcoord[8][0],'<')
						win.addch(robomedcoord[2][1],robomedcoord[2][0],'-')
					else:
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed[i],curses.color_pair(2))
				for i in xrange(0,3):
		 			win.addch(robomedcoord[i][1],robomedcoord[i][0]+1,' ')
				if(countleft==0):
					countleft=1
				else:
				 	countleft=0
			else:
				break
     
#snake.insert(0,[snake[0][0]+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), snake[0][1]+(key==KEY_DOWN and 1 or key==KEY_UP and -1)])
    
#    win.addch(snake[len(snake)-1][1],snake[len(snake)-1][0],' ')
    		elif(key==KEY_DOWN):
	    
	    
	    
	    		robomedcoord=map(lambda x:[x[0],x[1]+1],robomedcoord)
#	    	print snake
			decision=a.checksm(robomedcoord)
		
			if(decision==0):
				for i in xrange(0,len(robomedcoord)):
					if(countdown==0):
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed[i],curses.color_pair(2))
					else:
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed2[i])
	   			win.addch(robomedcoord[2][1]-1,robomedcoord[2][0],' ')
	    			win.addch(robomedcoord[5][1]-1,robomedcoord[5][0],' ')
	   			win.addch(robomedcoord[8][1]-1,robomedcoord[8][0],' ')
	   			if(countdown==0):
					countdown=1
				else:
				 	countdown=0
	    		else:
		    		break
    		elif(key==KEY_UP):
	    
	
	    
	    		robomedcoord=map(lambda x:[x[0],x[1]-1],robomedcoord)
#		print snake    	
			decision=a.checksm(robomedcoord)
		
			if(decision==0):
				for i in xrange(0,len(robomedcoord)):
					if(countup==0):
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed[i],curses.color_pair(2))
	    				elif(countup==1):
						win.addch(robomedcoord[i][1],robomedcoord[i][0],robomed2[i])
	    			win.addch(robomedcoord[0][1]+1,robomedcoord[0][0],' ')
	    			win.addch(robomedcoord[3][1]+1,robomedcoord[3][0],' ')
				win.addch(robomedcoord[6][1]+1,robomedcoord[6][0],' ')
				if(countup==0):
					countup=1
				else:
				 	countup=0
				
	    		else:
		    		break
	
	


		elif key == ord('p'):
			y=win.getch()
			while(y!=ord('p')):
				y=win.getch()
			key=prev
	
#	print snake






def robosmallfunc():
	global robocoord
	global key
	global robosmall
	global speed
	global speedarr
	global flag
	global decision
	global count
	global robsmall2
	global height
	global width
	global ancount
	countright=0
	countleft=0
	countup=0
	countdown=0
	prev=None

	for i in xrange(0,len(robocoord)):
		win.addch(robocoord[i][1],robocoord[i][0],robosmall[i])
        	
	
	while key != 27:

    		if(robocoord[0][0]==width-1 or robocoord[3][0]==0):
			flag=-1    
			break
    		elif(robocoord[0][1]==height-1 or robocoord[1][1]==0):
			flag=-1
			break
    		win.addstr(0,width/2-7,' code points' + ' : '+str(a.count*10-a.antiscore*10)+' ')
    		win.timeout(speedarr[speed]-count*10)#+ ( (len(snake)-6) % 10- (len(snake)-6) ) * 3 )
    		prev=key
		getkey = win.getch()
    		key = key if getkey==-1 else getkey

    		def check():
			global robocoord
	    		global count
			global robosmall
			global decision
			global robosmall2
			global levelx
			global antiscore
			global ancount
	    		status=0
			
	    		for i in xrange(0,len(robocoord)):
		    		if(win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('C')):
					    count=count+1
					    # win.addch(5,5,count)
	    	    		elif(count==d and win.inch(robocoord[i][1],robocoord[i][0]) & 255 ==ord('B')):
			    		    status=1
					    return status
		    		elif(count!=d and win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('B')):
			    		    status=-1
	    				    return status				    
			
				elif(levelx==1 and win.inch(robocoord[i][1],robocoord[i][0]) & 255 ==ord('A') and ancount!=0):
					    ancount=ancount-1
					    antiscore=antiscore+1
					    
# win.addch(5,5,str(ancount))
				elif(levelx==1 and win.inch(robocoord[i][1],robocoord[i][0]) & 255 == ord('A') and ancount==0):
					    status=-1
					    return status

	    		return status
	
		
			
			
		if(key==KEY_RIGHT):
			robocoord=map(lambda x:[x[0]+1,x[1]] , robocoord)
	

			decision=a.checksm(robocoord)
			if(decision==0):
		

				for i in xrange(0,len(robocoord)):
					if countright==0:
						win.addch(robocoord[i][1],robocoord[i][0],robosmall[i])
						win.addch(robocoord[0][1],robocoord[0][0],robosmall[0],curses.color_pair(2))
						win.addch(robocoord[2][1],robocoord[2][0],robosmall[2],curses.color_pair(2))
					else:
						win.addch(robocoord[i][1],robocoord[i][0],robosmall1[i])
				for i in xrange(2,4):
					win.addch(robocoord[i][1],robocoord[i][0]-1,' ')	
				if countright==0:
				 	countright=1
				else:
				 	countright=0

        		else:
				break
    		elif(key==KEY_LEFT):
			robocoord=map(lambda x:[x[0]-1,x[1]],robocoord)
	
#	print snake
			decision=a.checksm(robocoord)
	
			if(decision==0):
#		for i in xrange(0,4):
#			win.addch(snake[i][1],snake[i][0]+1,' ')
#		for i in xrange(4,8):
#	 		win.addch(snake[i][1],snake[i][0],'X')
				for i in xrange(0,len(robocoord)):
					if countleft==0:
						win.addch(robocoord[i][1],robocoord[i][0],robosmall[i])
						win.addch(robocoord[0][1],robocoord[0][0],robosmall[0],curses.color_pair(2))
					        win.addch(robocoord[2][1],robocoord[2][0],robosmall[2],curses.color_pair(2))
					else :
						win.addch(robocoord[i][1],robocoord[i][0],robosmall1[i])
				for i in xrange(0,2):
		 			win.addch(robocoord[i][1],robocoord[i][0]+1,' ')
				if countleft==0:
				  	countleft=1
				else:
				  	countleft=0
			else:
				break
     
#snake.insert(0,[snake[0][0]+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), snake[0][1]+(key==KEY_DOWN and 1 or key==KEY_UP and -1)])
    
#    win.addch(snake[len(snake)-1][1],snake[len(snake)-1][0],' ')
    		elif(key==KEY_DOWN):
	    
	    
	    
	    		robocoord=map(lambda x:[x[0],x[1]+1],robocoord)
#	    	print snake
			decision=a.checksm(robocoord)
		
			if(decision==0):
				

				for i in xrange(0,len(robocoord)):
					if countdown==0:

						win.addch(robocoord[i][1],robocoord[i][0],robosmall[i])
						win.addch(robocoord[0][1],robocoord[0][0],robosmall[0],curses.color_pair(2))
					        win.addch(robocoord[2][1],robocoord[2][0],robosmall[2],curses.color_pair(2))
					
					else:
						win.addch(robocoord[i][1],robocoord[i][0],robosmall1[i])
						win.addch(robocoord[1][1],robocoord[1][0],'\\')
						win.addch(robocoord[3][1],robocoord[3][0],'/')
				
	   			win.addch(robocoord[1][1]-1,robocoord[1][0],' ')
	    			win.addch(robocoord[3][1]-1,robocoord[3][0],' ')
	   			if countdown==0:
					countdown=1
				else:
					countdown=0
	   			
	    		else:
		    		break
    		elif(key==KEY_UP):
	    
	
	    
	    		robocoord=map(lambda x:[x[0],x[1]-1],robocoord)
#		print snake    	
			decision=a.checksm(robocoord)
		
			if(decision==0):
				for i in xrange(0,len(robocoord)):
					if countup==0:
					
						win.addch(robocoord[i][1],robocoord[i][0],robosmall[i])
						win.addch(robocoord[0][1],robocoord[0][0],robosmall[0],curses.color_pair(2))
	                                        win.addch(robocoord[2][1],robocoord[2][0],robosmall[2],curses.color_pair(2))
	    				else:
						
						win.addch(robocoord[i][1],robocoord[i][0],robosmall1[i])
						win.addch(robocoord[1][1],robocoord[1][0],'\\')
						win.addch(robocoord[3][1],robocoord[3][0],'/')
	    			win.addch(robocoord[0][1]+1,robocoord[0][0],' ')
	    			win.addch(robocoord[2][1]+1,robocoord[2][0],' ')
				if countup==0:
					countup=1
				else:
					countup=0
	    		else:
		    		break
	
 		elif key == ord('p'):
			y=win.getch()
			while(y!=ord('p')):
				y=win.getch()
			key=prev





#if key & 255 ==ord('p'):
#			win.addch(3,3,"x")
#			getkey=-1
#			win.timeout(-1)
#			while getkey==-1:
#				getkey=win.getch()
#				win.addch(3,3,"r")		
#				if getkey!=-1:
#					
#					win.timeout(180)
#					getkey=KEY_RIGHT
#					flagx=0
#					break



curses.init_pair(4,curses.COLOR_BLUE,curses.COLOR_BLACK)








def robo1():
	global snake
	global key
	global robo
	global flag
	global decision
	global speed
	global speedarr
	global height
	global width
	global ancount
	prev=None
	countright=countleft=countup=countdown=0
	win.addch(snake[0][1],snake[0][0],'\\')
	win.addch(snake[1][1],snake[1][0],'|')
	win.addch(snake[2][1],snake[2][0],']')
	win.addch(snake[3][1],snake[3][0],'/')
	win.addch(snake[4][1],snake[4][0],' ')
	win.addch(snake[5][1],snake[5][0],'_')
	win.addch(snake[6][1],snake[6][0],'@')
	win.addch(snake[7][1],snake[7][0],'i')
	win.addch(snake[8][1],snake[8][0],' ')
	win.addch(snake[9][1],snake[9][0],'_')
	win.addch(snake[10][1],snake[10][0],'@')
	win.addch(snake[11][1],snake[11][0],'i')
	win.addch(snake[12][1],snake[12][0],'/')
	win.addch(snake[13][1],snake[13][0],'|')
	win.addch(snake[14][1],snake[14][0],'[')
	win.addch(snake[15][1],snake[15][0],'\\')
	while key != 27:

    		if(snake[0][0]==width-1 or snake[15][0]==0):
			flag=-1    
			break
    		elif(snake[0][1]==height-1 or snake[7][1]==0):
			flag=-1
			break
    		win.addstr(0,width/2-9,' code points' + ' : '+str(a.count*10-a.antiscore*10)+' ')
    		win.timeout(speedarr[speed]-count*8)#+ ( (len(snake)-6) % 10- (len(snake)-6) ) * 3 )
    		prev=key
		getkey = win.getch()
    		key = key if getkey==-1 else getkey

    		def check():
	    		global snake 
	    		global count
			global levelx
			global antiscore
			global ancount

	    		status=0
	    		for i in xrange(0,len(snake)):
		    		if(win.inch(snake[i][1],snake[i][0]) & 255 == ord('C')):
					    count=count+1
					    # win.addch(5,5,count)
	    	    		elif(count==d and win.inch(snake[i][1],snake[i][0]) & 255 ==ord('B')):
			    		    status=1
					    return status
		    		elif(count!=d and win.inch(snake[i][1],snake[i][0]) & 255 == ord('B')):
			    		    status=-1
	    				    return status				    
				elif(levelx==1 and win.inch(snake[i][1],snake[i][0]) & 255 ==ord('A') and ancount!=0):
					    ancount=ancount-1
					    antiscore=antiscore+1
					    
# win.addch(5,5,str(ancount))
				elif(levelx==1 and win.inch(snake[i][1],snake[i][0]) & 255 == ord('A') and ancount==0):
					    status=-1
					    return status
	    
	    		return status
	

    		if(key==KEY_RIGHT):
			snake=map(lambda x:[x[0]+1,x[1]] , snake)
	

			decision=a.checksm(snake)
			if(decision==0):
		

				for i in xrange(0,len(snake)):
					if countright==0:
						win.addch(snake[i][1],snake[i][0],robo[i],curses.color_pair(4))
						
						win.addch(snake[0][1],snake[0][0],robo[0],curses.color_pair(1))
						win.addch(snake[12][1],snake[12][0],robo[12],curses.color_pair(1))
						win.addch(snake[6][1],snake[6][0],robo[6],curses.color_pair(2))
						
						win.addch(snake[10][1],snake[10][0],robo[10],curses.color_pair(2))
					else:
						win.addch(snake[i][1],snake[i][0],robo2[i])
				for i in xrange(12,16):
					win.addch(snake[i][1],snake[i][0]-1,' ')
			        if countright==0:
				 	countright=1
				else:
				 	countright=0

        		else:
				break
    		elif(key==KEY_LEFT):
			snake=map(lambda x:[x[0]-1,x[1]],snake)
	
#	print snake
			decision=a.checksm(snake)
	
			if(decision==0):
#		for i in xrange(0,4):
#			win.addch(snake[i][1],snake[i][0]+1,' ')
#		for i in xrange(4,8):
#	 		win.addch(snake[i][1],snake[i][0],'X')
				for i in xrange(0,len(snake)):
					if countleft==0:

						win.addch(snake[i][1],snake[i][0],robo[i],curses.color_pair(4))
						win.addch(snake[0][1],snake[0][0],robo[0],curses.color_pair(1))
						win.addch(snake[12][1],snake[12][0],robo[12],curses.color_pair(1))
						win.addch(snake[6][1],snake[6][0],robo[6],curses.color_pair(2))
						win.addch(snake[10][1],snake[10][0],robo[10],curses.color_pair(2))
					else:
						win.addch(snake[i][1],snake[i][0],robo2[i])

				for i in xrange(0,4):
		 			win.addch(snake[i][1],snake[i][0]+1,' ')
				if countleft==0:
				  	countleft=1
				else:
				  	countleft=0
			else:
				break
     
#snake.insert(0,[snake[0][0]+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), snake[0][1]+(key==KEY_DOWN and 1 or key==KEY_UP and -1)])
    
#    win.addch(snake[len(snake)-1][1],snake[len(snake)-1][0],' ')
    		elif(key==KEY_DOWN):
	    
	    
	    
	    		snake=map(lambda x:[x[0],x[1]+1],snake)
#	    	print snake
			decision=a.checksm(snake)
		
			if(decision==0):
				for i in xrange(0,len(snake)):
					if countdown==0:

						win.addch(snake[i][1],snake[i][0],robo[i],curses.color_pair(4))
					       	
						win.addch(snake[0][1],snake[0][0],robo[0],curses.color_pair(1))
						win.addch(snake[12][1],snake[12][0],robo[12],curses.color_pair(1))
						win.addch(snake[6][1],snake[6][0],robo[6],curses.color_pair(2))
						win.addch(snake[10][1],snake[10][0],robo[10],curses.color_pair(2))
					else:
						win.addch(snake[i][1],snake[i][0],robo3[i])
	   			win.addch(snake[3][1]-1,snake[3][0],' ')
	    			win.addch(snake[7][1]-1,snake[7][0],' ')
	   			win.addch(snake[11][1]-1,snake[11][0],' ')
	   			win.addch(snake[15][1]-1,snake[15][0],' ')
				if countdown==0:
					countdown=1
				else:
					countdown=0
	    		else:
		    		break
    		elif(key==KEY_UP):
	    
	
	    
	    		snake=map(lambda x:[x[0],x[1]-1],snake)
#		print snake    	
			decision=a.checksm(snake)
		
			if(decision==0):
				for i in xrange(0,len(snake)):
					if countup==0:
						win.addch(snake[i][1],snake[i][0],robo[i],curses.color_pair(4))
					       	
						win.addch(snake[0][1],snake[0][0],robo[0],curses.color_pair(1))
						win.addch(snake[12][1],snake[12][0],robo[12],curses.color_pair(1))
						win.addch(snake[6][1],snake[6][0],robo[6],curses.color_pair(2))
						win.addch(snake[10][1],snake[10][0],robo[10],curses.color_pair(2))
					else:
						win.addch(snake[i][1],snake[i][0],robo3[i])
	    	
	    			win.addch(snake[0][1]+1,snake[0][0],' ')
	    			win.addch(snake[4][1]+1,snake[4][0],' ')
				win.addch(snake[8][1]+1,snake[8][0],' ')
				win.addch(snake[12][1]+1,snake[12][0],' ')
				if countup==0:
					countup=1
				else:
					countup=0
	    		else:
		    		break
	
    
    
    
		elif key == ord('p'):
			y=win.getch()
			while(y!=ord('p')):
				y=win.getch()
			key=prev





#print win.inch(snake[0][1],snake[0][0])
#if win.inch(snake[0][1],snake[0][0]) & 255 == 32: 
#	win.addch(snake[0][1],snake[0][0],'X')
#	snake.pop()
    
#   elif win.inch(snake[0][1],snake[0][0]) & 255 == ord('C'):  
#	win.addch(snake[0][1],snake[0][0],'X')
#	snake.pop()
#	count=count+1       
#	c = [n for n in [[randrange(1,58,1),randrange(1,14,1)] for x in range(len(snake))] if n not in snake]
#	print c
#       win.addch(c == [] and 4 or c[0][1],c == [] and 44 or c[0][0],'C')
#    elif count!=d and win.inch(snake[0][1],snake[0][0]) & 255 == ord('B'):
#	    flag=0
#	    break
#   elif count==d and win.inch(snake[0][1],snake[0][0]) & 255 == ord('B'):
#	    flag=1
#	    break
#   else:
#	flag=0
#	break
#if robo==0:
#	robosmallfunc()
#elif robo==1:
#	robomedfunc()
#elif robo==2:
#win.addstr(5,5,str(robo))
#y=0
#while(y & 255!=10): 
#	y=win.getch()
if robonumber==0:
	robosmallfunc()
elif robonumber==1:
	robomedfunc()
elif robonumber==2:
	robo1()
endwin()
if flag==-1:
	print "robot left the arena"
	print "number of codes collected",str(count),"and yout score is",str(count*10)
	print "robot.py","(by Kumar Rishabh","thanks for playing anyway"
elif decision==1:
	if a.antiscore==0:	
		print "Mission successful"
		print "Number of codes collected",str(a.count),"and your score is",str(a.count*10)
		print "robot.py","(by Kumar Rishabh)","thanks for playing"
	else :
		print "Mission accomplished but you didnt get full points"
		print "Number of codes collected",str(a.count)
		print "number of anticodes collected",str(a.antiscore)
		print "your score is",str(a.count*10-a.antiscore*10)
		print "robot.py","(by Kumar Rishabh)","thanks for playing"
else:
	#win.flash()
	print "Mission fucked"
	print "Number of codes collected",str(a.count),"and your score is",str(a.count*10)
	print "robot.py","(by Kumar Rishabh)","thanks for playing anyway"
#print '\n  Snake.PY (by Kumar Rishabh),\, n  Thanks for playing, your score: '+str(len(snake)-7)+'\n'
