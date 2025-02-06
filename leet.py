from itertools import permutations

# Print header
print("[List.Rules:Leet]")

# Original leet_map with potential non-printable characters
leet_map = {
    'a': ['4', '@', '^'],
    'b': ['8', '6', 'ß', '3'],
    'c': ['[', '{', '<', '('],
    'd': [')', '|', '1', '?'],
    'e': ['3', '&'],
    'f': ['ƒ', 'v'],
    'g': ['6', '9', '&'],
    'h': ['#', '4', '?'],
    'i': ['1', '|', '!'],
    'j': [']'],
    'k': ['x', '|'],
    'l': ['1', '7', '|', '!', '2'],
    'm': [],
    'n': ['И', '2', 'r', '^'],
    'o': ['0', 'p'],
    'p': ['9', '?'],
    'q': ['0', '2', '9', '&'],
    'r': ['7', '2', '9', '4', '3'],
    's': ['z', '5', '$', '2'],
    't': ['+', '7', '|'],
    'u': ['µ'],
    'v': ['u'],
    'w': ['Ш'],
    'x': ['%', '?', '*'],
    'y': ['7', '΄', 'j'],
    'z': ['2', 's', '7', '%'],
}

# Function to remove non-printable characters from the leet_map
def remove_non_printable(leet_map):
    return {
        key: [char for char in chars if char.isprintable()]
        for key, chars in leet_map.items()
    }

# Create a new leet_map with non-printable characters removed
clean_leet_map = remove_non_printable(leet_map)

# Function to format substitutions correctly
def format_subs(subs):
    if subs[0]==']':
        return subs[0]
    return f"[{''.join(subs)}]"  # Use brackets for multiple characters

# Generate all pairs of distinct letters
for (letter1, subs1), (letter2, subs2) in permutations(clean_leet_map.items(), 2):
    if not subs1 or not subs2:  # Skip empty lists
        continue
    subs1_formatted = format_subs(subs1)
    subs2_formatted = format_subs(subs2)
    rule = f's{letter1}{subs1_formatted} s{letter2}{subs2_formatted}'
    print(rule)
