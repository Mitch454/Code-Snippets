import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# change the speech rate
engine.setProperty('rate',250)

# get the available voices 
voices = engine.getProperty('voices')

# choose a voice based on the voice id
engine.setProperty('voice',voices[0].id) # Selected Brian Voice

# say method on the engine that passing input text to be spoken
engine.say('''Hello this is voice sample''')

# run and wait method, it processes the voice commands.
engine.runAndWait()
