"""
MARKOV CHAIN
Maths additions, local.
"""

import random



class Random:
    @staticmethod
    def choice_pondered(choices: dict[str, int]) -> str:
        """
        Choose a random string from a dict[string, weight]
        """
        flatten_choices: list[str] = []
        for choice, weight in choices.items():
            for _ in range(round(weight)):
                flatten_choices.append(choice)

        random_index: int = random.randint(0, len(flatten_choices) - 1)

        return flatten_choices[random_index]

    @staticmethod
    def choice_flat(choices: list[str]) -> str:
        """
        Choose a random character from a given list, where each event as the same outcome probability. 
        """
        return choices[random.randint(0, len(choices) - 1)]

if __name__ == "__main__":
    print(f"{Random.choice_pondered({"a": 2, "b": 5, "c": 1, "d": 0})}")
    print(f"{Random.choice_flat(["a", "b", "c", "d"])}")