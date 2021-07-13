#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import math



class Transform:

    #init function call
    def __init__(self):
        # Arguments for transformPoint(A,B,Theta)
        # A is the Point wrt initial frame
        # B is the shifted origin of the coordinate frame
        # Theta specifies the angle with which the giver coordinate frame is rotated
        self.og_x,self.og_y= input("Enter the x and y coordinate as x,y : ")
        self.sh_x,self.sh_y = input("Enter the shifted origin as x,y : ")
        self.angle = input("Enter the angle of rotation : ")
        print("The initial coordinate wrt the axis is ({},{})".format(self.og_x,self.og_y))

        #Creating list of points
        self.initial = [self.og_x,self.og_y]
        self.shifted = [self.sh_x,self.sh_y]

        #Calling Transformation Function
        self.transformPoint(self.initial,self.shifted,self.angle)
        print("The transformed coordinate wrt the shifted axis is ({},{})".format(self.x_dash,self.y_dash))


    def transformPoint(self,A,B,Theta):
        #Declerations
        orig_x = A[0]
        orig_y = A[1]
        h = B[0]
        k = B[1]
        angle = Theta


        #Calculations for transformation
        Sin = math.sin(angle)
        Cos = math.cos(angle)
        A = np.zeros((2,2))
        A[0][0]=np.float(Cos)
        A[1][1]= np.float(Cos)
        A[0][1] = np.float(-Sin)
        A[1][0] = np.float(Sin)
        #print(A)
        X = np.zeros((2,1))
        X[0][0] = orig_x-h
        X[1][0] = orig_y-k
        rot = np.matmul(A,X)
        #print(rot)
        self.x_dash = rot[1][0]
        self.y_dash = rot[0][0]
    

#Main Call of class constructor
if __name__ == "__main__":
    Transform()
