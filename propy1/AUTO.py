"""makes your Pi find red stuff and tell the motors what to do.

- Grabs frames from the camera.
- Looks for red objects and finds their center.
- Checks how far left/right the object is and nudges the motors (forward/left/right).
- Sets up GPIO pins and exposes simple functions: move_forward, turn_left, turn_right, stop_car.

Run this on a Raspberry Pi with a camera and motors hooked up. Press 'q' or Ctrl-C to quit.
"""

import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

# Motor control GPIO pins (CHANGE THESE TO MATCH YOUR WIRING)
MOTOR_A_IN1_PIN = 16  # Example
MOTOR_A_IN2_PIN = 18  # Example
MOTOR_B_IN3_PIN = 22  # Example
MOTOR_B_IN4_PIN = 24  # Example

# Camera frame dimensions
FRAME_WIDTH = 640
FRAME_HEIGHT = 480  # ADDED THIS LINE
CENTER_X = FRAME_WIDTH // 2

# Steering threshold (how many pixels off-center to trigger turning)
CENTER_THRESHOLD = 640

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # To prevent "channel already in use" warnings if you run multiple times

# Setup GPIO pins as outputs
GPIO.setup(MOTOR_A_IN1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_A_IN2_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B_IN3_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B_IN4_PIN, GPIO.OUT)

def stop_car():
    GPIO.output(MOTOR_A_IN1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B_IN3_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B_IN4_PIN, GPIO.LOW)
    print("Stopping")

def move_forward():
    GPIO.output(MOTOR_A_IN1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_A_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B_IN3_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B_IN4_PIN, GPIO.LOW)
    print("Moving Forward")

def turn_left():
    GPIO.output(MOTOR_A_IN1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A_IN2_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B_IN3_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B_IN4_PIN, GPIO.LOW)
    print("Turning Left")

def turn_right():
    GPIO.output(MOTOR_A_IN1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_A_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B_IN3_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B_IN4_PIN, GPIO.HIGH)
    print("Turning Right")

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        lower_red = np.array([170, 100, 100])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        red_mask = cv2.bitwise_or(mask1, mask2)

        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(largest_contour)
            object_x = x + w // 2
            error_x = object_x - CENTER_X

            if abs(error_x) < CENTER_THRESHOLD:
                move_forward()
            
            elif error_x > CENTER_THRESHOLD:
                move_forward()
                time.sleep(0.2)
            else:  # error_x < -CENTER_THRESHOLD
                move_forward()
                time.sleep(0.2)
        else:
            stop_car()

        # Optional: Display the frame with a center line
        cv2.line(frame, (CENTER_X, 0), (CENTER_X, FRAME_HEIGHT), (0, 255, 0), 1)
        cv2.imshow("Frame", frame)
        cv2.imshow("Red Mask", red_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopping car and cleaning up GPIO...")
finally:
    cap.release()
    cv2.destroyAllWindows()
    stop_car()
    GPIO.cleanup()