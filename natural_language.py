"""
MARKOV CHAIN
Natural languages specifications
"""
from dataclasses import dataclass

@dataclass(frozen=False, order=False)
class Alphabet:
	lowers: list[str]
	uppers: list[str]
	vowels: list[str]
	consonants: list[str]
	spaces: list[str]

	def __init__(self, lowers: list[str], vowels: list[str], spaces: list[str] = [" "]) -> None:
		self.lowers = [letter.lower() for letter in lowers]
		self.uppers = [letter.upper() for letter in self.lowers] 
		self.vowels = [letter.lower() for letter in vowels] 
		self.consonants = [letter.lower() for letter in lowers if letter not in self.vowels]
		self.spaces = spaces

