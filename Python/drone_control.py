import airsim

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

while True:
    text = input()
    word = text.split(" ")
    if word[0] == "takeoff":
        client.takeoffAsync().join()
        client.hoverAsync().join()
    elif word[0] == "land":
        client.landAsync().join()
    elif word[0] == "move":
        try:
            client.moveByVelocityBodyFrameAsync(float(word[1]), float(word[2]), float(word[3]), float(word[4])).join()
            client.hoverAsync().join()
        except:
            print("DUH")
    elif word[0] == "moveto":
        try:
            client.moveToPositionAsync(float(word[1]), float(word[2]), float(word[3]), float(word[4])).join()
            client.hoverAsync().join()
        except:
            print("DUH")
    elif word[0] == "quit":
        break
    else:
        print("Dafuq")

client.armDisarm(False)
client.enableApiControl(False)