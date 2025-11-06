import chess
from chessy import board as board_module  # ton module chessy/board.py

def main():
    print("♟️ Bienvenue dans Chessy — Jeu d’échecs vocal avec IA ♟️")

    # --- Création ou chargement de la partie ---
    choice = ""
    while choice not in ["1", "2"]:
        print("\n1️⃣ Nouvelle partie")
        print("2️⃣ Charger une partie")
        choice = input("Choisissez une option (1 ou 2) : ").strip()

    if choice == "1":
        game = chess.Board()
        print("\nNouvelle partie créée !")
    else:
        fen = input("Entrez le FEN à charger : ").strip()
        try:
            game = chess.Board(fen)
            print("\nPartie chargée !")
        except Exception:
            print("FEN invalide, création d'une nouvelle partie.")
            game = chess.Board()

    # --- Boucle principale ---
    while not game.is_game_over():
        print("\nÉtat actuel de la partie :")
        print(game)
        print("\nC’est à vous de jouer !")

        move = input("Entrez votre coup (ex: e2e4) : ").strip()
        new_game = board_module.play_move(game, move)

        # ✅ Vérification du retour de play_move
        if isinstance(new_game, str):
            print(new_game)
            continue  # On redemande un coup valide

        if new_game is None:
            print("Erreur interne : le coup n’a pas été appliqué.")
            continue

        # Si tout va bien, on met à jour le plateau
        game = new_game

    # --- Fin de partie ---
    print("\n🎉 Partie terminée ! 🎉")
    print(game)
    print("Résultat :", game.result())

    outcome = game.outcome()
    if outcome:
        if outcome.termination == chess.Termination.CHECKMATE:
            gagnant = "Blancs" if outcome.winner else "Noirs"
            print(f"Échec et mat ! {gagnant} gagnent.")
        elif outcome.termination == chess.Termination.STALEMATE:
            print("Partie nulle par pat.")
        else:
            print(f"Partie terminée : {outcome.termination.name}")

if __name__ == "__main__":
    main()
