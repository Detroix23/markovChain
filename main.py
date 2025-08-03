"""
# MARKOV CHAIN Based program.
Probabilities of letter, syllable and words.

## Inspirations
- Veratisium's video: https://www.youtube.com/watch?app=desktop&v=KZeIEiBrT_w;
- The state of AI today (2025);
"""

alphabet: dict[str, dict[str, list[str]]] = {
	'fr': {
		'lower': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
		'vowels': ['a', 'e', 'i', 'o', 'u', 'y']
	}
}


class Search:
	"""
	Contain all search static methods, for the sake of organization.
	"""
	@staticmethod
	def chain_vowels(text: str, alphabet: dict[str, list[str]]) -> dict[str, dict[str, int]]:
		"""
		Function: Establish the probability chain from moving between consonants and vowels
		:param text: string to analyze.
		:param alphabet: entire alphabet structure that contain all letters, and all vowels.
		:returns: Dictionary containing the total number of character and the number of travels between each combinations.

		"""
		# Verify parmaters
		try:
			alphabet['vowels']
		except Exception as e:
			raise ValueError(f'(X) - Alphabet provided does not contain the necessary data: {Exception}')

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
		i: int = 0

		# Main loop
		while i < len(text) - 1:
			char_0: str = text[i]
			char_1: str = text[i + 1]

			if char_0 in alphabet['vowels']:
				if char_1 in alphabet['vowels']:
					results['vowel']['vowel'] += 1
				else:
					results['vowel']['consonant'] += 1
			else:
				if char_1 in alphabet['vowels']:
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


if __name__ == '__main__':
	print(f'# MAKAROV CHAIN')
	print(f'## Usage in text recognition')

	text_simple_1: str = "Salut tout le monde !"
	result_simple_1: dict = Search.chain_vowels(text_simple_1, alphabet['fr'])
	Search.chain_vowels_display(result_simple_1, len(text_simple_1))


