import webbrowser, sys, pyperclip

print("Hello World")
sys.argv #['mapit.py','20','Wellwood','St.']

if len(sys.argv) > 1:
    #['mapit.py','870','Valencia','St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.co.uk/maps/place/20+Wellwood+St,+Belfast+BT12+5GE/
#https://www.google.co.uk/maps/place/<ADDRESS>
webbrowser.open('https://www.google.co.uk/maps/place/'+ address)    
    
    
