import sys
import git 
import os
import shutil

workingdirectory  = os.path.dirname(__file__)
deploydirectory = os.path.join(workingdirectory, "../sythenz.github.io/")

rootSite = os.path.join(workingdirectory, "/_site/")

# g = git.cmd.Git(filename)
# status = g.status()
# g.pull()

# print(status)

deploymentGit = git.cmd.Git(deploydirectory)
deploymentStatus = deploymentGit.status()

def GetLatestDeployment():
    print("Pulling latest for " + deploydirectory)
    deploymentGit.pull()

def CallJekyll():
    os.system("jekyll build")

def MoveSiteDirectory():
    sitepath = os.path.join(workingdirectory, "_site")
    dest = shutil.copytree(sitepath, deploydirectory, dirs_exist_ok=True)
    deployfile = os.path.join(deploydirectory, "deploy.py")
    os.remove(deployfile)

def PushToGit():
    deploymentGit.add(all=True)
    deploymentGit.commit('-m', sys.argv[1], author="alessafur@protonmail.com")
    deploymentGit.push()

def main():     
    if len(sys.argv) < 2:
        print("No command specified")
        exit()

    print(sys.argv)

    GetLatestDeployment()
    CallJekyll()
    MoveSiteDirectory()
    PushToGit()

if __name__ == "__main__":
    main()