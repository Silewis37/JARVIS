# File Name: mainJarvis.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Initial Connection to the Ollama JARVIS model.
#[] Make it so that the output Information from the Model can be easily read and spoken in the VOICE BOX Function File.

#* Libraries *#

import ollama
import time
import sys
import os

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

#~ create and store variables here

#& Functions &#

def send_message(message):
  #- SO to use this properly and get a good output, you must do print(output[i], end='', flush=True) to get it to print properly, if you dont it will print on separate lines every time.
  output = []
  stream = ollama.chat(
      model='JARVIS-SL',
      messages=[{'role': 'user', 'content': f'{message}'}],
      stream=True
  )
  fi = open("./outputText.txt", "w")
  fi.write("")
  fi.close()
  f = open("./outputText.txt", "a+")
  for chunk in stream:
    messageO = chunk['message']['content']
    f.write(messageO)
  f.close()
  return output

#= Classes =#

#~ define and build classes here

#! Main Program !#

#~ the main program goes here




#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#