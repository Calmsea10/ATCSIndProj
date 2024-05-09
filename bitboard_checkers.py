def initialize_white_board(white_board):
    for i in range(20,33):
        white_board=white_board|(1<<i)
    return white_board

def initialize_red_board(red_board):
    for i in range(0,12):
        red_board=red_board|(1<<i)
    return red_board

def board_repr(board):
    for i in range(0,8):
        for j in range(0,4):
            print((board>>((4*i)+j))&1,end=' ')
        print('')

def get_valid_moves(board1,board2,team,pos):
    if not (board1>>pos)&1:
        return []
    else:
        moves=[]
        if team:
            move1=(pos-(3+((pos//4)%2)))
            move2=(pos-(4+((pos//4)%2)))
            if move1>=0:
                if (pos//4)-(move1//4)==1:
                    if (not (board1>>move1)&1) and (not (board2>>move1)&1):
                        moves.append(move1)
            if move2>=0:
                if (pos//4)-(move2//4)==1:
                    if (not (board1>>move2)&1) and (not (board2>>move2)&1):
                        moves.append(move2)
        else:
            move1=(pos+(3+(((pos//4)+1)%2)))
            move2=(pos+(4+(((pos//4)+1)%2)))
            if move1<=31:
                if (pos//4)-(move1//4)==-1:
                    if (not (board1>>move1)&1) and (not (board2>>move1)&1):
                        moves.append(move1)
            if move2<=31:
                if (pos//4)-(move2//4)==-1:
                    if (not (board1>>move2)&1) and (not (board2>>move2)&1):
                        moves.append(move2)
        return moves

def can_capture(board1,board2,team,pos):
    capture_dirs=[]
    if team:
        capture1=(pos-7)
        move1=(pos-(3+((pos//4)%2)))
        capture2=(pos-9)
        move2=(pos-(4+((pos//4)%2)))
        if capture1>=0:
            if (pos//4)-(capture1//4)==2:
                if (not ((board1>>capture1)&1)) and (not ((board2>>capture1)&1)):
                    if (board2>>move1)&1:
                        capture_dirs.append(1)
        if capture2>=0:
            if (pos//4)-(capture2//4)==2:
                if (not ((board1>>capture2)&1)) and (not ((board2>>capture2)&1)):
                    print(capture2)
                    if (board2>>move2)&1:
                        capture_dirs.append(2)
    else:
        capture1=(pos+7)
        move1=(pos+(3+((pos//4)%2)))
        capture2=(pos+9)
        move2=(pos+(4+((pos//4)%2)))
        if capture1<=31:
            if (pos//4)-(capture1//4)==2:
                if ((board1>>capture1)^1) and ((board2>>capture1)^1):
                    if (board1>>move1)&1:
                        capture_dirs.append(3)
        if capture2<=31:
            if (pos//4)-(capture2//4)==2:
                if ((board1>>capture2)^1) and ((board2>>capture2)^1):
                    if (board1>>move2)&1:
                        capture_dirs.append(4)
    if len(capture_dirs)==0:
        return [0]
    else:
        return capture_dirs

def get_possible_captures(board1,board2,capture_list,team):
    return_moves=[]
    holder=[]
    pos=capture_list[0]
    capture_dirs=can_capture(board1,board2,team,pos)
    if 1 in capture_dirs:
        holder=capture_list[:]
        holder[0]=capture_list[0]-7
        holder.append(pos-(3+((pos//4)%2)))
        return_moves.extend(get_possible_captures(board1,board2,holder,team))
    if 2 in capture_dirs:
        holder=capture_list[:]
        holder[0]=capture_list[0]-9
        holder.append(pos-(4+((pos//4)%2)))
        return_moves.extend(get_possible_captures(board1,board2,holder,team))
    if 3 in capture_dirs:
        holder=capture_list[:]
        holder[0]=capture_list[0]+7
        holder.append(pos+(3+((pos//4)%2)))
        return_moves.extend(get_possible_captures(board1,board2,holder,team))
    if 4 in capture_dirs:
        holder=capture_list[:]
        holder[0]=capture_list[0]+9
        holder.append(pos+(4+((pos//4)%2)))
        return_moves.extend(get_possible_captures(board1,board2,holder,team))
    if 0 in capture_dirs:
        capture_list.append(-1)
        return capture_list
    return return_moves

def move(board1,board2,start_pos,end_pos,team):
    if team:
        if board1>>(start_pos)&1:
            if end_pos in get_valid_moves(board1,board2,team,start_pos):
                board1=board1|(1<<end_pos)
                board1=board1^(1<<start_pos)
                return board1
    else:
        if board1>>(start_pos)&1:
            if end_pos in get_valid_moves(board1,board2,team,start_pos):
                board1=board1|(1<<end_pos)
                board1=board1^(1<<start_pos)
                return board1

def main():
    board_white=0
    board_red=0
    board_white=initialize_white_board(board_white)
    board_red=initialize_red_board(board_red)
    board_repr(board_red+board_white)
    print(get_valid_moves(board_white,board_red,True,23))
    board_white=move(board_white,board_red,23,18,True)
    print(get_valid_moves(board_red,board_white,False,9))
    board_red=move(board_red,board_white,9,14,False)
    board_repr(board_white+board_red)
    print(get_possible_captures(board_white,board_red,[18],True))
    print(get_valid_moves(board_white,board_red,True,18))

if __name__ == "__main__":
    main()