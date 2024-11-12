# Balancing Cube

Run main.py

Currently, only 3d animation works. The animation is hooked up to a sinusoidal angle input that rotates the cube about a vector pointing in the xy plane:

For right now, it seems the easiest way to do control is to define the angle between the vertical z axis and the vector line which goes from the corner of the cube that coincides with the origin of the inertial frame and the center of the cube, which we can denote by $\beta$. The goal of this control exercise is to get the cube to balance on this corner, so we would like to drive $\beta$ to zero. The cube will have 3 reaction wheels, which can provide reaction-moments in each of the 3 body-fixed axes directions. 

The dynamics of the cube will be difficult to model, since the cube will be in some rotated frame w.r.t the inertial frame, and so we might not be able to 

The dynamics of the system are obviously going to be non-linear, but we should start with a linear controller which is linearized about the $\beta$ = 0 point. We can go from there. There are also other major non-linearities that will be present -- mainly, the fact that the xy plane is "ground" and the cube will collide with it at any point. This can be handled much later on. 




