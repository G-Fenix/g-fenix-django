_NON_EN = ('tr', 'es', 'ca')

def seo(request):
    path = request.path
    for lang in _NON_EN:
        if path == '/' + lang or path.startswith('/' + lang + '/'):
            path = path[len(lang) + 1:] or '/'
            break
    if not path.startswith('/'):
        path = '/' + path
    return {
        'CANONICAL_PATH': path,
        'SITE_BASE': 'https://g-fenix.com',
    }
