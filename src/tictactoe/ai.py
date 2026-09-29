import time
import tracemalloc
import math

def minimax(game, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    # Lõpetab rekursiooni terminalseisus (võit/viik)
    if game.winner or game.is_draw:
        # Hangib baashinnangu (+1, -1, 0)
        score = game.evaluate_board()
        if score == 1:
            # Optimeerib lahendusteed premeerides kiiremaid võite
            return 10 - depth
        elif score == -1:
            # Karistab kiiremaid kaotusi, eelistades mängu pikendamist
            return -10 + depth
        return 0

    # Harrastab max-mängija ('O') loogikat (otsib suurimat skoori)
    if is_maximizing:
        best_score = -math.inf
        for r, c in game.get_available_moves():
            # Loob mänguseisust koopia, et vältida globaalse laua rikkumist simuleerimisel
            sim_game = game.clone()
            # Teeb potentsiaalse käigu koopias
            sim_game.make_move(r, c)
            # Kutsutakse rekursiivselt välja vastase käigu simuleerimiseks
            score = minimax(sim_game, depth + 1, False, alpha, beta)
            # Uuendab seni leitud parimat valikut
            best_score = max(score, best_score)
            # Uuendab Alpha-Beta kärpimise piire
            alpha = max(alpha, score)
            # (Kärpimine) Lõpetab haru läbimise, sest see on tõestatult halvem
            if beta <= alpha:
                break
        return best_score
    else:
        # Min-mängija ('X') loogika
        best_score = math.inf
        for r, c in game.get_available_moves():
            sim_game = game.clone()
            sim_game.make_move(r, c)
            score = minimax(sim_game, depth + 1, True, alpha, beta)
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def get_best_move(game):
    tracemalloc.start()
    start_time = time.perf_counter()

    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf

    for r, c in game.get_available_moves():
        sim_game = game.clone()
        sim_game.make_move(r, c)
        # AI is 'O' (maximizing player), human is 'X' (minimizing)
        # Since AI just moved, next turn is minimizing (False)
        score = minimax(sim_game, 0, False, alpha, beta)
        if score > best_score:
            best_score = score
            best_move = (r, c)
        alpha = max(alpha, best_score)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak / 1024

    print(f"--- AI Move Profile ---")
    print(f"Execution Time : {execution_time_ms:.2f} ms")
    print(f"Peak Memory    : {peak_memory_kb:.2f} KB")
    print(f"-----------------------")

    return best_move
