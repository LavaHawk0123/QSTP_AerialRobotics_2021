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

        #Calling Plotting Function
        self.plotAxis()

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
        self.x_dash = (orig_x-h)*Cos + (orig_y-k)*Sin
        self.y_dash = -(orig_x-h)*Sin + (orig_y-k)*Cos
    
    def findAxis(self,x,y):
        # To find the axis points for the transformed coordinate axis

        Sin = math.sin(self.angle)
        Cos = math.cos(self.angle)
        axis_x = x+self.sh_x + (x)*Cos + (y)*Sin
        axis_y = y + self.sh_y - (x)*Sin + (y)*Cos
        return axis_x,axis_y

    def plotAxis(self):
        #Function call to get axis points
        shifted_axis_x1,shifted_axis_x2 = self.findAxis(0,15)
        shifted_axis_y1,shifted_axis_y2 = self.findAxis(15,0)

        # Setting Axis points 
        x1, y1 = [0, self.og_x+5], [0, 0]
        x2, y2 = [0, 0], [0, self.og_y+5]
        x1_sh, y1_sh = [self.sh_x,shifted_axis_x1], [self.sh_y, shifted_axis_x2]
        x2_sh, y2_sh = [self.sh_x,shifted_axis_y1], [self.sh_y, shifted_axis_y2]
        x_coordinates = [self.og_x, self.sh_x]
        y_coordinates = [self.og_y, self.sh_y]

        #Plotting Axis lines
        plt.plot(x1, y1, x2, y2, marker = 'o')
        plt.plot(x1_sh, y1_sh, x2_sh, y2_sh, marker = 'o')

        #Plotting Points
        plt.scatter(x_coordinates, y_coordinates)

        #Defining Axis Labels
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Transformation of Axis')

        #Creating Plot
        plt.show()

#Main Call of class constructor
if __name__ == "__main__":
    Transform()
