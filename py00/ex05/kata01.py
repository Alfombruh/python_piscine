kata = {
    'Python' : 'Guide van Rossum',
    'Ruby' : 'Yukihiro Matsumoto',
    'PHP' : 'Rasmus Lerdorf',
    }
keys = sorted(kata.keys())
print('{0} was created by {1}\n{2} was created by{3}\n{4} was created by {5}'.format(*keys, *(kata[key]for key in keys)))
