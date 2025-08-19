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
	search_vowels_fr: vowels.SearchVowels = vowels.SearchVowels(depth=2, alphabet=alphabets["fr"])
	search_vowels_fr.analyse(text_simple_1)
	search_vowels_fr.display_all_children()