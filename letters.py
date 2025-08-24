"""
MARKOV CHAIN
Search vowels
"""
import tree
import natural_language as lang
import maths_local
# from typing_extensions import Self


class LettersBonzai(tree.BranchBonzai):
	"""
	Contain all search static methods, for the sake of organization.
	"""
	def __init__(self, depth: int, alphabet: lang.Alphabet) -> None:
		self.outcomes: list[str] = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.alphabet: lang.Alphabet = alphabet
		self.root_name: str = "total"
		self.root_position: int = 0
		self.depth: int = depth

		self.filter_special: bool = True
		self.filer_double_spaces: bool = True

		super().__init__(self.outcomes, depth, self.root_name, self.root_position)

	def case_map(self, case_value: str) -> str:
		"""
		For a given case, return the event name.
		"""
		event_name: str = ""
		if case_value in self.outcomes:
			event_name = case_value
		else:
			raise ValueError(f"Event name not a letter: {case_value}")

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
		while reader_index < len(text) - self.depth + 1:
			# Get the characters
			characters: list[str] = []
			sub_index: int = 0
			while len(characters) < self.depth and (reader_index + sub_index) < len(text):
				# Validation.
				character_valid: bool = True
				character: str = text[reader_index + sub_index].lower()
				if character not in self.outcomes:
					character_valid = False
				elif reader_index + sub_index < len(text) - 1:
					if (self.filer_double_spaces
		 				and text[reader_index + sub_index] in self.alphabet.spaces
						and text[reader_index + sub_index + 1] in self.alphabet.spaces
					):
						character_valid = False
				# Append char if valid.
				if character_valid:
					characters.append(character)
				sub_index += 1
			
			# print(f"{min(reader_index % self.depth, 1) * "	"} {reader_index} {characters}")
			
			self.update_tree(characters)
			reader_index += 1

		return self

	def update_tree(self, list_cases: list[str], branch_in: tree.BranchBonzai|None = None) -> None:
		"""
		Modify recursively the tree from the list of cases given, starting from the firt
		"""
		# Default.
		branch: tree.BranchBonzai
		if branch_in is None:
			branch = self
		else:
			branch = branch_in

		# Handle present case; extract the event.
		case_value: str = list_cases[0].lower()
		event_name: str = self.case_map(case_value)

		# Get next branch.
		branch = branch.get_branch(event_name)
		branch.value += 1
		list_cases.pop(0)
		# Recursion.
		if len(list_cases) > 0:
			self.update_tree(list_cases, branch)

	
	def build_from_chain(self, length: int, include_spaces: bool, exponent: float, factor: float) -> str:
		"""
		Generate a chain of character based on the probability table, obtained by `analysing`.
		"""
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
			next_events: dict[str, int] = branch.next_to_dict(exponent)
			if not include_spaces:
				next_events.pop(self.outcomes[0], None)
			character_new: str = maths_local.Random.choice_pondered(next_events)
			generated_text += character_new
			
			generator_index += 1

		return generated_text