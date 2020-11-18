# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

# array de conversion de RGB a YUV
RGB_to_YUV = np.array([[0.299, 0.587, 0.114], [-0.147, -0.289, 0.436], [0.615, -0.515, -0.1]])

# array de conversión YUV a RPG (inversa)
YUV_to_RGB = np.linalg.inv(RGB_to_YUV)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Rvalue= int(255)
    Gvalue= int(155)
    Bvalue= int(55)
    # Creamos un array con los valores RGB y normalizamos (entre 0 y 1)
    rgbValue = np.array([[Rvalue / 255.], [Gvalue / 255.], [Bvalue / 255.]])
    # Aplicamos la conversion
    yuvValue=np.dot(RGB_to_YUV, rgbValue)

