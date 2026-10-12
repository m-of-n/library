import yaml,sys
def score(ans):
    # ans: {practice: {'A':[v1,v2,v3],'B':[v1,v2,v3]}}
    out={}
    for p,s in ans.items():
        out[p]=round(sum((s['A'][i]+s['B'][i])/2 for i in range(3)),4)
    return out
for f in sys.argv[1:]:
    d=yaml.safe_load(open(f))
    got=score(d['answers'])
    ok=all(abs(got[p]-d['expected']['practice_score'][p])<1e-9 for p in got)
    print(f,got,'OK' if ok else 'FAIL')
