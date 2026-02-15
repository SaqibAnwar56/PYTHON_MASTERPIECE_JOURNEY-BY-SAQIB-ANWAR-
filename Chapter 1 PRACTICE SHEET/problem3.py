# 3. Install an external module and use it to perform an operation of your interest.  

# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Hello Saqib, welcome to Python world.")
# # engine.say("Muje paise chyee urgent plz.")
# engine.runAndWait()


import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  # Speed of voice
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

engine.say("Python is powerful and Saqib is learning fast.")
engine.runAndWait()
