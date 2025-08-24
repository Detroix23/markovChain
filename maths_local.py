"""
MARKOV CHAIN
Maths additions, local.
"""

import random



class Random:
    @staticmethod
    def choice_pondered(choices: dict[str, float]) -> str:
        """
        Choose a random string from a dict[string, weight]
        """
        ponder_total: float = sum(choices.values())
        r: float = random.uniform(0, ponder_total)
        ponder_actual: float = 0
        for choice, ponder in choices.items():
            if ponder_actual <= r < ponder_actual + ponder:
                return choice
            ponder_actual += ponder
        raise Exception(f"(X) maths_local.choice_pondered - R number didn't choose anything (r={r}, ponder_total={ponder_total}).")


    @staticmethod
    def choice_flat(choices: list[str]) -> str:
        """
        Choose a random character from a given list, where each event as the same outcome probability. 
        """
        return choices[random.randint(0, len(choices) - 1)]

if __name__ == "__main__":
    print(f"{Random.choice_pondered({"a": 2, "b": 5, "c": 1, "d": 0})}")
    print(f"{Random.choice_flat(["a", "b", "c", "d"])}")