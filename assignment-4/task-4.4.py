from typing import Callable

# ---------- Prompts you'd send to an LLM ----------
zero_shot_prompt = (
    "Write a Python function named count_vowels(s) that returns the number of vowels "
    "in the input string s. Count only a, e, i, o, u (case-insensitive)."
)

few_shot_prompt = (
    "# Example 1\n"
    "Input: 'hello' -> Output: 2\n"
    "# Example 2\n"
    "Input: 'AEIOU' -> Output: 5\n"
    "# Now produce the function:\n"
    "Write a Python function named count_vowels(s) that returns the number of vowels "
    "in the input string s. Count only a, e, i, o, u (case-insensitive)."
)

# ---------- Simulated LLM outputs (functions) ----------
# Zero-shot style: straightforward, explicit loop
def count_vowels_zero_shot(s: str) -> int:
    s = s.lower()
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count

# Few-shot style: compact, uses generator expression and a set for membership
def count_vowels_few_shot(s: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for ch in s.lower() if ch in vowels)

# ---------- Tests ----------
tests = [
    ("hello", 2),
    ("AEIOU", 5),
    ("rhythm", 0),         # no classic vowels
    ("Beautiful!", 5),     # mixed case, punctuation
    ("", 0),               # empty
    ("Café àéîõü", 4),     # contains some accented vowels (note: our simple count ignores accents)
]

def run_tests(fn: Callable[[str], int]):
    results = []
    for s, expected in tests:
        got = fn(s)
        results.append((s, expected, got))
    return results

if __name__ == "__main__":
    print("Zero-shot prompt:\n", zero_shot_prompt, "\n")
    print("Few-shot prompt:\n", few_shot_prompt, "\n")

    z_results = run_tests(count_vowels_zero_shot)
    f_results = run_tests(count_vowels_few_shot)

    print("Results (format: input | expected | zero_shot | few_shot):")
    for ((s, exp, gz), (_, _, gf)) in zip(z_results, f_results):
        print(f"'{s}' | {exp} | {gz} | {gf}")

    # Short comparison summary
    print("\nSummary:")
    print("- Zero-shot: often produces a correct, minimal implementation from the single instruction.")
    print("- Few-shot: by providing examples first, the model will more likely match expected behavior and style.")
    print("- Example caveat: neither implementation handles accented vowels; add normalization if needed (NFKD + filter).")