"""
MARKOV CHAIN
Natural languages specifications
"""


class Alphabet:
	def __init__(self, lowers: list[str], vowels: list[str]) -> None:
		self.lowers: list[str] = lowers
		self.uppers: list[str] = [letter.upper() for letter in self.lowers] 
		self.vowels: list[str] = vowels
		self.consonnants: list[str] = [letter for letter in lowers if letter not in self.vowels]
	

