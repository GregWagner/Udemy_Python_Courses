from abc import ABC, abstractmethod
from random import randint
from numpy import argmax


class Player(ABC):
    @abstractmethod
    def next_action(self, state):
        ...


class IndecisivePlayer(Player):
    """Randomly select a move"""

    def next_action(self, state):
        # get the valid moves
        moves = self.next_actions(state)
        return moves[randint(0, len(moves) - 1)]

    @abstractmethod
    def next_actions(self, state):
        ...


class MiniMaxPlayer(IndecisivePlayer):
    """AI Player"""

    def __init__(self, lookahead):
        assert lookahead > 0
        self.lookahead = lookahead

    def next_actions(self, state):
        moves, _ = self.get_herstiic_value(state, self.lookahead)
        return moves

    def get_herstiic_value(self, state, lookahead):
        if lookahead == 0 or state.gameover():
            # there was a tie or one player won (no moves)
            return [], 1.0 * state.winner() * (lookahead + 1)
        behaviour = max if state.player() == 1 else min
        return self.minimax(state, behaviour, lookahead)

    def minimax(self, state, behaviour, lookahead):
        """minimax algorithm"""
        moves, reward = [], -10000 * state.player()
        for cell in state.actions():
            _, v = self.get_herstiic_value(state.move(cell), lookahead - 1)
            if reward == v:
                moves.append(cell)
            elif behaviour(reward, v) == v:
                moves, reward = [cell], v
        return moves, reward


class NNPlayer(Player):
    def __init__(self, model):
        self.model = model

    def next_action(self, state):
        actions = state.actions()
        current_player = state.player()
        states = [state.move(action).cells for action in actions]
        probs = self.model.predict(states)
        player_probs = [p[current_player] for p in probs]
        return actions[argmax(player_probs)]
