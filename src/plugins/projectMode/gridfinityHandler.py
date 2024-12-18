# File Name: gridfinityHandler.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item

#* Libraries *#

import sys
import os
import json

#* Custom Libraries *#

sys.path.append(os.path.abspath("../../"))

#~ import custom made libraries here

#^ Variables ^#

json_file_path = os.path.join(os.path.dirname(__file__), '../../data/projectMode/gridfinity/gridfinity.json')

#& Functions &#

def read_nested_data():
    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Access the nested value (e.g., data['nested']['key'])
        nested_value = data['Base']['Dove Frame - GlitchPrinter']['Items Within']
        
        print('Nested Value:', nested_value)
        return nested_value
    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
    except KeyError as e:
        print(f"Error: Missing key in JSON data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON: {e}")

#= Classes =#

#~ define and build classes here

#! Main Program !#

read_nested_data()

#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
