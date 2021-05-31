import requests

def get_frequencies(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'ATGC'}

def format_frequencies(freq):
    return ', '.join(['%s: %.2f' % (base, freq[base]) for base in freq])

def handle(req):
    """ Takes a URL or a string as request """
    try:
        r = requests.get(req)
    except requests.exceptions.MissingSchema:
        dna = req # we assume it's a string
        if not dna:
            return
    else:
        dna = ''.join(c for c in r.text if c != '\n')
    return format_frequencies(get_frequencies(dna)) 