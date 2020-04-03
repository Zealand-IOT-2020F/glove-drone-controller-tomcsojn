import socket
import sys
import time


class Drone(object):
    """description of class"""


    def __init__(self, ip, port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        # Create a UDP socket
        self.Host = ''
        self.HostPort = 9000
        self.locaddr = (self.Host,self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = (self.TelloIp, self.TelloPort)
        self.sock.bind(self.locaddr)

        
    def sendMessage(self,TelloMessage):
        try:
            print("send message "+ TelloMessage +" end")
            msg = TelloMessage.encode(encoding="utf-8")
            sent = self.sock.sendto(msg,self.tello_address)
            data, server = self.sock.recvfrom(1518)
            return data.decode(encoding="utf-8")
        except:
            return "error in sending message" 

    # command takeoff land flip forward back left right up down cw ccw speed

    def connect(self):
        print("Connect")
        result = self.sendMessage("command")
        print (result)

    def end(self):
        print("end")
        self.sock.close()
        
    def takeOff(self):
        print("takeOff")
        #add the takeoff code
        result = self.sendMessage("takeoff") 
        print(result)

    def land(self):
        print("land")
        result = self.sendMessage("land")
        print(result)

    def flip(self, direction):
        print("flip")
        result = self.sendMessage("flip " + str(direction)) 
        print(result)

    def forward(self, distance):
        print("forward")
        result = self.sendMessage("forward " + str(distance))
        print(result)

    def back(self, distance):
        print("back")
        result = self.sendMessage("back " + str(distance)) 
        print(result)

    def left(self, distance):
        print("left")
        result = self.sendMessage("left " + str(distance)) 
        print(result)

    def right(self, distance):
        print("right")
        result = self.sendMessage("right " + str(distance)) 
        print(result)

    def up(self, distance):
        print("up")
        result = self.sendMessage("up " + str(distance)) 
        print(result)

    def down(self, distance):
        print("down")
        result = self.sendMessage("down " + str(distance)) 
        print(result)

    def cw(self, deg):
        print("cw")
        result = self.sendMessage("cw " + str(deg)) 
        print(result)

    def ccw(self, deg):
        print("ccw")
        result = self.sendMessage("ccw " + str(deg)) 
        print(result)

    def speed(self, speed):
        print("speed")
        result = self.sendMessage("speed " + str(speed)) 
        print(result)

    def battery(self):
        print ("battery")   
        result = self.sendMessage("battery?")
        return result