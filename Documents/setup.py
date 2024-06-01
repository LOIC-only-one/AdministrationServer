import os
import subprocess
import tempfile
import shutil

def cloner_projet(repo, chemin):
    """
    Cloner le projet git dans le chemin spécifié
    """
    subprocess.run(['git', 'clone', repo, chemin], check=True)

def copier_dossiers(dossiers, src, dst):
    """
    Copier les dossiers spécifiés de src vers dst
    """
    for dossier in dossiers:
        src_dossier = os.path.join(src, dossier)
        dst_dossier = os.path.join(dst, dossier)
        if os.path.exists(dst_dossier):
            shutil.rmtree(dst_dossier)  # Supprimer le dossier existant
        shutil.copytree(src_dossier, dst_dossier)  # Copier le nouveau dossier

def attribuer_droits(chemin):
    """
    Attribuer les droits 777 au chemin spécifié
    """
    os.system(f'chmod 777 -R {chemin}')

def main():
    """
    Fonction principale
    """
    dossier_tmp = tempfile.mkdtemp()

    repo = "https://github.com/LOIC-only-one/AdministrationServer.git"
    cloner_projet(repo, dossier_tmp)

    os.chdir(os.path.join(dossier_tmp, 'AdministrationServer', 'admin_serv'))

    dossiers = ['logos', 'media', 'servops', 'static']
    copier_dossiers(dossiers, os.getcwd(), '/var/www/html/admin_serv')

    attribuer_droits('/var/www/html/admin_serv')

if __name__ == "__main__":
    main()