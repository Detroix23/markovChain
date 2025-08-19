"""
MARKOV CHAIN
Search vowels
"""

import tree
import natural_language as lang
# from typing_extensions import Self


class SearchVowels(tree.Branch):
	"""
	Contain all search static methods, for the sake of organization.
	"""

	def __init__(self, depth: int, alphabet: lang.Alphabet) -> None:
		self.outcomes: list[str] = ["vowel", "consonant", "space", "special"]
		self.alphabet: lang.Alphabet = alphabet
		self.root_name: str = "total"
		self.root_position: int = 0
		super().__init__(self.outcomes, depth, self.root_name, self.root_position)

	def analyse(self, text: str) -> tree.Branch:
		"""
		Function: Establish the probability chain from moving between consonants and vowels. Additive to previous results
		:param text: string to analyze.
		:param alphabet: entire alphabet structure that contain all letters, and all vowels.
		:returns: Dictionary containing the total number of character and the number of travels between each combinations.

		"""
		# Main loop
		reader_index: int = 0
		while reader_index < len(text) - 1:
			# Get the characters
			char_0: str = text[reader_index]
			char_1: str = text[reader_index + 1]
			# If both spaces, skip
			if char_0.lower() not in self.alphabet.lowers and char_1.lower() not in self.alphabet.lowers:
				pass
			else:
				# Saving the combination
				self.update_tree([char_0, char_1])

			reader_index += 1

		return self
	
	def update_tree(self, list_cases: list[str], branch_in: tree.Branch|None = None):
		# Default
		branch: tree.Branch
		if branch_in is None:
			branch = self
		else:
			branch = branch_in

		# Handle each case, for the vowel based search
		event_name: str
		case_value: str = list_cases[0].lower()
		if case_value in self.alphabet.vowels:
			event_name = self.outcomes[0]
		elif case_value in self.alphabet.consonants:
			event_name = self.outcomes[1]
		elif case_value in self.alphabet.spaces:
			event_name = self.outcomes[2]
		else:
			event_name = self.outcomes[3]
		# Get next branch
		branch = branch.get_branch(event_name)
		branch.value += 1
		list_cases.pop(0)
		# Recursion
		if len(list_cases) > 0:
			self.update_tree(list_cases, branch)


if __name__ == "__main__":
	print("MARKOV CHAIN.")
	print("Vowels testing")

