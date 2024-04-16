
from django.shortcuts import render
from django.http import JsonResponse
import cv2
import mediapipe as mp
import pyautogui

# Initialize face mesh for eye gesture tracking
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Function to capture webcam feed and detect eye gestures
def capture_and_detect_eye_gestures():
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)

# Chatbot view
def chatbot(request):
    # Start a separate thread to capture and detect eye gestures
    import threading
    t = threading.Thread(target=capture_and_detect_eye_gestures)
    t.start()

    # Return the rendered HTML template
    return render(request, 'chatbot.html')


# from django.conf import settings
# from .utils import get_answer # text_to_speech, speech_to_text
# import os

# # Initialize session state for managing chat messages
# def initialize_session_state(request):
#     if "messages" not in request.session:
#         request.session["messages"] = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

# def chatbot(request):
#     #initialize_session_state(request)
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         print(message)
#         # if message:
#         #     request.session["messages"].append({"role": "user", "content": message})
#             # Process user message and get response
#             #final_response = get_answer(request.session["messages"])
#         final_response = get_answer(message)
#         print(final_response)
#             # Convert response to speech
#             # audio_file = text_to_speech(final_response)
#             # # Add response to session messages
#             # request.session["messages"].append({"role": "assistant", "content": final_response})
#             # os.remove(audio_file)  # Clean up audio file
#             # return JsonResponse({'response': final_response})
#     return render(request, 'chatbot.html')#, {'messages': request.session.get("messages", [])})
