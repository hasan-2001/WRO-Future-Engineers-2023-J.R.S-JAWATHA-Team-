from huskylib import HuskyLensLibrary
from spike import MotorPair

# Initialize the HUSKYLENS sensor
huskylens = HuskyLensLibrary()

# Initialize motors
motors = MotorPair('D', 'C')  # Adjust motor ports as needed


def move_forward():
    motors.start(50)  # Adjust speed as needed


def move_backward():
    motors.start(-50)  # Reverse direction, adjust speed as needed


def turn_left():
    motors.start(50)
    motors.turn(180)  # Adjust angle as needed


def turn_right():
    motors.start(50)
    motors.turn(-180)  # Adjust angle as needed


def stop_movement():
    motors.stop()


# Define a function for object detection and robot movement
def object_detection_and_movement():
    # Start the HuskyLens module
    huskylens.begin()

    # Set the module to recognize objects
    huskylens.writeAlgorithm("ALGORITHM_OBJECT_TRACKING")

    while True:
        huskylens.request()

        if huskylens.available():
            for block in huskylens.read():
                if block[8] == 3:  # Recognized object ID
                    object_id = block[10]
                    center_x = block[1]
                    center_y = block[2]

                    # Process object detection data and control robot movement
                    if object_id == 1:  # Assume object ID 1 is the target object
                        if center_x < 100:
                            # Turn left
                            turn_left()
                        elif center_x > 200:
                            # Turn right
                            turn_right()
                        else:
                            # Move forward
                            move_forward()
                    else:
                        # Stop if an unrecognized object is detected
                        stop_movement()


# Main program
def main():
    # Initialize any other necessary components (e.g., motors, sensors)

    # Call the object_detection_and_movement function
    object_detection_and_movement()

    # Release resources (if necessary)
    huskylens.end()


# Helper function to wait for a specified duration in milliseconds
def wait(duration):
    import time
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        pass


# Call the main function to start the program
if __name__ == "__main__":
    main()
