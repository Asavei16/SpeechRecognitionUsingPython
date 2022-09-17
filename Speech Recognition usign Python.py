#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr
import pyaudio


# In[2]:


# Initialize the recognizer
r = sr.Recognizer()


# In[3]:


############### SPEECH RECOGNITION FROM MICROPHONE LIVE ####################


# In[12]:


# Utilizam microfonul ca sursa de intrare
with sr.Microphone() as mic:
            #asteptati o secunda pentru a ajusta 
            #pragul de energie in functie de 
            #nivelul de zgomot din jur
        print("Liniste, calibrare zgomot fundal...")
        r.adjust_for_ambient_noise(mic, duration=2)
        print("Calibrat, poti vorbi...")
        
        #Asculta intrarea utilizatorului
        audio2 = r.listen(mic)
        
        #Folosind google pentru a recunoaste sunetul in limba romana
        MyText = r.recognize_google(audio2, language='ro-RO')
        
        try:
            print("Tu ai spus : " + MyText)
        except Exception as e:
            print("A aparut o eroare -> " + str(e))
            
#         SpeakText(MyText)


# In[13]:


#Optional
#Salvam inregistrarea sub un fisier wav
with open("romana.wav", "wb") as f:
            f.write(audio2.get_wav_data())
            print("Inregistrarea a fost salvata cu succes!")


# In[6]:


############### SPEECH RECOGNITION FROM AUDIO FILE ORIGINAL ####################


# In[17]:


sample_audio = sr.AudioFile('59_Split_.wav')
# sample_audio = sr.AudioFile('romana.wav')
# sample_audio = sr.AudioFile('60_Split_.wav')
# sample_audio = sr.AudioFile('61_Split_.wav')
# sample_audio = sr.AudioFile('62_Split_.wav')
# sample_audio = sr.AudioFile('63_Split_.wav')
with sample_audio as source:
       audio=r.record(source)


# In[15]:


r.recognize_google(audio)


# In[18]:


r.recognize_google(audio,language='ro-RO') #pentru romana


# In[ ]:




