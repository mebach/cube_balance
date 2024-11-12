import numpy as np
import cubeParam as P


class cubeController:
    def __init__(self):

        self.error_d1 = 0.0
        self.K = P.K  # state feedback gain
        self.kp = P.kp
        self.kd = P.kd

        x = np.array([
            [P.beta0],  # initial cube angle
            [P.betadot0]   # initial cube angular velocity
        ])

        self.ki = P.ki
        self.integrator = self.K @ x / (-self.ki)
        self.limit = P.F_max  # max force
        self.Ts = P.Ts  # sample rate of the controller

    def update(self, x_r, x):
        state_error = x - x_r

        tau_unsat = -self.K @ state_error
        tau_sat = self.saturate(tau_unsat)

        return tau_sat

    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit * np.sign(u)
        return u
