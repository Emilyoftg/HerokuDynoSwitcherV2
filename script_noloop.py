#!/usr/bin/env python3
#
# (c) Katarina & 5MysterySD V2
#
# All Right Reserved 

from itertools import zip_longest
from time import sleep
from os import environ
from datetime import datetime
from heroku3 import from_key as from_apikey

def getVar(var: str, val: str):
    return environ.get(var, val)

# Required vars >>>>>>>> Add Unlimited Number of Apps separated by space in each var
# A = The Credentials of the First Account
# B = The Credentials of the Second Account
# C = The Credentials of the Third Account
A_APPNAME = getVar('A_APPNAME',"")
A_APIKEY = getVar('A_APIKEY',"")
B_APPNAME = getVar('B_APPNAME',"")
B_APIKEY = getVar('B_APIKEY',"")
PROCESSTYPE = getVar('PROCESSTYPE',"")
CA_APPNAME = getVar('CA_APPNAME',"")
CB_APPNAME = getVar('CB_APPNAME',"")
C_APIKEY = getVar('C_APIKEY',"")

# List Forming >>>>>>>>
A_APPNAME = A_APPNAME.split(" ")
A_APIKEY = A_APIKEY.split(" ")
B_APPNAME = B_APPNAME.split(" ")
B_APIKEY = B_APIKEY.split(" ")
PROCESSTYPE = PROCESSTYPE.split(" ")
CA_APPNAME = CA_APPNAME.split(" ")
CB_APPNAME = CB_APPNAME.split(" ")
C_APIKEY = C_APIKEY.split(" ")

# The Main Script Execution >>>>>>>>
today = datetime.now()

# Multiple Pair of Apps >>>>>>>>
print("Checking the Conditions & Vars for the app ..")
if(len(PROCESSTYPE) != 0 and len(A_APIKEY) != 0 and len(A_APPNAME) != 0 and len(C_APIKEY) != 0 and len(CA_APPNAME) != 0):
  if(today.day == 23):
    for  (A, AAPP, PRO, B, BAPP, C, CAAPP, CBAPP) in zip_longest(A_APIKEY, A_APPNAME, PROCESSTYPE, B_APIKEY, B_APPNAME, C_APIKEY, CA_APPNAME, CB_APPNAME):
      if len(CB_APPNAME) != 0 and len(B_APIKEY) != 0 and len(B_APPNAME) != 0:
        print("Changing the Dyno of the First Account..")
        heroku_conn = from_apikey(A)
        app = heroku_conn.app(AAPP)
        app.process_formation()[PRO].scale(0)
        print("The App in the First Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of the Second Account..")
        heroku_conn = from_apikey(B)
        app = heroku_conn.app(BAPP)
        app.process_formation()[PRO].scale(0)
        print("The App in the Second Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of First App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CAAPP)
        app.process_formation()[PRO].scale(1)
        print("The First App in the Third Account has been Scaled Up.")

        sleep(5)

        print("Changing the Dyno of Second App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CBAPP)
        app.process_formation()[PRO].scale(1)
        print("The Second App in the Third Account has been Scaled Up.")
      else: # Single Account Switch Function
        print("Changing the Dyno of the First Account..")
        heroku_conn = from_apikey(A)
        app = heroku_conn.app(AAPP)
        app.process_formation()[PRO].scale(0)
        print("The App in the First Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of First App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CAAPP)
        app.process_formation()[PRO].scale(1)
        print("The First App in the Third Account has been Scaled Up.")

  elif(today.day == 1):
    for  (A, AAPP, PRO, B, BAPP, C, CAAPP, CBAPP) in zip_longest(A_APIKEY, A_APPNAME, PROCESSTYPE, B_APIKEY, B_APPNAME, C_APIKEY, CA_APPNAME, CB_APPNAME):
      if len(CB_APPNAME) != 0 and len(B_APIKEY) != 0 and len(B_APPNAME) != 0:
        print("Changing the Dyno of First App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CAAPP)
        app.process_formation()[PRO].scale(0)
        print("The First App in the Third Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of Second App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CBAPP)
        app.process_formation()[PRO].scale(0)
        print("The Second App in the Third Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of the First Account..")
        heroku_conn = from_apikey(A)
        app = heroku_conn.app(AAPP)
        app.process_formation()[PRO].scale(1)
        print("The App in the First Account has been Scaled Up.")

        sleep(5)

        print("Changing the Dyno of the Second Account..")
        heroku_conn = from_apikey(B)
        app = heroku_conn.app(BAPP)
        app.process_formation()[PRO].scale(1)
        print("The App in the Second Account has been Scaled Up.")
      else: # Single Account Switch Function
        print("Changing the Dyno of First App of the Third Account..")
        heroku_conn = from_apikey(C)
        app = heroku_conn.app(CAAPP)
        app.process_formation()[PRO].scale(0)
        print("The First App in the Third Account has been Scaled Down.")

        sleep(5)

        print("Changing the Dyno of the First Account..")
        heroku_conn = from_apikey(A)
        app = heroku_conn.app(AAPP)
        app.process_formation()[PRO].scale(1)
        print("The App in the First Account has been Scaled Up.")

  else:
    print("Today is not 1st or 23rd of Current Month")
else:
  print("Variables for the app are not fully filled. RECHECK AGAIN. ")
     
# Ending the Current process >>>>>>>>
print("\nThe Script has been Executed.")
