# # import module
# import os
#
#
# # function to establish a new connection
# def createNewConnection(name, SSID, password):
#     config = """<?xml version=\"1.0\"?>
# <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
# 	<name>""" + name + """</name>
# 	<SSIDConfig>
# 		<SSID>
# 			<name>""" + SSID + """</name>
# 		</SSID>
# 	</SSIDConfig>
# 	<connectionType>ESS</connectionType>
# 	<connectionMode>auto</connectionMode>
# 	<MSM>
# 		<security>
# 			<authEncryption>
# 				<authentication>WPA2PSK</authentication>
# 				<encryption>AES</encryption>
# 				<useOneX>false</useOneX>
# 			</authEncryption>
# 			<sharedKey>
# 				<keyType>passPhrase</keyType>
# 				<protected>false</protected>
# 				<keyMaterial>""" + password + """</keyMaterial>
# 			</sharedKey>
# 		</security>
# 	</MSM>
# </WLANProfile>"""
#     command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
#     with open(name + ".xml", 'w') as file:
#         file.write(config)
#     os.system(command)
#
#
# # function to connect to a network
# def connect(name, SSID):
#     command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
#     os.system(command)
#
#
# # function to display avavilabe Wifi networks
# def displayAvailableNetworks():
#     command = "netsh wlan show networks interface=Wi-Fi"
#     os.system(command)
#
#
# # display available netwroks
# displayAvailableNetworks()
#
# # input wifi name and password
# name = input("Name of Wi-Fi: ")
# password = input("Password: ")
#
# # establish new connection
# createNewConnection(name, name, password)
#
# # connect to the wifi network
# connect(name, name)
# print("If you aren't connected to this network, try connecting with the correct password!")

# import cv2
# cap = cv2.VideoCapture(0)
# # initialize the cv2 QRCode detector
# detector = cv2.QRCodeDetector()
# while True:
#     _, img = cap.read()
#     data, bbox, _ = detector.detectAndDecode(img)
#     if data:
#         p = data.split(";")[1][2:]
#         u = data.split(";")[2][2:]
#         print(p,u,data)
#         break
#     cv2.imshow("QRCODEscanner", img)
#     if cv2.waitKey(1) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
# rp="WIFI:S:abhishek5;T:WPA;P:abhishek@5;H:false;;"
# rp="WIFI:S:abhishek2.4;T:WPA;P:abhishek@2.4;H:false;;"
# rp="WIFI:T:WPA;P:sourab@1999;S:SOURAB MAITY;H:false;"
# rp ="a"
# print(rp.find("S:"),rp[rp.find("S:")+2:rp.find(";",rp.find("S:"))],rp[rp.find("P:")+2:rp.find(";",rp.find("P:"))])

import os
import cv2

def WiFi_QR():
    S = P=" "
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            S = data[data.find("S:")+2:data.find(";",data.find("S:"))]
            P = data[data.find("P:")+2:data.find(";",data.find("P:"))]
            print(S,P,data)
            break
        cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return S, P


# function to establish a new connection
def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>""" + name + """</name>
	<SSIDConfig>
		<SSID>
			<name>""" + SSID + """</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>""" + password + """</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    with open(name + ".xml", 'w') as file:
        file.write(config)
    os.system(command)


# function to connect to a network
def connect(name, SSID):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
    os.system(command)


# function to display avavilabe Wifi networks
def displayAvailableNetworks():
    command = "netsh wlan show networks interface=Wi-Fi"
    os.system(command)


# display available netwroks
displayAvailableNetworks()

# input wifi name and password
name, password= WiFi_QR()

# establish new connection
createNewConnection(name, name, password)

# connect to the wifi network
connect(name, name)
print("If you aren't connected to this network, try connecting with the correct password!")














