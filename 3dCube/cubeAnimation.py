import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import sys
sys.path.append('../..')  # add parent directory
import numpy as np
import cubeParam as P
from scipy.spatial.transform import Rotation


class cubeAnimation:
    '''
        Create cube animation
    '''
    def __init__(self):
        self.flagInit = True                  # Used to indicate initialization
        self.fig = plt.figure()               # Initializes a figure and axes object
        self.handle = []                      # Initializes a list object that will
                                              # be used to contain handles to the
                                              # patches and line objects.
        self.length = P.l

        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_zlim(0, 1.5)


        self.cube = np.zeros([8, 3])
        # Define initial x values
        self.cube[:,0] = [0, 0, 0, 0, 1, 1, 1, 1]
        # Define initial y values
        self.cube[:,1] = [0, 1, 0, 1, 0, 1, 0, 1]
        # Define initial z values
        self.cube[:,2] = [0, 0, 1, 1, 0, 0, 1, 1]

        self.cube_vertex0 = np.array([[0],[0],[0]])
        self.cube_vertex1 = np.array([[P.l],[0],[0]])
        self.cube_vertex2 = np.array([[P.l],[P.l],[0]])
        self.cube_vertex3 = np.array([[0],[P.l],[0]])
        self.cube_vertex4 = np.array([[0],[0],[P.l]])
        self.cube_vertex5 = np.array([[P.l],[0],[P.l]])
        self.cube_vertex6 = np.array([[P.l],[P.l],[P.l]])
        self.cube_vertex7 = np.array([[0],[P.l],[P.l]])

        self.cube_vertices = np.hstack((self.cube_vertex0, self.cube_vertex1, self.cube_vertex2, self.cube_vertex3, self.cube_vertex4, self.cube_vertex5, self.cube_vertex6, self.cube_vertex7))
        self.current_cube_vertices = self.cube_vertices

        self.faces = np.zeros([6, 5, 3])

        # Bottom face
        self.faces[0, :,0] = [0,0,1,1,0]
        self.faces[0, :,1] = [0,1,1,0,0]
        self.faces[0, :,2] = [0,0,0,0,0]
        # Top face
        self.faces[1, :,0] = [0,0,1,1,0]
        self.faces[1, :,1] = [0,1,1,0,0]
        self.faces[1, :,2] = [1,1,1,1,1]
        # Left Face
        self.faces[2, :,0] = [0,0,0,0,0]
        self.faces[2, :,1] = [0,1,1,0,0]
        self.faces[2, :,2] = [0,0,1,1,0]
        # Left Face
        self.faces[3, :,0] = [1,1,1,1,1]
        self.faces[3, :,1] = [0,1,1,0,0]
        self.faces[3, :,2] = [0,0,1,1,0]
        # front face
        self.faces[4, :,0] = [0,1,1,0,0]
        self.faces[4, :,1] = [0,0,0,0,0]
        self.faces[4, :,2] = [0,0,1,1,0]
        # front face
        self.faces[5, :,0] = [0,1,1,0,0]
        self.faces[5, :,1] = [1,1,1,1,1]
        self.faces[5, :,2] = [0,0,1,1,0]
    


    def update(self, u):
        # Process inputs to function
        psi = u[0]
        theta = u[1]   # angle of the cube of cart
        phi = u[2]
        

        self.drawCube(psi, theta, phi)

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def drawCube(self, psi, theta, phi):
        self.calculateVertices(psi, theta, phi)
        self.reconstructFaces()

        self.ax.clear()
        self.ax.add_collection3d(Poly3DCollection(self.faces, facecolors='cyan', linewidths=1, edgecolors='k', alpha=0.25))
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_zlim(-1.5, 1.5)
        self.ax.set_aspect('equal')


    def calculateVertices(self, psi, theta, phi):
        # R = Rotation.from_euler('xy', [psi, theta], degrees=False)
        R = Rotation.from_rotvec(psi * np.array([np.sqrt(2)/2, -np.sqrt(2)/2, 0]))

        # print(R.as_matrix())
        
        self.current_cube_vertices = R.as_matrix() @ self.cube_vertices
        print(self.current_cube_vertices[:,6])
        

    def reconstructFaces(self):

        # Bottom Face
        self.faces[0, 0, :] = self.current_cube_vertices[:,0]
        self.faces[0, 1, :] = self.current_cube_vertices[:,1]
        self.faces[0, 2, :] = self.current_cube_vertices[:,2]
        self.faces[0, 3, :] = self.current_cube_vertices[:,3]
        self.faces[0, 4, :] = self.current_cube_vertices[:,0]

        # Front Face
        self.faces[1, 0, :] = self.current_cube_vertices[:,1]
        self.faces[1, 1, :] = self.current_cube_vertices[:,2]
        self.faces[1, 2, :] = self.current_cube_vertices[:,6]
        self.faces[1, 3, :] = self.current_cube_vertices[:,5]
        self.faces[1, 4, :] = self.current_cube_vertices[:,1]

        # Right Face
        self.faces[2, 0, :] = self.current_cube_vertices[:,2]
        self.faces[2, 1, :] = self.current_cube_vertices[:,3]
        self.faces[2, 2, :] = self.current_cube_vertices[:,7]
        self.faces[2, 3, :] = self.current_cube_vertices[:,6]
        self.faces[2, 4, :] = self.current_cube_vertices[:,2]

        # Back Face
        self.faces[3, 0, :] = self.current_cube_vertices[:,3]
        self.faces[3, 1, :] = self.current_cube_vertices[:,0]
        self.faces[3, 2, :] = self.current_cube_vertices[:,4]
        self.faces[3, 3, :] = self.current_cube_vertices[:,7]
        self.faces[3, 4, :] = self.current_cube_vertices[:,3]

        # Left Face
        self.faces[4, 0, :] = self.current_cube_vertices[:,0]
        self.faces[4, 1, :] = self.current_cube_vertices[:,1]
        self.faces[4, 2, :] = self.current_cube_vertices[:,5]
        self.faces[4, 3, :] = self.current_cube_vertices[:,4]
        self.faces[4, 4, :] = self.current_cube_vertices[:,0]

        # Top Face
        self.faces[5, 0, :] = self.current_cube_vertices[:,4]
        self.faces[5, 1, :] = self.current_cube_vertices[:,5]
        self.faces[5, 2, :] = self.current_cube_vertices[:,6]
        self.faces[5, 3, :] = self.current_cube_vertices[:,7]
        self.faces[5, 4, :] = self.current_cube_vertices[:,4]
        


        

