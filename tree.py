"""
MARKOV CHAINS
Tree module
"""


# Tree class
from typing_extensions import Self


class Branch:
	"""
	Tree like system.
	The rank 0 is the root.
	"""
	def __init__(self, outcomes_possible: list[str], depth: int, event: str = "root", rank: int = 0) -> None:
		"""
		Create an empty root branch.
		:param outcomes_possible:
		:param depth:
		:param outcome:
		:param rank:
		"""
		self.event: str = event
		# Holding the actual value
		self.value: int = 0
		# Depth of the branch (1 --> 2 --> 3)
		self.rank: int = rank
		# All following branches.
		self.next_branches: list[Self] = self.generate_recursive_branches(outcomes_possible, depth, self.rank);


	def display_all_children(self) -> None:
		"""
		Debug temporary command prompt display of the object and its children. 
		"""

		print(f"r{self.rank} '{self.event}': {self.value}", end=";\n")
		for child in self.next_branches:
			if child.next_branches:
				child.display_all_children()
			else:
				print(f"r{child.rank} '{child.event}': {child.value}", end="; ")
		print()

	def generate_recursive_branches(self, outcomes: list[str], depth: int, rank: int) -> list[Self]:
		next_branches: list[Self] = []
		for outcome in outcomes:
			if depth > 0:
				next_branches.append(Branch(outcomes, depth - 1, outcome, rank + 1)) # type: ignore
			else:
				pass

		return next_branches


if __name__ == "__main__":
	print("MARKOV CHAIN.")
	print("Tree module")

	outcomes1: list[str] = ["a", "b", "c"]
	depth1: int = 2
	branch1: Branch = Branch(outcomes1, depth1)
	branch1.display_all_children()
