"""
MARKOV CHAINS
Tree module
"""


# Tree class
from typing_extensions import Self
from enum import Enum

class Settings(Enum):
	SELF = 1

class BranchBonzai:
	"""
	Tree like system.
	The rank 0 is the root.
	Bonzai because it is not scalable, and do not use Numpy.
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

	def __str__(self) -> str:
		return f"Branch: event={self.event}, value={self.value}, rank={self.rank}, child_quantity={len(self.next_branches)}"
	
	def __repr__(self) -> str:
		return f"Branch: event={self.event}, value={self.value}, rank={self.rank}, child_quantity={len(self.next_branches)}"

	def display_all_children(self) -> None:
		"""
		Debug temporary command prompt display of the object and its children. 
		"""
		# Main loop
		for _ in range(self.rank):
			print("  ", end="")
		print(f"r{self.rank} '{self.event}': {self.value}", end=";\n")
		for child in self.next_branches:
			if child.next_branches:
				child.display_all_children()
			else:
				for _ in range(0, child.rank):
					print("  ", end="")
				print(f"r{child.rank} '{child.event}': {child.value}", end="; ")
		print()

	def generate_recursive_branches(self, outcomes: list[str], depth: int, rank: int) -> list[Self]:
		next_branches: list[Self] = []
		for outcome in outcomes:
			if depth > 0:
				next_branches.append(BranchBonzai(outcomes, depth - 1, outcome, rank + 1)) # type: ignore

		return next_branches

	def get_branch(self, event: str, repeat: int = 1) -> Self:
		"""
		Find and return the branch for the given event string.
    	"""
		branch: Self = self

		for _ in range(repeat):
			i: int = 0
			found_event: bool = False
			while i < len(branch.next_branches) and not found_event:
				if branch.next_branches[i].event == event:
					found_event = True
				else:
					i += 1
			if found_event:
				branch = branch.next_branches[i]
			elif len(branch.next_branches) == 0:
				raise ValueError(f"(X) - No children.")
			else:
				raise ValueError(f"(X) - Event non existent in branches: '{event}'.")

		return branch
	
	def next_to_dict(self) -> dict[str, int]:
		next_dict: dict[str, int] = {}
		for branch in self.next_branches:
			next_dict[branch.event] = branch.value

		return next_dict

if __name__ == "__main__":
	print("MARKOV CHAIN.")
	print("Tree module")

	outcomes1: list[str] = ["a", "b", "c", "d"]
	depth1: int = 2
	tree1: BranchBonzai = BranchBonzai(outcomes1, depth1)
	tree1.display_all_children()
	branch1_1: BranchBonzai = tree1.get_branch(outcomes1[0])
	branch1_2: BranchBonzai = tree1.get_branch(outcomes1[0], repeat=2)
	branch1_3: BranchBonzai = branch1_1.get_branch(outcomes1[1])
	branch1_4: BranchBonzai = tree1.get_branch(outcomes1[0]).get_branch(outcomes1[0])

	print(f"Branches: \n\t{branch1_1=}, \n\t{branch1_2=}, \n\t{branch1_3=}, \n\t{branch1_4=}")
	print(f"Cmp: {branch1_2 == branch1_4}")