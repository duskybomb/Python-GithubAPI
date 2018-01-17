from github import Github

""" 
authenticate by:
    using access token
        g = Github('Add access token here') 
    or passing handle and password as param: 
        g = Github('username','password')
"""
g = Github('Add access token here')

# Starting point for the loop
# Add the github handle you want to start from
_UserName = 'Starting_User_Name'

# Open file for data entry
new_path = 'data.txt'
new_file = open(new_path, 'w')

# que_data: add followers to the queue
# visited_users: check for visited users
que_data = []
visited_users = []
# Append first user
que_data.append(_UserName)
visited_users.append(_UserName)


def take_data(user_name):
    """
    Core Function to crawl through all the followers of a certain user and check for >30 repo
    :param user_name:
    :return:
    """
    print(user_name)
    que_data.remove(user_name)
    for follow in g.get_user(user_name).get_followers():

        if g.get_user(user_name).public_repos > 30 and follow.login not in visited_users and \
                g.get_user(follow.login).email is not None:
            que_data.append(follow.login)
            visited_users.append(follow.login)
            try:
                new_file.write(g.get_user(follow.login).email + ' ' + g.get_user(follow.login).login + ' ' + str(
                    g.get_user(follow.login).public_repos) + '\n')
            except:
                pass

    for user_name in que_data:
        take_data(user_name)

# Data entry for first user
try:
    new_file.write(g.get_user(_UserName).email + ' ' + g.get_user(_UserName).login + ' ' + str(
        g.get_user(_UserName).public_repos) + '\n')
except:
    pass

# Calling take_data()
take_data(_UserName)

# Close the opened file
new_file.close()