# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module permettant de créer les menus pour permettre au joueur de choisir ses paramètres de jeu'''

#---Imports
from src.upemtk import *
from src.fichiers import *


def fenetre():
    cree_fenetre(400,600)
    return True

def accueil():
    efface_tout()
    #Nom du jeu
    texte(145,100,police='Arial',chaine='Jeu Azul')

    #Jouer
    rectangle(100,200,300,250)
    texte(155,205,"Jouer",police="Arial")

    #Options
    rectangle(100,270,300,320)
    texte(150,275,"Options",police="Arial")

    #Quitter
    rectangle(100,340,300,390)
    texte(155,345,"Quitter",police="Arial")

    rectangle(10,550,15,555)
    if existe('./files/save.txt'):
        rectangle(100,410,300,460)
        texte(110,415,"Reprendre partie",police='Arial',taille=17)

def clic_accueil():
    while True:
        x,y,_ = attente_clic()
        if 100<=x<=250 and 200<=y<=250:
            return 1
        if 100<=x<=250 and 270<=y<=320:
            return 2
        if existe('./files/save.txt') and 100<=x<=250 and 410<=y<=460:
            return 4
        if 100<=x<=250 and 340<=y<=390:
            return False
        if 10<=x<=15 and 500<=y<=555:
            print("ii")
            return 99




def clic_ia(nombre_joueurs):
    while True:
        x,y,_ = attente_clic()
        if 100<=x<=250 and 200<=y<=250:
            return [None]
        if 100<=x<=250 and 270<=y<=320:
            return list(range(2,nombre_joueurs+1))
        if 100<=x<=250 and 340<=y<=390:
            return False
        '''
        if 100<=x<=250 and 410<=y<=460:
            return False
        '''

def jouer_ia():
    efface_tout()
    texte(120,100,police='Arial',chaine='Jouer contre ?')

    #Jouer
    rectangle(100,200,300,250)
    texte(130,205,"Un humain",police="Arial")

    #Options
    rectangle(100,270,300,320)
    texte(120,275,"L'ordinateur",police="Arial")

    #Quitter
    rectangle(100,340,300,390)
    texte(145,345,"Accueil",police="Arial")



def clic_jouer():
    while True:
        x,y,_ = attente_clic()
        if 100<=x<=250 and 200<=y<=250:
            return 2
        if 100<=x<=250 and 270<=y<=320:
            return 3
        if 100<=x<=250 and 340<=y<=390:
            return 4
        if 100<=x<=250 and 410<=y<=460:
            return False

def jouer():
    efface_tout()
    texte(80,100,police='Arial',chaine='Choisir mode de jeu')

    #Jouer
    rectangle(100,200,300,250)
    texte(145,205,"2 joueurs",police="Arial")

    #Options
    rectangle(100,270,300,320)
    texte(145,275,"3 joueurs",police="Arial")

    #Quitter
    rectangle(100,340,300,390)
    texte(145,345,"4 joueurs",police="Arial")

    rectangle(100,410,300,460)
    texte(150,415,"Retour",police="Arial")

def options(settings_config):
    efface_tout()
    texte(140,100,police='Arial',chaine='Options')

    #Jouer
    rectangle(100,200,300,250)
    texte(105,205,"Low Graphiques: "+str(settings_config[2]),taille="10")

    '''
    #Options
    rectangle(100,270,300,320)
    texte(145,275,"3 joueurs",police="Arial")

    #Quitter
    rectangle(100,340,300,390)
    texte(145,345,"4 joueurs",police="Arial")
    '''

    rectangle(100,410,300,460)
    texte(150,415,"Retour",police="Arial")


def clic_options(settings_config):
    while True:
        x,y,_ = attente_clic()
        if 100<=x<=250 and 200<=y<=250:
            settings_config[2] = not settings_config[2]
            options(settings_config)
        '''
        if 100<=x<=250 and 270<=y<=320:
            return 3
        if 100<=x<=250 and 340<=y<=390:
            return 4
        '''
        if 100<=x<=250 and 410<=y<=460:
            return False


def menu_jeu(chemin):
    fenetre()
    config = [2,[2],False,False]
    if existe(chemin):
        config = copy_file(chemin)
        config[-1] = False
    print(config)
    
    while True:
        accueil()
        choix = clic_accueil()
        if not choix:
            ecrire_config(config,chemin)
            print("Quitter")
            return False
        if choix == 1:
            jouer()
            nombre_joueurs = clic_jouer()
            if not nombre_joueurs:
                print("Retour")
                continue
            config[0] = nombre_joueurs
            jouer_ia()
            choix = clic_ia(nombre_joueurs)
            if not choix:
                print("Accueil")
                continue
            config[1] = choix
            ecrire_config(config,chemin)
            ferme_fenetre()
            return True
        if choix == 4:
            config[3] = True
            ecrire_config(config,chemin)
            ferme_fenetre()
            return True
        if choix == 2:
            options(config)
            choix = clic_options(config)
        if choix == 99:
            ecrire_config([4,[1,2,3,4],False,False],chemin)
            ferme_fenetre()
            return True






if __name__ == '__main__':
    menu_jeu()
