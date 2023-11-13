import socket
import matplotlib.pyplot as plt
import numpy as np

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

def centroid(labeled, label=1):
    pos = np.where(labeled == label)
    return pos[0].mean(), pos[1].mean()

def neighbours(img, i, j):
    return [img[i + 1, j], img[i - 1, j], img[i, j - 1], img[i, j + 1]]

host = "84.237.21.36"
port = 5152

plt.ion()
plt.figure()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    beat = b"nope"
    while beat != b"yep":
        sock.send(b"get")
        
        bts = recvall(sock, 40002)
        print(len(bts))

        img = np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0], bts[1])
        posMax = []
        for i in range(1, len(img) - 1):
            for j in range(1, len(img) - 1):
                if all(img[i, j] > n for n in neighbours(img, i, j)):
                    posMax.append([i, j])
        pos1 = posMax[0]
        pos2 = posMax[1]
        res = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
        print(round(res, 1))

        sock.send(f"{round(res, 1)}".encode())
        print(sock.recv(4).decode())
        
        plt.clf()
        plt.title(str(pos1) + str(pos2))
        plt.imshow(img)
        plt.pause(1)

        sock.send(b"beat")
        beat = sock.recv(20)
