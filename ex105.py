def notas(*n,sit = False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r ['media'] >=5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
        return r


#Programa Principal
resp = notas(9.5,4.5,8.5, sit=True)
print(resp)









