import Equation


def validVar(x,eq):            # --------------- should be present in exactly one monomial of a simplified equation
    flag=0
    for m in eq.lN:
        if x in m.mono:
            if flag ==1:
                return 0        # --------------- There are more than on instance of x
            flag = 1
    if flag ==0:
        return 2                # --------------- there are no instance of x
    else:
        return 1                # --------------- There is exactly on instance of x

def validEq(x,E):
    for e in E:
        if validVar(x,e)==0:
            return 0            # ----------------- Some equations have more than 1 instance of x
    return 1

def eliminateS(x,E):
    if validEq(x,E)!=1:
        return
    else:
        E1=[]
        i=0
        while i<len(E):
            if validVar(x,E[i])==1:
                E1.append(Equation.seperate(E[i],x))
                E.remove(E[i])
            else:
                i=i+1
        for i in range(0,len(E1)-1,1):
            e = Equation.equate(E1[i],E1[i+1])
            Equation.simplify(e)
            E.append(e)
    return


def subFunc(El,p):
#    print 'Now '+str(p)
    for i in range(len(El)-1):
        e1 = Equation.equate(El[p[i]],El[p[i+1]])
        Equation.simplify(e1)
        print 'Elinated and Simplified:  '+e1.show()
    print 'Before :- \n '+' '.join([t.show()+'\n' for t in El])

def subFunc2(El,Ee,Eg,L):
    En =[]
    p=L[0]
    p2=L[1]

    if len(El)>1:
        for i in range(len(El)-1):
            e1 = Equation.equateR(El[p[i]].rN,El[p[i]].rD,El[p[i+1]].rN,El[p[i+1]].rD,'<=')
            Equation.simplify(e1)
            En.append(e1)

    if Ee != [] and p!=[]:
        ee = Ee[0]
        e1 = Equation.equateR(El[p[-1]].rN,El[p[-1]].rD,ee.rN,ee.rD,'<=')
        Equation.simplify(e1)
        En.append(e1)

    if Ee!= []:
        for i in range(len(Ee)-1):
            e1 = Equation.equateR(Ee[i].rN,Ee[i].rD,Ee[i+1].rN,Ee[i+1].rD,'=')
            Equation.simplify(e1)
            En.append(e1)

    if Ee == [] and p!=[] and p2!=[]:
        e1 = Equation.equateR(El[p[-1]].rN,El[p[-1]].rD,Eg[p2[0]].rN,Eg[p2[0]].rD,'<=')
        Equation.simplify(e1)
        En.append(e1)

    if Eg!=[] and Ee !=[]:
        ee = Ee[-1]
        e1 = Equation.equateR(ee.rN,ee.rD,Eg[p2[0]].rN,Eg[p2[0]].rD,'<=')
        Equation.simplify(e1)
        En.append(e1)

    if len(Eg)>1:
        for i in range(len(Eg)-1):
            e1 = Equation.equateR(Eg[p2[i]].rN,Eg[p2[i]].rD,Eg[p2[i+1]].rN,Eg[p2[i+1]].rD,'<=')
            Equation.simplify(e1)
            En.append(e1)
    return En

def eliminateA(x,E):
    if validEq(x,E)!=1:
        return 0
    E0=[]
    E1=[]
    E2=[]
    i=0
    while i < len(E):
        e=E[i]
        if validVar(x,e) ==1:
            e1= Equation.seperate(e,x)
            if e1.comp == '>=':
                E0.append(e1)
                E.remove(e)
            else:
                if e1.comp == '=':
                    E1.append(e1)
                    E.remove(e)
                else:
                    if e1.comp == '<=':
                        E2.append(e1)
                        E.remove(e)
                    else:
                        i=i+1
        else:
            i=i+1

    #print 'Here\n' +' '.join([t.show()+'\n' for t in E])
    print 'Before Call E0 :- \n '+' '.join([t.show()+'\n' for t in E0])
    print 'Before Call E1 :- \n '+' '.join([t.show()+'\n' for t in E1])
    print 'Before Call E2:-\n '+' '.join([t.show()+'\n' for t in E2])


    #    for p1 in Equation.permutations(range(len(E0))):
    #        for p2 in Equation.permutations(range(len(E2))):
    #       Make the permutation and handle non-determinism
    L =[range(len(E0)),range(len(E2))]
    En = subFunc2(E0,E1,E2,L)
    print 'New equations :- \n '+' '.join([t.show()+'\n' for t in En])
    E.extend(En)
    print 'Modified E :- \n '+' '.join([t.show()+'\n' for t in E])
    return 1


def eliminateOrder(E,L):
    if L==[]:
        return
    else:
        x = L[0]
        L = L[1:]
        print 'Trying to eliminate Variable x'+str(x)+' from the Equation system'
        if eliminateA(x,E) ==0:
            print 'Not a valid order of elimination'
            return
        else:
            eliminateOrder(E,L)


def solve(e):
    if len(e.lN)>1 or len(e.rN)>1:
        print 'Can not Solve!'
        return 2    # Cannpt solve.
    if len(e.lN[0].mono) >1 or len(e.rN[0].mono)>1:
        print 'Contains variables!'
        return 2
    #print str(e.lN[0].cof)+ ' ' +str(e.lN[0].mono) + ' '+ e.comp
    if e.lN[0].mono == [0]:
        if e.lN[0].cof<0:
            Equation.scalarmult(-1,e.rN)
            e.switch()
        if e.comp =='<=':
            if e.rN[0].cof == 0:
                return False
            return 0 <= e.rN[0].cof
        if e.comp =='>=':
            return 0 >= e.rN[0].cof
        if e.comp =='=':
            if e.rN[0].cof == 0:
                return False
            return 0 == e.rN[0].cof
    else:
        if e.comp =='<=':
            return e.lN[0].cof <= e.rN[0].cof
        if e.comp =='>=':
            return e.lN[0].cof >= e.rN[0].cof
        if e.comp =='=':
            return e.lN[0].cof == e.rN[0].cof


def solveE(E):
    for e in E:
        if solve(e)!= True:
            return False
    return True

'''
o = Equation.Term(1,[0])
l = Equation.Term(1,[])

t = Equation.Term(0.5,[6,Equation.newVar(),Equation.newVar(),Equation.newVar()])
t1 = Equation.Term(0.4,[])
t2 = Equation.Term(0.3,[1,2,3])

nl=Equation.Term(1,[1,2])
n2=Equation.Term(0.8,[1,2,4])

eq1 = Equation.Eq([t,nl],'<=',[Equation.Term(0.7,[])])                  # 0.5 x1 x2 x3 x6 + x1 x2 <= 0.7
eq2 = Equation.Eq([nl,t2],'<=',[t1])                                    # x1 x2 + 0.3 x1 x2 x3 <= 0.4
eq3 = Equation.Eq([n2 , t2],'>=',[o])                                     # 0.8 x1 x2 x4 + 0.3 x1 x2 x3 > 0
eq4 = Equation.Eq([Equation.Term(1,[3]),Equation.Term(1,[4])],'=',[l])    # x3 + x4 = 1

eq3o = Equation.Eq([Equation.Term(1,[3])],'>=',[o])            # x3 >=0
eq3l = Equation.Eq([Equation.Term(1,[3])],'<=',[l])            # x3 <=1
eq2o = Equation.Eq([Equation.Term(1,[2])],'>=',[o])            # x2 >=0
eq2l = Equation.Eq([Equation.Term(1,[2])],'<=',[l])            # x2 <=1
eq1o = Equation.Eq([Equation.Term(1,[1])],'>=',[o])            # x1 >=0
eq1l = Equation.Eq([Equation.Term(1,[1])],'<=',[l])            # x1 <=1
eq6o = Equation.Eq([Equation.Term(1,[6])],'>=',[o])            # x6 >=0
eq6l = Equation.Eq([Equation.Term(1,[6])],'<=',[l])            # x6 <=1
eq4o = Equation.Eq([Equation.Term(1,[4])],'>=',[o])            # x4 >=0
eq4l = Equation.Eq([Equation.Term(1,[4])],'<=',[l])            # x4 <=1

#print 'EQ1: ' + eq1.show()
#print 'EQ2: ' +eq2.show()
#print 'EQ3: ' + eq3.show()

E= [eq1,eq2,eq3,eq4,eq1l,eq2l,eq3l,eq4l,eq6l,eq1o,eq2o,eq4o,eq6o]
#print validVar(3,eq2)
#eliminateS(3,E)

#print 'Result :' + E[2].show()
#Equation.simplify(E[0])

#print ' '.join([t.show()+'\n' for t in E])

#print '\n'.join(str(t) for t in Equation.permutations(range(3)))

#ret = Equation.seperate(eq1,6)
#print ret.show()
#print eq1.show()
#print validVar(6,eq2)
#eliminateA(6,E)

L = [6,4,3,2,1]

#eliminateA(6,E)
#print 'Finanly\n'+' '.join([t.show()+'\n ' for t in E])
#eliminateA(4,E)
eliminateOrder(E,L)
E.append(eq3o)
print 'Finanly\n'+' '.join([t.show()+'\n ' for t in E])

#print 'Solving ' + E[6].show()+ ' : ' + str(solve(E[6]))

print 'SOLVE : '+str(solveE(E[-1:]))


n = Equation.Eq([Equation.Term(-1,[3])],'<=',[Equation.Term(0,[])])
print 'Test '+ n.show()

m = Equation.seperate(n,3)
print 'Test '+ m.show()


l = Equation.mult([Equation.Term(1,[]),o], [Equation.Term(-0.3,[1,2])])
print 'Multiply\n'+' '.join([t.show()+' + ' for t in l])


new = Equation.Eq([Equation.Term(1,[]),o],'<=',[Equation.Term(1,[]),o],[Equation.Term(-0.3,[1,2])],[Equation.Term(1,[])])
print "THERE \n"+  new.show()
m = Equation.equateR([Equation.Term(1,[]),o],[Equation.Term(-0.3,[1,2])],[Equation.Term(1,[]),o],[Equation.Term(1,[])],'<=')
print "THERE \n"+ m.show()

n = Equation.Eq([Equation.Term(0,[]),o],'>=',[Equation.Term(-0.3,[1,2]),o])

print m.show()
Equation.simplify(m)
print n.show()

ln=[o,Equation.Term(-0.3,[1,2,3])]
ld=[Equation.Term(0.8,[1,2])]

rn= [o]
rd= [l]
n = Equation.equateR(ln,ld,rn,rd,'<=')
print 'check '+n.show()
Equation.simplify(n)
print 'check '+n.show()
'''