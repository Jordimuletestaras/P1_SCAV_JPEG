import os
import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp


def encode(message):
    encoded_message = ""
    i = 0

    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + ch
        i = j + 1
    return encoded_message


if __name__ == '__main__':
    input = "111100000101010000111"
    print(encode(input))

    # https://www.geeksforgeeks.org/run-length-encoding-python/
