"""
MARKOV CHAIN
Search vowels
"""
import tree
import natural_language as lang
import maths_local
# from typing_extensions import Self


class Vowels(tree.BranchBonzai):
	"""
	Contain all search static methods, for the sake of organization.
	"""

	def __init__(self, depth: int, alphabet: lang.Alphabet) -> None:
		self.outcomes: list[str] = ["vowel", "consonant", "space", "special"]
		self.alphabet: lang.Alphabet = alphabet
		self.root_name: str = "total"
		self.root_position: int = 0
		super().__init__(self.outcomes, depth, self.root_name, self.root_position)

	def case_map(self, case_value: str) -> str:
		event_name: str
		if case_value in self.alphabet.vowels:
			event_name = self.outcomes[0]
		elif case_value in self.alphabet.consonants:
			event_name = self.outcomes[1]
		elif case_value in self.alphabet.spaces:
			event_name = self.outcomes[2]
		else:
			event_name = self.outcomes[3]
		
		return event_name

	def analyse(self, text: str) -> tree.BranchBonzai:
		"""
		Function: Establish the probability chain from moving between consonants and vowels. Additive to previous results
		:param text: string to analyze.
		:param alphabet: entire alphabet structure that contain all letters, and all vowels.
		:returns: Dictionary containing the total number of character and the number of travels between each combinations.

		"""
		# Setting the `root` value, considering the text to be clean (no double space, no spaces at the end,...).
		self.value += len(text)
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
	
	def update_tree(self, list_cases: list[str], branch_in: tree.BranchBonzai|None = None):
		# Default
		branch: tree.BranchBonzai
		if branch_in is None:
			branch = self
		else:
			branch = branch_in

		# Handle each case, for the vowel based search
		case_value: str = list_cases[0].lower()
		event_name: str = self.case_map(case_value)

		# Get next branch
		branch = branch.get_branch(event_name)
		branch.value += 1
		list_cases.pop(0)
		# Recursion
		if len(list_cases) > 0:
			self.update_tree(list_cases, branch)

	def build_from_chain(self, length: int, include_spaces: bool) -> str:
		generated_text: str = " "
		generator_index: int = 0

		while generator_index < length:
			# Pathing the good branch
			branch: tree.BranchBonzai = self
			for depth in range(-branch.rank - 1, 0, 1):
				# Check if the position even exists
				if generator_index + depth < 0:
					break
				char: str = generated_text[generator_index + depth]
				event: str = self.case_map(char)
				branch = branch.get_branch(event)
			
			# Computing the character
			next_events: dict[str, int] = branch.next_to_dict()
			if not include_spaces:
				next_events.pop(self.outcomes[2], None)
			next_events.pop(self.outcomes[3], None)

			character_type: str = maths_local.Random.choice_pondered(next_events)
			character_new: str
			if character_type == self.outcomes[0]:
				character_new = maths_local.Random.choice_flat(self.alphabet.vowels)
			elif character_type == self.outcomes[1]:
				character_new = maths_local.Random.choice_flat(self.alphabet.consonants)
			else:
				character_new = " "
			
			generated_text += character_new
			
			generator_index += 1

		return generated_text

if __name__ == "__main__":
	print("MARKOV CHAIN.")
	print("Vowels testing")

