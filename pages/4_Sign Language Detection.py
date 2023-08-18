import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import tempfile
import base64

st.write("---")
st.title("SIBI Sign Language Translator using LSTM and Mediapipe")

st.write("---")
st.subheader('Project Overview')
st.markdown("""
<p style='text-align: justify;'>
Sign language is vital for deaf communities, and in Indonesia, SIBI is a recognized and structured sign language. 
Traditional human interpreters aren't always efficient, so in the Industry 4.0 era, a deep learning-based sign language translation system presents a promising solution. 
By training on valid SIBI sign movements, we aim to develop a precise web application that detects dynamic SIBI gestures, catering to both deaf and hearing individuals.
The system will utilizing Mediapipe Hand Landmark as a input processing for the LSTM model. This page will also delve into the ML model making process and analysis
</p>
""", unsafe_allow_html=True)
st.write("Keypoints : Sign Language, Deep Learning, Mediapipe, LSTM")


st.write("---")
st.subheader('Mediapipe Hand Landmark')
st.markdown("""
<p style='text-align: justify;'>
In this section, we delve into the core mechanics of the Mediapipe HandLandmark detection system. At its heart lies a sophisticated fusion of computer vision and machine learning techniques. 
By leveraging an intricate neural network architecture, the system can accurately pinpoint and track key landmarks on the human hand, capturing even the subtlest of movements with remarkable precision. 
Through a cascade of processing stages, the technology first detects the hand's presence, then proceeds to recognize and monitor its individual landmarks – from fingertip positions to palm orientation. 
This granular data is processed in real-time, enabling the system to interpret complex sign language gestures with unparalleled accuracy.
As we unravel the layers of this advanced methodology, a deeper understanding emerges of how Mediapipe HandLandmark paves the way for dynamic, inclusive communication through its breakthrough hand gesture recognition capabilities.
</p>
""", unsafe_allow_html=True)
st.write("[Documentation >](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)")
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils 

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img, results = self.mediapipe_detection(img, self.holistic)
        self.draw_styled_landmarks(img, results)

        return img

    def mediapipe_detection(self, img, model):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = model.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img, results

    def draw_landmarks(self, img, results):
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    def draw_styled_landmarks(self, img, results):
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                ) 
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                )

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)


st.write("---")
st.subheader('LSTM Model Development')
st.markdown('<h2 style="font-size: 31px; text-align: center;">🙀 Sorry This Section is Under Development 😿</h2>', unsafe_allow_html=True)

st.write("---")
st.subheader('LSTM Model Analysis')
st.markdown('<h2 style="font-size: 31px; text-align: center;">🙀 Sorry This Section is Under Development 😿</h2>', unsafe_allow_html=True)

st.write("---")
st.write("#")
st.write("#")
mp_holistic = mp.solutions.holistic  # Holistic model

actions = ['aku', 'apa', 'bagaimana', 'berapa', 'di', 'halo', 'I', 'J', 'K', 'kamu', 'kapan', 'ke', 'kita', 'makan', 'mana', 'minum', 'nama', 'saya', 'siapa', 'Z'] #realtimemodel


@st.cache_resource
def load_custom_model():
    return load_model('pages/translateV17.h5')

model = load_custom_model()

threshold = 0.5

class VideoTransformer():
    def __init__(self):
        self.holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.sequence = []
        self.sentence = []

    def extract_keypoints(self, results):
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([lh, rh])

    def transform(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = self.holistic.process(image_rgb)
        image_rgb.flags.writeable = True
        image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        keypoints = self.extract_keypoints(results)

        try:
            self.sequence.append(keypoints)
            self.sequence = self.sequence[-15:]
        except NameError:
            self.sequence = [keypoints]

        if len(self.sequence) == 15:
            try:
                res = model.predict(np.expand_dims(self.sequence, axis=0))[0]

                if res[np.argmax(res)] > threshold:
                    self.sentence.append(actions[np.argmax(res)])

                if len(self.sentence) > 1:
                    self.sentence = self.sentence[-1:]
            except Exception as e:
                print("No sentence detected:", str(e))

        return image_rgb

st.markdown(
    """
    <style>
    .bar {
        background-color: rgb(114, 134, 211);
        height: 35px;
    }
    .sentence {
        font-size: 21px;
    }
    .subheader {
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="bar"></div>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center;">Sign Language Detection</h1>', unsafe_allow_html=True)

for _ in range(5):
    st.markdown("")
    
url = 'https://bit.ly/KataSIBI'
st.write("[Watch the demo first !! >](https://drive.google.com/file/d/1-VtTWXQCHm1J_ZEf5QLk6bJQDcQc6YBb/view?usp=sharing)")
st.markdown(f'''
<a href={url}><button style="font-size: 13px; color: white;background-color:rgb(114, 134, 211);">click to see dataset</button></a>
''',
unsafe_allow_html=True)
st.write("[Try with the provided test data here! >](https://drive.google.com/drive/folders/1iFAW6sUos9oFMhbxbCywFTanBcBNibsk?usp=sharing)")
uploaded_file = st.file_uploader("Upload a video (max. 5 second)", type=["mp4"])
flip_the_video = st.checkbox("check for mirrored video")

st.markdown('<h2 style="font-size: 21px;">Note: can only detecting one gesture at a time!</h2>', unsafe_allow_html=True)


if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filepath = temp_file.name
    
    st.video(temp_filepath)

    video = cv2.VideoCapture(temp_filepath)

    video_transformer = VideoTransformer()

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if flip_the_video == True:
                frame = cv2.flip(frame, 1)
        elif flip_the_video == False:
                pass
        transformed_frame = video_transformer.transform(frame)

    video.release()

    st.markdown('<h2 style="font-size: 27px;">Detection Result:</h2>', unsafe_allow_html=True)

    st.write('<div class="sentence">' + ' '.join(video_transformer.sentence) + '</div>', unsafe_allow_html=True)
