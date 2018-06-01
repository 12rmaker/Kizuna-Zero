def getUser(discord, db, arg):
    '''
    Input:
    - discord (discord): pass discord object from app
    - db      (list)   : pass ctx.message.server.members
    - arg     (str)    : string id or username to search for

    Output:
    - returns member/User object if user is found
    - returns False if there is no match
    '''
    #search by id attribute
    member = discord.utils.get(db, id = arg)
    #if we get results
    if member:
        #output member/User object
        return member
    #if member isnt found
    else:
        #search with name attribute
        member = discord.utils.find(lambda m: arg.lower() in m.name.lower(), db)
        #if we get results
        if member:
            return member
        #else search by ping
        else:
            #oh boi ping check time using raw string
            if "<@" in arg and ">" in arg:
                #split <@ out of string
                ident = arg.split("<@")[1]
                #split out > at end now
                ident = ident.split(">")[0]
                #not grab user for last attempt
                member = discord.utils.get(db, id = ident)
                #if we get results
                if member:
                    return member
                #else feelsbadman
                else:
                    return False

def getUsers(discord, db, args):
    '''
    Input:
    - discord (discord): pass discord object from app
    - db      (list)   : pass ctx.message.server.members
    - args    (list)   : bunch of strings to search against

    Output:
    - returns list of mentionable users
    - if member not found, they are not added to output list
      Example: ["12rmaker", "Solarinas"]
    '''
    #create empty user list
    users = []
    #loop through search string list "args"
    for i in args:
        #user previous "getUser" function on each element of args
        member = getUser(discord, db, i)
        #check if we got actual results
        if member:
            #then add to user list
            users.append(member)
    return users

def duplicateCleaner(items):
    newList = []    # Create a new array for a new list
    for i in items: 
        if i not in newList: # if item is not in the new list then add it into the new list
            newList.append(i)
    return newList
