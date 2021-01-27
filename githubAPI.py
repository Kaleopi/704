#!/usr/bin/python3
import os

email="thomas.gigout@etudiant.univ-reims.fr"
pseudo="Kaleopi"

def config(email=email,name=pseudo):
    cmd = 'git config --global user.email "'+email+'" '
    os.system(cmd)
    cmd = 'git config --global user.name "'+name+'" '
    os.system(cmd)

def clone(url):
    cmd="git clone "+url
    print("[GIT CLONE] "+str(cmd))
    os.system(cmd) 

def init(project_path):
    cmd = "mkdir "+project_path+" && git init " + project_path
    print("[GIT INIT] " + str(cmd))
    os.system(cmd)

def add(filespath, project_path):
    cmd="cd "+project_path+" && git add "
    for f in filespath:
        cmd += f+" "
        
        # print("Copying "+f+" into "+project_path)
        print(cmd)
        os.system("cp "+f+" "+project_path)

    print("[GIT ADD] "+str(cmd))
    os.system(cmd) 

def commit_push(modif, project_path):
    cmd="cd "+project_path+" && git commit -m '"+modif+"' && git push --set-upstream origin master"
    print("[GIT COMMIT PUSH] "+str(cmd))
    os.system(cmd) 

def del_project(project_path):
    cmd="rm -fr "+project_path+"/.git"1
    print("[GIT DEL] "+str(cmd))
    os.system(cmd) 
