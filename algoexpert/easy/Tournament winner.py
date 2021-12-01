def update_points(team, point, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += point


def tournamentWinner(competitions, results):

    scores = {}
    winner = None

    for idx in range(len(results)):

        home, away = competitions[idx]
        winner_team = home if results[idx] == 1 else away

        update_points(winner_team, 3, scores)

        if winner is None:
            winner = winner_team

        if (scores[winner_team] != winner_team and
                scores[winner_team] > scores[winner]):
            winner = winner_team

    return winner

