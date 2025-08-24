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

	text_simple_1: str = "Salut tout le monde"
	# Search vowels for French texts.
	search_vowels_fr: vowels.Vowels = vowels.Vowels(depth=2, alphabet=alphabets["fr"])
	
	search_vowels_fr.analyse(text_simple_1)
	with open("./assets/LesTroisMousquetaires.txt", "r", encoding="utf-8") as f:
		search_vowels_fr.analyse(f.read())
	
	search_vowels_fr.display_all_children()
	
	for _ in range(50):
		build: str = search_vowels_fr.build_from_chain(15, include_spaces=True)
		print(f"{build=}")