import cv2
import mediapipe as mp
import pyautogui

# Initialize camera and hand tracking
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()

# Compute screen scaling factors once
scale_x, scale_y = screen_w / cap.get(3), screen_h / cap.get(4)

is_dragging = False  # Flag for dragging
prev_index_y = None  # Store previous index finger Y-position

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            index_x = index_y = 0
            thumb_x = thumb_y = 0
            middle_x = middle_y = 0  # Middle finger coordinates

            for idx, landmark in enumerate(landmarks):
                x, y = int(landmark.x * frame_w), int(landmark.y * frame_h)

                if idx == 8:  # Index finger tip
                    cv2.circle(frame, (x, y), 15, (0, 255, 255))
                    index_x, index_y = x * scale_x, y * scale_y
                    pyautogui.moveTo(index_x, index_y)

                if idx == 4:  # Thumb tip
                    cv2.circle(frame, (x, y), 15, (255, 0, 0))
                    thumb_x, thumb_y = x * scale_x, y * scale_y

                if idx == 12:  # Middle finger tip (for right-clicking & scrolling)
                    cv2.circle(frame, (x, y), 15, (255, 255, 0))
                    middle_x, middle_y = x * scale_x, y * scale_y

            # Click if the index finger and thumb are close
            if abs(index_y - thumb_y) < 20:
                if not is_dragging:  # Prevent multiple click events
                    print("Click detected")
                    pyautogui.click()
                    pyautogui.sleep(0.5)

            # Dragging: If index and thumb are close, hold the click
            if abs(index_y - thumb_y) < 10:
                if not is_dragging:
                    print("Dragging started")
                    pyautogui.mouseDown()
                    is_dragging = True
            else:
                if is_dragging:
                    print("Dragging stopped")
                    pyautogui.mouseUp()
                    is_dragging = False

            # Right-click if the middle finger and thumb are close
            if abs(middle_y - thumb_y) < 20:
                print("Right-click detected")
                pyautogui.rightClick()
                pyautogui.sleep(0.5)  # Prevent multiple clicks

            # Scrolling Gesture (Index finger moving up/down while middle is extended)
            if prev_index_y is not None and abs(prev_index_y - index_y) > 20:
                if index_y < prev_index_y:  # Moving up
                    print("Scrolling Up")
                    pyautogui.scroll(20)
                else:  # Moving down
                    print("Scrolling Down")
                    pyautogui.scroll(-20)

            # Update previous index Y-position
            prev_index_y = index_y

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
