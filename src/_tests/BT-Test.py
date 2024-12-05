# File Name: BT-Test.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import asyncio
from bleak import BleakScanner
import os

#* Custom Libraries *#

import utilities.mongoDB.mongoIN as mongoIN

#^ Variables ^#

#~ create and store variables here

#& Functions &#

def clear():
    os.system("clear")

def rssiToDistance(rssi):    
  n=2
  mp=-69
  return round(10 ** ((mp - (int(rssi)))/(10 * n)),2)  

async def detect_devices():
    listd = []
    devices = await BleakScanner.discover()
    for device in devices:
        data = mongoIN.jarvisSettings("Bluetooth.ConnectionInfo", "BluetoothAddrs")
        if device.address in data.values():
            rssiVal = device.rssi
            distance = rssiToDistance(rssiVal)
            #clear()
            text = {f"{str(device.name)}": distance}
            listd.append(text)
        else:
            pass
    clear
    for i in range(len(listd)):
        for items in listd[i]:
            print(items)
            print(listd[i][items], "meters")

async def discover_devices2():
    fl = []
    nl = []
    devices = await BleakScanner.discover()
    for device in devices:
            rssiVal = device.rssi
            distance = rssiToDistance(rssiVal)
            #clear()
            fl.append(distance)
            #print(f"Device: {device.name}, Address: {device.address}, RSSI: {device.rssi}, Distance From Me: {distance} meters")
    rl = []
    devices2 = await BleakScanner.discover()
    for device2 in devices2:
            rssiVal2 = device2.rssi
            distance2 = rssiToDistance(rssiVal2)
            rl.append(distance2)
    yl = []
    devices3 = await BleakScanner.discover()
    for device3 in devices3:
            rssiVal3 = device3.rssi
            distance3 = rssiToDistance(rssiVal3)
            yl.append(distance3)
    fl.sort(reverse=True)
    rl.sort(reverse=True)
    yl.sort(reverse=True)
    nl.append(fl[0])
    nl.append(fl[1])
    nl.append(fl[2])
    nl.append(rl[0])
    nl.append(rl[1])
    nl.append(rl[2])
    nl.append(yl[0])
    nl.append(yl[1])
    nl.append(yl[2])
    nl.sort(reverse=True)
    clear()
    print(nl)

#= Classes =#

#~ define and build classes here

#! Main Program !#

asyncio.run(detect_devices())
#asyncio.run(discover_devices2())
#rssiVal = asyncio.run(bleak.BleakClientCoreBluetooth(address_or_ble_device="D74C1A6A-67E1-0FA1-3146-7AE1B65F046C").get_rssi())
#print(rssiVal)
#print(rssiToDistance(rssiVal))



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#