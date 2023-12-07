
def simuler_infection(population, infectes_initiaux, jours, rencontres_par_jour):
    
    pt = 0.01
    pg = 0.05
    infectes_jour = [0] * (jours + 1)
    infectes_jour[0] = infectes_initiaux
    rencontres_par_jour_liste = [rencontres_par_jour] * (jours + 1)

    
    for jour in range(1, jours + 1):
        if 30 <= jour <= 75:
            rencontres_par_jour_liste[jour] = 3

        nouveaux_infectes = infectes_jour[jour - 1] * (1 - pg)
        infectes_jour[jour] = nouveaux_infectes + (population - nouveaux_infectes) * rencontres_par_jour * nouveaux_infectes / population * pt

    return infectes_jour


def main():
    
    population = 11500000
    infectes_initiaux = 100
    jours = 365
    rencontres_par_jour = 10

    
    donnees_infection = simuler_infection(population, infectes_initiaux, jours, rencontres_par_jour)

    
    while True:
        jour_input = input("Entrez le numéro d'un jour (1-365) ou '0' pour passer à la suite : ")

        if jour_input == '0':
            break

        try:
            jour = int(jour_input)
            if 1 <= jour <= 365:
                print(f"Nombre de personnes infectées le jour {jour}: {int(donnees_infection[jour])}")
            else:
                print("Le jour doit être compris entre 1 et 365.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    
    moyenne_infectes_par_jour = sum(donnees_infection) / jours
    moyenne_nouvelles_infections_par_jour = sum(donnees_infection[i] - donnees_infection[i - 1] for i in range(1, jours)) / (jours - 1)

    
    print(f"\nNombre moyen de personnes infectées par jour sur l'année : {moyenne_infectes_par_jour:.2f}")
    print(f"Nombre moyen de nouvelles infections par jour sur l'année : {moyenne_nouvelles_infections_par_jour:.2f}")

    
    jour_max_infectes = donnees_infection.index(max(donnees_infection))
    print(f"Le jour du premier pic du nombre de personnes infectées est le jour {jour_max_infectes}.")

    
    if donnees_infection[-1] == max(donnees_infection):
        print("La population sera complètement infectée.")
    elif donnees_infection[-1] == 0:
        print("La population guérira complètement.")
    else:
        print("La population sera partiellement infectée.")


if __name__ == "__main__":
    main()
