"""
# MARKOV CHAIN Based program.
Probabilities of letter, syllable and words.

## Inspirations
- Veratisium's video: https://www.youtube.com/watch?app=desktop&v=KZeIEiBrT_w;
- The state of AI today (2025);
"""

import vowels # type: ignore
import letters # type: ignore
import natural_language as lang
import random
import time
import threading
import time_widgets

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


def execute_search_vowels_fr() -> None:
	print("### Search vowels for French texts.")
	search_vowels_fr: vowels.VowelsBonzai = vowels.VowelsBonzai(depth=3, alphabet=alphabets["fr"])
	text_simple_1: str = "Salut tout le monde"
	search_vowels_fr.analyse(text_simple_1)
	with open("./assets/LesTroisMousquetaires.txt", "r", encoding="utf-8") as f:
		search_vowels_fr.analyse(f.read())
	
	search_vowels_fr.display_all_children()
	
	build_quantity: int = 50
	print(f"## Builds ({build_quantity})")
	for _ in range(build_quantity):
		build: str = search_vowels_fr.build_from_chain(15, include_spaces=True)
		print(f"{build}")

def execute_search_letters_fr() -> None:
	print("### Search letter combinations for French texts.")
	search_letters_fr: letters.LettersBonzai = letters.LettersBonzai(
		depth=3, 
		alphabet=alphabets["fr"]
	)
	search_letters_fr_time: float = time.monotonic()
	text_simple_1: str = "Salut tout le monde"
	search_letters_fr.analyse(text_simple_1)
	with open("./assets/LesTroisMousquetaires.txt", "r", encoding="utf-8") as f:
		search_letters_fr.analyse(f.read())
	search_letters_fr_time: float = time.monotonic() - search_letters_fr_time

	search_letters_fr.display_all_children()
	print(f"Search took: {search_letters_fr_time:.2f}s\n")

	build_quantity: int = 10
	print(f"#### Builds ({build_quantity})")
	for _ in range(build_quantity):
		build: str = search_letters_fr.build_from_chain(
			random.randint(10, 40),
			include_spaces=True,
			exponent=1.35,
			factor=0.5
		)
		print(f"{build}")


if __name__ == '__main__':
	print(f'# MAKAROV CHAIN')
	print(f'## Usage in text recognition')

	time_widgets_thread = threading.Thread(target=time_widgets.uptime_count, args=(0.1,), daemon=True)
	time_widgets_thread.start()
	exe_thread = threading.Thread(target=execute_search_letters_fr, args=(), daemon=True)
	exe_thread.start()
	exe_thread.join()
	
		