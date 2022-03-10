##################################################################
################## Exercise 05 - kata01.py #######################

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for lang,creator in kata.items():
    print("{} was created by {}".format(lang, creator))