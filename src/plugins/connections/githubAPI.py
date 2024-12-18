# File Name: gitHub.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item

#* Libraries *#

import os
import json
import sys
from github import Github
import requests
import urllib.request
from dotenv import load_dotenv


#* Custom Libraries *#

import _settings.settingHandler as settingsHandler

#^ Variables ^#

load_dotenv()

GithubAPI_TOKEN = os.getenv('GITHUB_API_TOKEN')
g = Github(GithubAPI_TOKEN)

#& Functions &#

def RepoForks(Owner, Repo):
  url = f"https://api.github.com/repos/{Owner}/{Repo}/forks"
  h = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GithubAPI_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
  }
  response = requests.get(url, headers=h)
  print(response.json())
  with open("github-output.json", "w+") as f:
      data4 = json.dumps(response.json(), indent=4)
      f.write(data4)
      f.close()

#= Classes =#

#~ define and build classes here

#! Main Program !#

RepoForks("Silewis37", "JARVIS")
# g.get_user().login
# info = g.get_repo("Silewis37/JARVIS")
# print(info.name)
# print(info.stargazers_count)



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#