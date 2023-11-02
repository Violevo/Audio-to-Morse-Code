#imports
import speech_recognition as sr
from gpiozero import LED
import time

led = LED(17)
num = 0
previousresult = None

while 1:
    # setting buzzer pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(14,GPIO.OUT)

    # buzzer code
    def dot():
        # Buzzer on
        led.on()
        # hold for one second
        time.sleep(1)

        # Buzzer off
        led.off

    def dash():
        # Buzzer on
        led.on()
        # hold for three seconds
        time.sleep(3)

        # Buzzer off
        led.off()

    filename = "Output.wav"

    r = sr.Recognizer()

    try:
        # open the file
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)

        # Dictionary representing the morse code chart
        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                            'C': '-.-.', 'D': '-..', 'E': '.',
                            'F': '..-.', 'G': '--.', 'H': '....',
                            'I': '..', 'J': '.---', 'K': '-.-',
                            'L': '.-..', 'M': '--', 'N': '-.',
                            'O': '---', 'P': '.--.', 'Q': '--.-',
                            'R': '.-.', 'S': '...', 'T': '-',
                            'U': '..-', 'V': '...-', 'W': '.--',
                            'X': '-..-', 'Y': '-.--', 'Z': '--..',
                            '1': '.----', '2': '..---', '3': '...--',
                            '4': '....-', '5': '.....', '6': '-....',
                            '7': '--...', '8': '---..', '9': '----.',
                            '0': '-----', ', ': '--..--', '.': '.-.-.-',
                            '?': '..--..', '/': '-..-.', '-': '-....-',
                            '(': '-.--.', ')': '-.--.-', }

        message = text.replace("'", "")

        # according to the morse code chart
        def encrypt(message):
            cipher = ''
            for letter in message:
                if letter != ' ':

                    # Looks up the dictionary and adds the
                    # corresponding morse code
                    # along with a space to separate
                    # morse codes for different characters
                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:
                    # 1 space indicates different characters
                    # and 2 indicates different words
                    cipher += ' '

            return cipher

        result = encrypt(message.upper())

        if result != previousresult:

            print(result)

            for i in range(0, len(result)):
                if (result[i]) == ".":
                    dot()

                if (result[i]) == "-":
                    dash()

                else:
                    time.sleep(7)

        previousresult = result

    except sr.UnknownValueError:
        # no voice found
        print ("Waiting...")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {str(e)}")
