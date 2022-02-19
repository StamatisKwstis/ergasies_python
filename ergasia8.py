import random
for i in range (99):
	def print_board(x):
		for i in range(8):
			print (" ".join(x[i]))
	
	Rook=1
	Bishop=1
	tmp=["0"]*(64-Rook)
	tmp+=["Rook"]*Rook
	tmp1=["0"]*(64-Bishop)
	tmp1+=["Bishop"]*Bishop	
	random.shuffle(tmp)
	random.shuffle(tmp1)
	board=[]


	for i in range(8):
		board+=[tmp[8*i:8*i+8]]
		board+=[tmp1[8*i:8*i+8]]

	ele="Rook"      #ηθελα να βρω τον δεικτη του καθε πιονου στην λιστα μιας λιστας                
	R_pos=0         #ωστε να τον χρησιμοποιησω στις συναρτησεις παρακατω αλλα δεν το καταφερα έγκαιρα... 
	for i in board:
		if (i==ele):
			R_pos=i
			break
	

	ele1="Bishop"
	B_pos=0
	for i in board:
		if (i==ele1):
			B_pos=i
			break
		

def BishopTakeDown(bishopX, BishopY, RookX, RookY) :
    if (RookX - bishopX == RookY - BishopY) :
        return True    
    elif (-RookX + bishopX == RookY - bishopY):
        return True    
    else:
        return False
 
# Bishop's Position
bishopX=B_pos
bishopY=B_pos
# Rook's Position
rookX=R_pos
rookY=R_pos

rook_score=0
bishop_score=0
if (BishopTakeDown(bishopX, bishopY, rookX, rookY)) :
    bishop_score=bishop_score+1

def Rookcantakedown(current_row, current_col, destination_row, destination_col):     
    if(current_row == destination_row):
        return True 
    elif(current_col == destination_col):
        return True 
    else:
        return False

current_row=R_pos
current_col=R_pos
destination_row =B_pos
destination_col=B_pos
 
if Rookcantakedown(current_row, current_col, destination_row, destination_col): 
    rook_score=rook_score+1

print (rook_score,bishop_score)