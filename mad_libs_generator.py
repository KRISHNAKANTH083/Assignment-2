story = """
Today I went to the {place}. I saw a {adjective} {animal}
{verb} very {adverb}. It made me feel {feeling} and I
laughed for {number} minutes!
"""

place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb (ending with -ing): ")
adverb = input("Enter an adverb: ")
feeling = input("Enter a feeling: ")
number = input("Enter a number: ")

final_story = story.format(
    place=place,
    adjective=adjective,
    animal=animal,
    verb=verb,
    adverb=adverb,
    feeling=feeling,
    number=number
)

print("\n--- Your Mad Libs Story ---")
print(final_story)
