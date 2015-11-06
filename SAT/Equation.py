__author__ = 'souy'

import copy

def newVar():
    newVar.counter += 1
    return newVar.counter

newVar.counter = 0

class Term:
    def __init__(self,cof,var):
        self.cof=cof
        self.mono=var

    def show(self):
        if self.mono==[0]:
            if self.cof<0:
                return '-e'
            else:
                return 'e'
        if self.cof!=1:
            s = str(self.cof)
            for x in self.mono[:-1]:
                s = s + '*'+'x'+ str(x)
            if len(self.mono) >0:
                s = s+'*x'+str(self.mono[-1])
            return s
        else:
            if self.mono==[]:
                return '1'
            else:
                s = 'x'+str(self.mono[0])
                for x in self.mono[1:-1]:
                    s = s + '*'+'x'+ str(x)
                if len(self.mono) >1:
                    s = s+'*x'+str(self.mono[-1])
                return s



#class Poly:
 #   def __init__(self,):

def showPoly(L):
    if L==[]:
        return ''
    s = L[0].show()
    for m in L[1:-1]:
        if m.cof>0:
            t=' + '
        else:
            t=''
        s= s+ t + m.show()
    if len(L) >1:
        if L[-1].cof>0:
            t=' + '
        else:
            t=''
        s = s +t+ L[-1].show()
    return s

class Eq:
    def __init__(self,lN,comp,rN,lD=None,rD=None):
        self.lN=lN
        self.comp = comp
        self.rN= rN
        if lD is None:
            self.lD=[Term(1,[])]
        else:
            self.lD =lD
        if rD is None:
            self.rD = [Term(1,[])]
        else:
            self.rD= rD


    def switch(self):
        if self.comp=='<=':
            self.comp = '>='
            return
        if self.comp=='>=':
            self.comp = '<='
            return
        if self.comp=='<':
            self.comp = '>'
            return
        if self.comp=='>':
            self.comp = '<'
            return

    def copy(self,eq):
        self= copy.deepcopy(eq)
        #self.rN=eq.rN
        #self.l   D=eq.lD
        #self.rD=eq.rD
        #self.comp=eq.comp

    def show(self):
        if self is None:
            return 'No equation'
        s = ''
        s = s + showPoly(self.lN)

        # ---------------------------------- LHS Denominator ---------------------------
        if len(self.lD)==1 and len(self.lD[0].mono)==0 and self.lD[0].cof==1:
            s=s
        else:
            s='('+s+') / (' + showPoly(self.lD) + ')'
        s = s + ' ' +self.comp+ ' '


        # ------------------------------------- RHS NUmerator --------------------
        if len(self.rD)==1 and len(self.rD[0].mono)==0 and self.rD[0].cof==1:
            s=s
        else:
            s =s +'('
        s = s + showPoly(self.rN)


        # RHS Denominator

        if len(self.rD)==1 and len(self.rD[0].mono)==0 and self.rD[0].cof==1:
            s=s
        else:
            s =s +') / (' + showPoly(self.rD) + ')'
        return s

    def __str__(self):
        return self.show()


def mult(l,r):
    if l==[] or r==[]:
        return []
    if len(l)==1 and len(l[0].mono)==0 and l[0].cof==1:
        return r
    if len(r)==1 and len(r[0].mono)==0 and r[0].cof==1:
        return l
    ret = []
    for tr in l:
        for tr2 in r:
            if tr.mono == [0] or tr2.mono == [0]:
                ret.append(Term(tr.cof*tr2.cof,[0]))
            else:
                c = tr.cof * tr2.cof
                m = tr.mono + tr2.mono
                ret.append(Term(c,m))
    return ret

def scalarmult(c,p):
    if c==0:
        return []
    else:
        for m in p:
            m.cof = c*m.cof
            #ret.append(Term(cof,m.mono))
    #return p


# ------------- Side Effect Free

def seperate(eq,x):
    n = len(eq.lN)
    i=0
    while i<n and x not in eq.lN[i].mono:
        i = i+1
    if x in eq.lN[i].mono:
        eq1= copy.deepcopy(eq)
        eq1.lN[i].mono.remove(x)
        tr = eq1.lN[i]
        eq1.lN.remove(tr)
        scalarmult(-1,eq1.lN)
        eq1.rN = eq1.rN + eq1.lN
        eq1.lN = [Term(1,[x])]
        eq1.rD = [tr]
        if tr.cof<0:
            eq1.switch()
            scalarmult(-1,eq1.rD)
            scalarmult(-1,eq1.rN)
        return  eq1
    else:
        return None


# ------------------------ Side effect free
'''
def equate(eqa,eqb):
    if len(eqa.rD)!=1 or len(eqb.rD)!=1:
        return None
    eq1 = copy.deepcopy(eqa)
    eq2 = copy.deepcopy(eqb)
    eq3 = Eq(Term(1,[]),'=',Term(1,[]))
    if eq1.comp==eq2.comp == '<=':
        eq3.comp = '<='
    if eq1.comp==eq2.comp == '=':
        eq3.comp = '='
    if eq1.comp==eq2.comp == '>=':
        eq3.comp = '>='

    if set(eq1.rD[0].mono) <= set(eq2.rD[0].mono):
        for a in eq1.rD[0].mono:
            eq2.rD[0].mono.remove(a)
        if eq2.rD[0].cof < 0:
            eq3.switch()
        eq3.lN = mult(eq2.rD, eq1.rN)
        if eq1.rD[0].cof<0:
            eq3.switch()
        eq3.rN = scalarmult(eq1.rD[0].cof, eq2.rN)
        return  eq3
    if set(eq1.rD[0].mono) >= set(eq2.rD[0].mono):
        for a in eq2.rD[0].mono:
            eq1.rD[0].mono.remove(a)
        if eq2.rD[0].cof<0:
            eq3.switch()
        eq3.lN = scalarmult(eq2.rD[0].cof, eq1.rN)
        if eq1.rD[0].cof<0:
            eq3.switch()
        eq3.rN = mult(eq1.rD, eq2.rN)

    return eq3

'''

def equateR(lN1,lD1,rN1,rD1,comp):
    if len(rD1)!=1 or len(rD1)!=1:
        return None
    lN = copy.deepcopy(lN1)
    lD = copy.deepcopy(lD1)
    rN = copy.deepcopy(rN1)
    rD = copy.deepcopy(rD1)
    #print "testing lN lD"
#   eq1 = copy.deepcopy(eqa)
#   eq2 = copy.deepcopy(eqb)
    eq3 = Eq(Term(1,[]),comp,Term(1,[]))

    if set(lD[0].mono) <= set(rD[0].mono):
        for a in lD[0].mono:
            rD[0].mono.remove(a)
        if rD[0].cof < 0:
            eq3.switch()
        eq3.lN = mult(rD, lN)
        if lD[0].cof<0:
            eq3.switch()
        scalarmult(lD[0].cof, rN)
        eq3.rN = rN
        return  eq3
    if set(lD[0].mono) >= set(rD[0].mono):
        for a in rD[0].mono:
            lD[0].mono.remove(a)
        if rD[0].cof<0:
            eq3.switch()
        scalarmult(rD[0].cof, lN)
        eq3.lN = lN
        if lD[0].cof<0:
            eq3.switch()
        eq3.rN = mult(lD,rN)

    return eq3

# ----------------------- IMPLEMENTED ONLY FOR POLYNOMIAL EQUATIONS NOT RATIONAL

def simplify(eq):
    scalarmult(-1,eq.rN)
    ret = eq.lN + eq.rN
    i=0
    while i<len(ret):
        j=i+1
        m1 = ret[i]
        #ret[i].mono.sort()
        while j<len(ret):
            m2 = ret[j]
            if set(m1.mono)== set(m2.mono):
                ret[i].cof = m1.cof + m2.cof
                ret.remove(m2)
            j=j+1
        i=i+1
    i=0
    while i<len(ret):
        m=ret[i]
        if m.mono == [0]:
            if m.cof < 0:
                m.cof = -1
            elif m.cof > 0:
                m.cof = 1
        if m.cof ==0:
            ret.remove(m)
        else:
            i=i+1

    i=0
    while i<len(ret) and ret[i].mono !=[]:
            i=i+1
    if i<len(ret):
        k = ret[i]
        ret.remove(k)
        eq.rN = [Term(-1*k.cof,[])]
    else:
        eq.rN = [Term(0,[])]
    eq.lN =ret
    eq.lD = [Term(1,[])]
    eq.rD = [Term(1,[])]
    if eq.rN==[]:
        eq.rN=[Term(0,[])]
    if eq.lN==[]:
        eq.lN=[Term(0,[])]


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield [pool[i] for i in indices[:r]]
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield [pool[i] for i in indices[:r]]
                break
        else:
            return

