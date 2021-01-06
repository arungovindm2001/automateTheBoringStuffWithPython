## 1. What is the function that creates Regex objects?

`re.compile()`

## 2. Why are raw strings often used when creating Regex objects?

Raw strings are used so that backslashes do not have to be escaped.

## 3. What does the search() method return?

Match Objects

## 4. How do you get the actual strings that match the pattern from a Match object?

`group()`

## 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)' , what does group 0 cover? Group 1 ? Group 2 ?

`group(0)` will return the entire matched text.
`group(1)` will return the first set of parenthesis.
`group(2)` will return the second set of parenthesis.

## 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

We use backlashes (escape character) to put parenthesis and period characters to match them.

## 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

If the regex has no groups, a list of strings return otherwise a list of tuples of strings return.

## 8. What does the | character signify in regular expressions?

**'or'**

## 9. What two things does the ? character signify in regular expressions?

1. Matches zero or one of the preceding group.
2. Used for non-greedy matching.

## 10. What is the difference between the + and * characters in regular expressions?

The + matches **one or more** of the preceding group.<br />
The * matches **zero or more** of the preceding group.

## 11. What is the difference between {3} and {3,5} in regular expressions?

The {3} matches **exactly 3** of the preceding group.<br />
The {3,5} matches **at least 3 and at most 5** of the preceding group.

## 12. What do the \d , \w , and \s shorthand character classes signify in regular expressions?

\d , \w , and \s match a digit, word, or space character, respectively.	

## 13. What do the \D , \W , and \S shorthand character classes signify in regular expressions?

\D , \W , and \S match anything except a digit, word, or space character, respectively.

## 14. What is the difference between .* and .*? ?

.* - used for **greedy** matching<br />
.*? - used for **non-greedy** matching

## 15. What is the character class syntax to match all numbers and lowercase letters?

`[0-9a-z]`

## 16. How do you make a regular expression case-insensitive?

`re.compile(<first-argument>,re.IGNORECASE)`

## 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile() ?

. character normally matches all characters except newline.<br />
If re.DOTALL is passed as the second argument to re.compile(), then . character will also match newline.

##18. If numRegex = re.compile(r'\d+') , what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

`'X drummers, X pipers, five rings, X hens'`

## 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

It allows us to add whitespace and comments.

## 20. How would you write a regex that matches a number with commas for every three digits? It must match the following: '42', '1,234', '6,368,745', but not the following: '12,34,567' (which has only two digits between the commas), '1234' (which lacks commas)

`re.compile(r'^\d{1,3}(,\d{3})*$')`

## 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following: 'Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe' but not the following: 'haruto Watanabe' (where the first name is not capitalized), 'Mr. Watanabe' (where the preceding word has a nonletter character), 'Watanabe' (which has no first name), 'Haruto watanabe' (where Watanabe is not capitalized)

`re.compile(r'[A-Z][a-z]*\sWatanabe')`

## 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following: 'Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.''Alice throws Apples.', 'BOB EATS CATS.' but not the following: 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.'

`re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`

