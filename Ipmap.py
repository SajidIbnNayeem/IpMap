# Ipmap

# Author - sajid ibn nayeem

# github - https://github.com/SajidIbnNayeem



import json
import urllib.request
import webbrowser
import os
import sys 

class IPAddressLocator:
    def __init__(self):
        self.R = '\033[91m'
        self.Y = '\033[93m'
        self.G = '\033[92m'
        self.CY = '\033[96m'
        self.W = '\033[97m'
        self.path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
        
        
    def start(self):
        os.system('clear')
        print(self.R + """
          
                    ____     __  ___        
                   /  _/__  /  |/  /__ ____ 
                  _/ // _ \/ /|_/ / _ `/ _ \ 
                 /___/ .__/_/  /_/\_,_/ .__/
                    /_/     V1.0     /_/    
                
             """ + self.G + """    𝑺𝒊𝒎𝒑𝒍𝒆 𝑰𝑷 𝑨𝒅𝒅𝒓𝒆𝒔𝒔 𝒍𝒐𝒄𝒂𝒕𝒐𝒓
        
        """ + self.R + """>>""" + self.Y + """----""" + self.CY + """ Author - Sajid Ibn Nayeem """ + self.Y + """----""" + self.R + """<<""")

    def m3(self):
        try:
            print(self.R + """\n
    #""" + self.Y + """ Select option""" + self.G + """ >>""" + self.Y + """
    
    1)""" + self.G + """ Check your IP info""" + self.Y + """
    2)""" + self.G + """ Check other IP info""" + self.Y + """
    3)""" + self.G + """ Exit
    """)
            ch = int(input(self.CY + "Enter Your choice: " + self.W))
            if ch == 1:
                self.main2()
                self.m3()
            elif ch == 2:
                self.main()
                self.m3()
            elif ch == 3:
                print(self.Y + "Exit................" + self.W)
                sys.exit(0)
            else:
                print(self.R + "\nInvalid choice! Please try again\n")
                self.m3()
        except ValueError:
            print(self.R + "\nInvalid choice! Please try again\n")
            self.m3()

    def finder(self, u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(self.R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(self.Y + '\n>>>' + self.CY + ' IP address details\n ')
                print(self.G + "1) IP Address : " + self.Y, data['query'], '\n')
                print(self.G + "2) Org : " + self.Y, data['org'], '\n')
                print(self.G + "3) City : " + self.Y, data['city'], '\n')
                print(self.G + "4) Region : " + self.Y, data['regionName'], '\n')
                print(self.G + "5) Country : " + self.Y, data['country'], '\n')
                print(self.G + "6) Location\n")
                print(self.G + "\tLattitude : " + self.Y, data['lat'], '\n')
                print(self.G + "\tLongitude : " + self.Y, data['lon'], '\n')
                l = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
                print(self.R + "\n#" + self.Y + " Google Map link : " + self.CY, l)
                path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link = 'am start -a android.intent.action.VIEW -d ' + str(l)
                    pr = input(self.R + "\n>>" + self.Y + " Open link in browser?" + self.G + " (y|n): " + self.W)
                    if pr == "y":
                        lnk = str(link) + " > /dev/null"
                        os.system(str(lnk))
                        self.start()
                        self.m3()
                    elif pr == "n":
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        self.start()
                        self.m3()
                    else:
                        print("\nInvalid choice! Please try again\n")
                        self.m3()
                else:
                    pr = input(self.R + "\n>>" + self.Y + " Open link in browser?" + self.G + " (y|n): " + self.W)
                    if pr == "y":
                        webbrowser.open(l, new=0)
                        self.start()
                        self.m3()
                    elif pr == "n":
                        print(self.R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(self.Y + "\nCheck another IP or exit using " + self.R + "Ctrl + C\n\n")
                        self.start()
                        self.m3()
                    else:
                        print(self.R + "\nInvalid choice! Please try again\n")
                        self.m3()
                return
            except KeyError:
                print(self.R + "\nError! Invalid IP/Website Address!\n" + self.W)
                self.m3()
        except urllib.error.URLError:
            print(self.R + "\nError!" + self.Y + " Please check your internet connection!\n" + self.W)
            exit()

    def main(self):
        u = input(self.G + "\n>>> " + self.Y + "Enter IP Address/website address:" + self.W + " ")
        if u == "":
            print(self.R + "\nEnter valid IP Address/website address!")
            self.main()
        else:
            url = 'http://ip-api.com/json/' + u
            self.finder(url)

    def main2(self):
        url = 'http://ip-api.com/json/'
        self.finder(url)

    def run(self):
        try:
            self.start()
            self.m3()
        except KeyboardInterrupt:
            print(self.Y + "\nInterrupted! Have a nice day :)" + self.W)

if __name__ == "__main__":
    ip_locator = IPAddressLocator()
    ip_locator.run()