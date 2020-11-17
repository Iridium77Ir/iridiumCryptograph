from math import floor
from os import write
from textwrap import wrap
import math


class Cryptographer():
    def gen_key(password):
        encoded = password.encode()
        if len(encoded) < 16:
            for i in range(16//len(encoded)):
                encoded += encoded
        return Cryptographer.make_arr_from_bytes(encoded[:16 - len(encoded)])

    def byte_xor(ba1, ba2):
        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

    # Shift array functions
    def shift_right(a):
        return a
    def shift_left(a):
        return a
    def shift_up(a):
        return a
    def shift_down(a):
        return a

    def shift_arr(arr, key):
        for i in range(len(key)):
            for j in range(ord(key[i][0])%4):
                arr = Cryptographer.shift_right(arr)
            for j in range(ord(key[i][1])%4):
                arr = Cryptographer.shift_left(arr)
            for j in range(ord(key[i][2])%4):
                arr = Cryptographer.shift_up(arr)
            for j in range(ord(key[i][3])%4):
                arr = Cryptographer.shift_down(arr)
        return arr
    
    def substitute_arr(arr, key):
        for i in range(len(arr)):
            for j in range(4):
                for k in range(4):
                    if ord(key[j][k])%(j+k+1) == 0:
                        arr[i][j][k] = chr((ord(arr[i][j][k])+64)%128).encode()
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
            inputMsg.append(msg[msglen//keylen * keylen:msglen] + b' ' * (16 - msglen%keylen))

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
        for x in arr:
            for y in x:
                for z in y:
                    outputMsg += z
        return outputMsg

    def crypt(password, msg):
        key = Cryptographer.gen_key(password)
        arrays = Cryptographer.make_arrays(msg)
        
        # Permute arrays   
        arrays = Cryptographer.shift_arr(arrays, key) # Should return 16,4,4 array - Does not work, because of the reinfolge
        #
        arrays = Cryptographer.substitute_arr(arrays, key) # Change some chars with some others - WORKING
        arrays = Cryptographer.xor_arr(arrays, key)
        #
        arrays = Cryptographer.shift_arr(arrays, key) # Should return 16,4,4 array - Does not work, because of the reinfolge
        
        
        return Cryptographer.bytes_from_array(arrays)
