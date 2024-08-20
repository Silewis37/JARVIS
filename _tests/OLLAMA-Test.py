# File Name: OLLAMA-Test.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item


#* Libraries *#

import ollama

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

stream = ollama.chat(
    model='JARVIS',
    messages=[{'role': 'user', 'content': 'Hello, what is your name?'}],
    stream=True
)

#& Functions &#

#~ define and build functions here

#= Classes =#

#~ define and build classes here

#! Main Program !#

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)


#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @# 