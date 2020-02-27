def shut_down(s):
    if s == "yes":
        return 'shutting down'
    elif s== "no":
        return 'shutting aborted'
    else:
        return 'sorry'

#print(shut_down("no"))