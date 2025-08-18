"""
MARKOV CHAIN
Search vowels
"""

import tree
import natural_language as lang

class Search:
	"""
	Contain all search static methods, for the sake of organization.
	"""
	@staticmethod
	def chain_vowels(text: str, alphabet: lang.Alphabet) -> dict[str, dict[str, int]]:
		"""
		Function: Establish the probability chain from moving between consonants and vowels
		:param text: string to analyze.
		:param alphabet: entire alphabet structure that contain all letters, and all vowels.
		:returns: Dictionary containing the total number of character and the number of travels between each combinations.

		"""
		# Vars
		results: dict[str, dict[str, int]] = {
			'consonant': {
				'consonant': 0,
				'vowel': 0
			},
			'vowel': {
				'consonant': 0,
				'vowel': 0,
			}
		}
		results_depth = 1
		results_root_name = "total"
		results_outcomes = ["consonant", "vowel", "space"]
		_results: tree.Branch = tree.Branch(results_outcomes, results_depth+1, results_root_name)
		i: int = 0

		# Main loop
		while i < len(text) - 1:
			char_0: str = text[i]
			char_1: str = text[i + 1]

			if char_0 in alphabet.vowels:
				if char_1 in alphabet.vowels:
					results['vowel']['vowel'] += 1
				else:
					results['vowel']['consonant'] += 1
			else:
				if char_1 in alphabet.vowels:
					results['consonant']['vowel'] += 1
				else:
					results['consonant']['consonant'] += 1

			i += 1

		return results

	@staticmethod
	def chain_vowels_display(result: dict[str, dict[str, int]], text_length: int):
		print(f"Search vowel chain results, for a text of length {text_length}: ")
		print(f"- Vowel -> Vowel = {result['vowel']['vowel'] / text_length:.2%} ({result['vowel']['vowel']})")
		print(f"- Vowel -> Consonant = {result['vowel']['consonant'] / text_length:.2%} ({result['vowel']['consonant']})")
		print(f"- Consonant -> Vowel = {result['consonant']['vowel'] / text_length:.2%} ({result['consonant']['vowel']})")
		print(f"- Consonant -> Consonant = {result['consonant']['consonant'] / text_length:.2%} ({result['consonant']['consonant']})")
