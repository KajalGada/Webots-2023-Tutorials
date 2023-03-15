"""obstacle_avoidance controller."""


from controller import Robot


# get the time step of the current world.
TIMESTEP = 32
MAX_SPEED = 6.28


def run_robot(robot):

    # Motor instance to drive robot
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # IR sensors to detect obstalces
    list_ps = []
    for ind in [0, 1, 2, 5, 6, 7]:
        sensor_name = 'ps' + str(ind)
        list_ps.append(robot.getDevice(sensor_name))
        list_ps[-1].enable(TIMESTEP)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
    
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED
        
        # Read the sensors:
        for ps in list_ps:
            ps_val = ps.getValue()
            
            # Process sensor data here.
            if ps_val > 100:
                # turn
                left_speed = -MAX_SPEED
   
        # Drive robot
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
