import urllib.request
from inscriptis import get_text
from flask import *
import re


user = input("Enter Your UserName: ")
url = 'http://instagram.com/' + user + '/'

webpg = urllib.request.urlopen(url).read().decode('utf-8')
# textpg = get_text(webpg)
# textpg = str(webpg).lower()
# print(webpg)

try:
    print('Info :\n')
    info = re.compile(r'href\=\"(.*)\"\s*\/\>\s*\<meta\scontent\=\"(.*)\sFollowers,\s(.*)\sFollowing,\s*(.*)\sPosts\s*\-\s*See\s*Instagram\s*photos\s*and\svideos\s*from\s*(.*)\s*\((@.*)\)')
    person_info = info.findall(webpg)

    if person_info:
        for link , follower, following, posts, acc_name, username in person_info:

            print('Account Link    --> {}'.format(link))
            print('Followers Count --> {}'.format(follower))
            print('Following Count --> {}'.format(following))
            print('Posts Count     --> {}'.format(posts))
            print('Account Name    --> {}'.format(acc_name))
            print('User Name       --> {}'.format(username))


    else:
        print('Not Found This UserName')


except:
    print('Not Found This UserName')

    # re.compile(r'href\=\"(.*)\"\s*\/\>\s*\<meta\scontent\=\"(.*)\sFollowers,\s(.*)\sFollowing,\s*(.*)\sPosts\s*\-\s*See\s*Instagram\s*photos\s*and\svideos\s*from\s*(.*)\s*\((@.*)\)')
