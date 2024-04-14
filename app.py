"""
    Puzzly - A puzzle game project
 
    (C) 2024 Yasmine EL AAFIA <elaafiayasmine@gmail.com>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Puzzly is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time

import speech_recognition as sr
from pyniryo import NiryoRobot
from flask import Flask, request
from utils import *

robot: NiryoRobot | None = None

app = Flask(__name__)

def detecter_voix(audio_file):
    """
    Args:
        audio_file : The audio file

    Raises:
        SpeechException
        SpeechException

    Returns:
        texte (str): The text that is recongized
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        print("Processing audio file...")
        audio = recognizer.record(source)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + texte)
        return texte
    except sr.UnknownValueError as uv:
        print(f"Impossible de comprendre l'audio {uv}")
        raise SpeechException(msg="Impossible de comprendre l'audio")
    except sr.RequestError as r:
        print("Erreur lors de la requête à Google Speech Recognition service; {0}".format(r))
        raise SpeechException(msg="Erreur lors de la requête à Google Speech Recognition service")

@app.route("/", methods=["GET"])
def hello():
    return "HIIII", 200

@app.route('/command', methods=['POST'])
def command():
    global robot
    try:
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        if file:
            
            print("WE GOT THE COMMAND!!")
            
            commande = detecter_voix(file)
            
            if robot is None:
                if commande == "observation":
                    robot = NiryoRobot("169.254.200.200")
                    robot.calibrate_auto()
                    robot.move_joints([0.00, 0.08, -0.11, -0.06, -1.46, 2.53])
                else:
                    raise CommandException(msg="Pas encore de connextion avec Niryo, dites 'observation'")
            else:
                if commande == "en haut":
                    robot.move_joints([-0.02, -0.51, 0.09, -0.07, -1.17, 2.53])

                elif commande == "en bas":
                    robot.move_joints([-0.01, -0.02, -0.22, -0.01, -1.27, 2.53])

                elif commande == "à gauche":
                    robot.move_joints([-0.12, -0.31 , -0.13, -0.10, -1.17, 2.53])

                elif commande == "à droite":
                    robot.move_joints([0.14, -0.33, -0.13, -0.09, -1.17, 2.53])

                elif commande == "quitter":
                    robot.close_connection()
                    robot = None
                
                else:
                    raise CommandException(msg="Commande inconnue")

            return commande, 200
    except Exception as e:
        return f"{e}" ,500
