# File Name: settingHandler.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] 

#* Libraries *#

import os
import json
import sys
import time

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

AprilTag_HoloMat = "AT-HM-Para.json"
BlueTooth = "./btSettings/btSettings.json"
DeadZone = "deadZoneSettings.json"
General = "generalSettings.json"
handLayers = "handLayer.json"
Connections = "./connectionSettings/connectionSettings.json"

#& Functions &#

#~ define and build functions here

#= Classes =#

class ConnectionSettings():
  class Github():
    class Reading():
      def Reader(Endpoint=None):
        """This reads the endpoint addressed in the Required object to run this function.

        Args:
            Endpoint (string, required): The location that you wish to read. Defaults to None.
        """
        with open(Connections, "r") as f:
          data = json.load(f)
        output = data["Github"][Endpoint]
        return output
        
        
        
    class RepositoryManger():
      def AddRepository(ROwner=None, Repository=None):
        with open(Connections, "r") as f:
          data = json.load(f)
          CurrentRepositories = data["Github"]["Repository(s)"]
          CurrentList = CurrentRepositories
          NewRepository ={'Owner': ROwner, 'Repo': Repository}
          if NewRepository in CurrentList:
            print("This Repository is already Being Monitored!")
            return
          CurrentList.append(NewRepository)
        path = "Github.Repository(s)"
        with open(Connections, 'r') as f:
            data = json.load(f)

        # Split the path into individual keys
        keys = path.split('.')

        # Update the value at the specified path
        current_object = data
        for key in keys[:-1]:
            if key not in current_object:
                current_object[key] = {}
            current_object = current_object[key]
        current_object[keys[-1]] = CurrentList

        with open(Connections, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"The Repository {ROwner}/{Repository} Is now Actively Being Monitored.")
      def RemoveRepository(ROwner=None, Repository=None):
        with open(Connections, "r") as f:
          data = json.load(f)
          CurrentRepositories = data["Github"]["Repository(s)"]
          CurrentList = CurrentRepositories
          NewRepository ={'Owner': ROwner, 'Repo': Repository}
          if NewRepository not in CurrentList:
            print("This Repository is not already Being Monitored!")
            return
          CurrentList.remove(NewRepository)
        path = "Github.Repository(s)"
        with open(Connections, 'r') as f:
            data = json.load(f)

        # Split the path into individual keys
        keys = path.split('.')

        # Update the value at the specified path
        current_object = data
        for key in keys[:-1]:
            if key not in current_object:
                current_object[key] = {}
            current_object = current_object[key]
        current_object[keys[-1]] = CurrentList

        with open(Connections, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"The Repository {ROwner}/{Repository} was Deleted.")
    
    class Updater():
      #$ Updater Class TO-DO List $#
      #[*] add all the remove functions for the updater class
      #[] 
      def UpdateForks(Repository=None, Remove=False):
        """This updates the Forks List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["Forks"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.Forks"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["Forks"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.Forks"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
      
      def UpdateStarred(Repository=None, Remove=False):
        """This updates the Starred List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["Starred"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.Starred"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["Starred"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.Starred"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Stars.")
      
      def UpdateRepositoryCollaborators(Repository=None, Remove=False):
        """This updates the RepositoryCollaborators List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryCollaborators"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryCollaborators"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryCollaborators"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryCollaborators"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Repository Collaborators.")
      
      def UpdateCommits(Repository=None, Remove=False):
        """This updates the Commits List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["Commits"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.Commits"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["Commits"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.Commits"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Commits.")
      
      def UpdateRepositoryContributors(Repository=None, Remove=False):
        """This updates the RepositoryContributors List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryContributors"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryContributors"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For Forks.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryContributors"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryContributors"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Contributors.")
      
      def UpdateRepositoryDeployments(Repository=None, Remove=False):
        """This updates the RepositoryDeployments List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryDeployments"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryDeployments"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Deployments.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryDeployments"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryDeployments"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Deployments.")
      
      
      def UpdateRepositoryTags(Repository=None, Remove=False):
        """This updates the RepositoryTags List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryTags"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryTags"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Tags.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryTags"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryTags"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Tags.")
      
      
      def UpdateRepositoryIssues(Repository=None, Remove=False):
        """This updates the RepositoryIssues List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryIssues"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryIssues"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Issues.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryIssues"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryIssues"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Issues.")
      
      
      def UpdateRepositoryReleases(Repository=None, Remove=False):
        """This updates the Repository Releases in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryReleases"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryReleases"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Releases.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryReleases"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryReleases"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Releases.")
      
      def UpdateRepositoryCommitActivity(Repository=None, Remove=False):
        """This updates the RepositoryCommitActivity List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryCommitActivity"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryCommitActivity"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Commit Activity.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryCommitActivity"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryCommitActivity"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Commit Activity.")
      
        with open(Connections, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Commit Activity.")
      
      def UpdateRepositoryTopics(Repository=None, Remove=False):
        """This updates the RepositoryTopics List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryTopics"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryTopics"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Topics.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryTopics"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryTopics"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Topics.")

      def UpdateRepositoryWatchers(Repository=None, Remove=False):
        """This updates the RepositoryWatchers List in the Connections Settings for the Connection Github.

        Args:
            Repository (str, required): The name of the Repository that is being added to the List. Defaults to None.
            Remove (bool, optional): Always Defaults to False. Defaults to False.
        """
        #+ Adding to the List +#
        if Remove is False:
            with open(Connections, "r") as f:
              data = json.load(f)
              CurrentRepositories = data["Github"]["RepositoryWatchers"]
              CurrentList = CurrentRepositories
              NewRepository ={'Repo': Repository, 'Active': True}
              if NewRepository in CurrentList:
                print("This Repository is already Being Monitored!")
                return
              CurrentList.append(NewRepository)
            path = "Github.RepositoryWatchers"
            with open(Connections, 'r') as f:
                data = json.load(f)

            # Split the path into individual keys
            keys = path.split('.')

            # Update the value at the specified path
            current_object = data
            for key in keys[:-1]:
                if key not in current_object:
                    current_object[key] = {}
                current_object = current_object[key]
            current_object[keys[-1]] = CurrentList

            with open(Connections, 'w') as f:
                json.dump(data, f, indent=4)
                print(f"The Repository {Repository} Is now Actively Being Monitored For any New Repository Watchers.")
        #- Removing from the List -#
        if Remove is True:
          with open(Connections, "r") as f:
            data = json.load(f)
            CurrentRepositories = data["Github"]["RepositoryWatchers"]
            CurrentList = CurrentRepositories
            NewRepository = [{'Repo': Repository, 'Active': True}, {'Repo': Repository, 'Active': False}]
            if NewRepository[0] in CurrentList:
              CurrentList.remove(NewRepository[0])
              pass
            elif NewRepository[1] in CurrentList:
              CurrentList.remove(NewRepository[1])
              pass
          path = "Github.RepositoryWatchers"
          with open(Connections, 'r') as f:
              data = json.load(f)

          # Split the path into individual keys
          keys = path.split('.')

          # Update the value at the specified path
          current_object = data
          for key in keys[:-1]:
              if key not in current_object:
                  current_object[key] = {}
              current_object = current_object[key]
          current_object[keys[-1]] = CurrentList

          with open(Connections, 'w') as f:
              json.dump(data, f, indent=4)
              print(f"The Repository {Repository} Is now Actively Being Monitored For Any New Repository Watchers.")
      
class DatabaseSettings():
  def checkMySQL(path):
    with open(path, "r") as f:
        data = json.load(f)
        output = data["Database Settings"]["MySQL"]
        return output
  def checkMongoDB(path):
    with open(path, "r") as f:
        data = json.load(f)
        output = data["Database Settings"]["MongoDB"]
        return output
#! Main Program !#

# ConnectionSettings.Github.RepositoryManger.AddRepository("Silewis37", "Test")
# ConnectionSettings.Github.Updater.UpdateForks("Test")
# ConnectionSettings.Github.Updater.UpdateStarred("Test")
# time.sleep(3)
# ConnectionSettings.Github.RepositoryManger.RemoveRepository("Silewis37", "Test")
# ConnectionSettings.Github.Updater.UpdateForks("Test", Remove=True)
# ConnectionSettings.Github.Updater.UpdateStarred("Test", Remove=True)

#print(DatabaseSettings.checkMongoDB("src/_settings/connectionSettings"))




#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#