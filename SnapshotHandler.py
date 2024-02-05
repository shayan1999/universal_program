# I created this file to implement functions to update snapshots of our program
# this first function is used to check what kind of operation we are going to handle
# after that it will get results from other functions and will update line_number and snapshot
def check_line(code, snapshot, line_number):
    if(code[line_number]['b']==0):
        # this one is skip operator so we just need to skip one line
        line_number= line_number+1
    elif(code[line_number]['b']==1):
        snapshot, line_number=update_snapshot_increment(snapshot= snapshot, line_number= line_number, variable=code[line_number]['c'])
    elif(code[line_number]['b']==2):
        snapshot, line_number=update_snapshot_decrement(snapshot= snapshot, line_number= line_number, variable=code[line_number]['c'])
    else:
        line_number= update_snapshot_condition(line_number= line_number, variable= code[line_number]['c'], label_number= code[line_number]['b']-2, code= code, snapshot= snapshot)
    
    return snapshot, line_number

# it checks if the the variable is not equal to zero after that it checks if it can
# find the label provided in this line and changes line of code if any of these not happens
# it simply send our code to next line
def update_snapshot_condition(line_number, variable, label_number, code, snapshot):
    if(snapshot[variable]!=0):
        for i in range(len(code)):
            if(code[i]['a']==label_number):
                line_number= i
                return i
    return line_number+1


# these two will update one element by incrementing or decrementing then moves to next line
def update_snapshot_decrement(snapshot, line_number, variable):
    snapshot[variable] -= 1
    return snapshot, line_number+1

def update_snapshot_increment(snapshot, line_number, variable):
    snapshot[variable] += 1
    return snapshot, line_number+1