# Есть фрагмент текста, состоящий из предложений.
# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
# Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
# Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.

import re
text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
#Hello and who or yes claro.
pattern = '\d{3,}'

res = re.findall(pattern, text)
print(res)

# def generate_sentence(text: str) -> str:
#     pass


# generate_sentence(a)

# \w - alphanumeric symbols
# \W - NO-alphanumeric symbols
# \d - digits
# \s - all spaces
# \S - NO spaces
# \D - NO-digits
# . - all symbols.
# \b letter limits
# $ - end of string
# ^ - start of string
# | - OR
# [A-z] - range
# [a-zA-Z] - two ranges
# [^a-z] - range with ALL except entered value after ^ sign
# [agtr] - several letters that should be found
# [^agtr] - several letters that shouldn't be found

# quantificators:
# .{3} - should find all SPACES which have 3 symbols left
# \d{3} - should find all SPACES which have 3 digits left
# \d{3,5} - should find all SPACES which have 3 or 4 or 5 digits left
# \d{3,} - should find all SPACES which have 3 or more digits left
# \d+ - should find any 1 digit
# \d* - should find all digits
# colou?r - should find "color" and "colour", because "?" sign means 0 or 1 times.
# <(.*?)> - should find all tags from < until first >
# <(.*)> - should find all tags from < until last >




# "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.." -> "Hello and who or yes claro."
#
# "Hola..." -> Hola.