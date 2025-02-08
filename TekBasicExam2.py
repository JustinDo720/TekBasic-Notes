# Recursive Function for combinations of a string
# Including Empty SubSequence

"""

Hint:
1) Include the current character in combination
2) exclude it

So what I'm thinking is we loop through the string
- 'abc' we'll take a look at a

Then we do a second loop to concate a with the rest like:
- 'aa', 'ab', 'ac' 'abc'

We're def going to use nested loops for this problem

But nested loops isn't recursive

so What if we generate a combination with the first letter...
Remove it and return that string to generate combinations again

"""
def generate_combinations(s):
    # Need a place to store all of our combinations
    # I can't figure out how to add the empty string so we'll check if there's an empty string already
    combinations = ['']

    # Break case
    if len(s) == 1:
        # We need to return that string
        return [s[0]]

    # But We also need the remaining string but remember strings are immutable
    # So we could only slice but the slice logic is a bit difficult therefore lets change it to a list
    l = list(s)  # Remove our main string
    curr_sub_string = l.pop(0)
    # Adding the current sub string to the list
    combinations.append(curr_sub_string)
    # Finding all the possible combinations of that string with another
    for ss in ''.join(l):
        combinations.append(f'{curr_sub_string}{ss}')

    # We need to add the full combination
    if s not in combinations:
        combinations.append(s)

    # Recursive step
    # With that Recursive step we need to return combinations lists
    return combinations + list(generate_combinations("".join(l)))


ans = generate_combinations('abc')
print(f'My Answer: {ans}')

ans2 = generate_combinations('dog')
print(f'My Answer: {ans2}')

ans3 = generate_combinations('a')
print(f'My Answer: {ans3}')

ans4 = generate_combinations('zxy')
print(f'My Answer: {ans4}')

ans5 = generate_combinations('ab')
print(f'My Answer: {ans5}')