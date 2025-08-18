"""
# MARKOV CHAIN Based program.
Probabilities of letter, syllable and words.

## Inspirations
- Veratisium's video: https://www.youtube.com/watch?app=desktop&v=KZeIEiBrT_w;
- The state of AI today (2025);
"""

import vowels
import natural_language as lang



alphabets: dict[str, lang.Alphabet] = {
	'fr': lang.Alphabet(
		lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
		vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	),
	'en': lang.Alphabet(
		lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
		vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	)
}




if __name__ == '__main__':
	print(f'# MAKAROV CHAIN')
	print(f'## Usage in text recognition')

	text_simple_1: str = "Salut tout le monde !"
	result_simple_1: dict[str, dict[str, int]] = vowels.Search.chain_vowels(text_simple_1, alphabets['fr'])
	vowels.Search.chain_vowels_display(result_simple_1, len(text_simple_1))
