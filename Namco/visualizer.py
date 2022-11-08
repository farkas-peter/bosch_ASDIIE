import os

import numpy as np


class Visualizer:
    def clear_console(self):
        """
        Clearing the console
        :return:
        """
        # Note: Cannot clear the console in PyCharm, only in terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_map(self, observation: np.ndarray):
        """
        Visualizing the current state of the game to the player
        :param observation: Array containing the map (np.ndarray)
        :return:
        """
        for line in observation:
            print(*line, sep='  ')

    def show_score(self, curr_score: int):
        """
        Informing the user about the current score
        :param curr_score: Current score of the player (int)
        :return: -
        """
        print("\nCurrent score: ", curr_score)

    def game_over(self, done: bool):
        """
        Informing the user that the game is over
        :param done: Game over flag
        :return: -
        """
        if done:
            print("\nGAME OVER")

    def render(self, observation: np.ndarray, curr_score: int, done: bool):
        """
        Renders the required information.
        :param observation: Array containing the map (np.ndarray)
        :param curr_score: Current score of the player (int)
        :param done: Game over flag (bool)
        :return:
        """
        self.clear_console()
        self.show_map(observation)
        self.show_score(curr_score)
        self.game_over(done)