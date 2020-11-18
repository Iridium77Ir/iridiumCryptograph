from math import floor
from os import terminal_size, write
from textwrap import wrap
import math

class Cryptographer():
    def gen_key(password):
        encoded = password.encode('utf-8')
        if len(encoded) < 16:
            for i in range(16//len(encoded)):
                encoded += encoded
        return Cryptographer.make_arr_from_bytes(encoded[:16 - len(encoded)])

    def byte_xor(ba1, ba2):
        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

    def shift(a):
        for i in range(8):
            temp = a[(i+1)%3]
            a[(i+1)%3] = a[i%3]
            a[i%3] = temp
        return a

    def shift_arr(arr, key):
        for x in range(len(arr)):
            for i in range(len(key)):
                for j in range(ord(key[i][0])%4):
                    arr[x] = Cryptographer.shift(arr[x])
                for j in range(ord(key[i][1])%4):
                    arr[x] = Cryptographer.shift(arr[x])
                for j in range(ord(key[i][2])%4):
                    arr[x] = Cryptographer.shift(arr[x])
                for j in range(ord(key[i][3])%4):
                    arr[x] = Cryptographer.shift(arr[x])
            return arr
    
    def substitute_arr(arr, key): # Doesn't work
        for i in range(len(arr)):
            for j in range(4):
                for k in range(4):
                    if ord(key[j][k])%(j+k+1) == 0:
                        arr[i][j][k] = chr((ord(arr[i][j][k])+557056)%1114112).encode('utf-8')
        return arr

    def xor_arr(arr, key):
        for i in range(len(arr)):
            for j in range(4):
                for k in range(4):
                    arr[i][j][k] = Cryptographer.byte_xor(arr[i][j][k], key[j][k])
        return arr
        
    def make_arrays(msg):
        inputMsg = []
        keylen, msglen = 16, len(msg)

        for i in range(msglen//keylen):
            inputMsg.append(msg[i*keylen:(i+1)*keylen])
        if msglen%keylen != 0:
            inputMsg.append(msg[msglen//keylen * keylen:msglen] + str(16 - msglen%keylen).encode() * (16 - msglen%keylen))

        outputArr = []
        for i in range(len(inputMsg)):
            outputArr.append(Cryptographer.make_arr_from_bytes(inputMsg[i]))
        return outputArr

    def make_arr_from_bytes(key):
        outputArray = []
        for i in range(4):
            outputArray.append([])
            for j in range(4):
                outputArray[i].append(key[i*4 + j:i*4 + (j+1)])
        return outputArray

    def bytes_from_array(arr):
        outputMsg = b''
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                for z in range(len(arr [x][y])):
                    if x == len(arr)-1:
                        if arr[x][y][z].isdigit() == True:
                            for u in range(int(arr[x][y][z])):
                                if arr[x][y][z].isdigit() == True:
                                    pass
                                else:
                                    break
                        else:
                            outputMsg += arr[x][y][z]
                    else:
                        outputMsg += arr[x][y][z]
        return outputMsg

    def crypt(password, msg):
        key = Cryptographer.gen_key(password)
        arrays = Cryptographer.make_arrays(msg)
        
        # Permute arrays   
        arrays = Cryptographer.shift_arr(arrays, key) # Should return 16,4,4 array - Does not work, because of the reinfolge
        #
        #arrays = Cryptographer.substitute_arr(arrays, key) # Change some chars with some others - NOT WORKING
        arrays = Cryptographer.xor_arr(arrays, key)
        #
        arrays = Cryptographer.shift_arr(arrays, key) # Should return 16,4,4 array - Does not work, because of the reinfolge
        
        
        return Cryptographer.bytes_from_array(arrays)
