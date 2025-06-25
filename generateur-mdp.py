import random

def generer_mot_de_passe_chiffres(longueur, avec_lettreMAJ, avec_chiffre, avec_caractere):
    chiffre = "0123456789"
    caractere = "!:;,?./§"
    lettreMAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettreMIN = "abcdefghijklmnopqrstuvwxyz"
    
    final = lettreMIN
    if avec_lettreMAJ:
        final += lettreMAJ
    if avec_chiffre:
        final += chiffre
    if avec_caractere:
        final += caractere

    mdp = ''
    for _ in range(longueur):
        mdp += random.choice(final)
    return mdp

def evaluer_robustesse(mdp, avec_maj, avec_chiffre, avec_cara):
    longueur = len(mdp)
    
    # Détection du niveau de complexité
    if not avec_maj and not avec_chiffre and not avec_cara:
        niveau = "minuscules seulement"
        mini = 20
    elif avec_maj and avec_chiffre and avec_cara:
        niveau = "minuscules + majuscules + chiffres + caractères spéciaux"
        mini = 12
    else:
        niveau = "complexité intermédiaire"
        mini = 16

    print("Complexité détectée : " + niveau)
    print("Longueur minimale recommandée : " + str(mini))
    print("Longueur réelle du mot de passe : " + str(longueur))

    # Calcul du score
    score = 0
    if avec_maj:
        score += 2
    if avec_chiffre:
        score += 2
    if avec_cara:
        score += 2

    if longueur >= 20:
        score += 4
    elif longueur >= 16:
        score += 3
    elif longueur >= 12:
        score += 2
    elif longueur >= 8:
        score += 1

    if score <= 6:
        print("\n⚠️ Faible — Mot de passe trop court ou pas assez varié")
    elif score <= 9:
        print("\n🟡 Moyen — Acceptable mais améliorable")
    else:
        print("\n🟢 Fort — Bon niveau de sécurité")

# --- Programme principal ---

longueur = int(input("longueur du mot de passe : "))
maj = input("inclure des majuscules (o/n) ? ").lower() == 'o'
chi = input("inclure des chiffres (o/n) ? ").lower() == 'o'
cara = input("inclure des caractères spéciaux (o/n) ? ").lower() == 'o'

mdp = generer_mot_de_passe_chiffres(longueur, maj, chi, cara)
print("\nMot de passe : " + mdp + "\n")
evaluer_robustesse(mdp, maj, chi, cara)

input("")  # pause terminal
