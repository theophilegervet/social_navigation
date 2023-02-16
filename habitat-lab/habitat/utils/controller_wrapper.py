import numpy as np
from home_robot.control.goto_controller import GotoVelocityController
from omegaconf import OmegaConf


class ContinuousController:
    """Wrapper around the velocity controller in home_robot"""

    def __init__(
        self,
        v_max=1.0,
        w_max=1.0,
        acc_lin=2.4,
        acc_ang=2.4,
        max_heading_ang=np.pi / 10,
        lin_error_tol=0.001,
        ang_error_tol=0.001,
        track_yaw=True,
    ):
        # Generate config
        cfg_dict = {
            "v_max": v_max,
            "w_max": w_max,
            "acc_lin": acc_lin,
            "acc_ang": acc_ang,
            "tol_lin": lin_error_tol,
            "tol_ang": ang_error_tol,
            "max_heading_ang": max_heading_ang,
        }
        cfg = OmegaConf.create(cfg_dict)

        # Instatiate controller
        self.controller = GotoVelocityController(cfg)
        self.controller.set_yaw_tracking(track_yaw)

    def set_goal(self, goal: np.ndarray, vel_goal=None):
        """Update controller goal
        goal: Desired robot base SE2 pose in global frame
        """
        self.controller.update_goal(goal)

    def forward(self, xyt, *args, **kwargs):
        """Query controller to compute velocity command
        xyt: Robot base current SE2 pose in global frame
        """
        # Update state feedback
        self.controller.update_pose_feedback(xyt)
        # Compute velocity control
        return self.controller.compute_control()