__author__ = 'souy'
import copy,elemination,Equation


def eli_permutation(E,L):
    if L ==[]:
        return elemination.solveE(E)
    else:
        #E = copy.deepcopy(E1)
        x=L[0]
        L=L[1:]
        if elemination.validEq(x,E)!=1:
            print 'Incorrect order of elimination!'
            return True
        #print 'Trying to eliminate Variable x'+str(x)+' from the Equation system :::::::'
        E0=[]
        E1=[]
        E2=[]
        i=0
        while i < len(E):
            e=E[i]
            if elemination.validVar(x,e) ==1:
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
        #print 'Before Call E0 :- \n '+' '.join([t.show()+'\n' for t in E0])
        #print 'Before Call E1 :- \n '+' '.join([t.show()+'\n' for t in E1])
        #print 'Before Call E2:-\n '+' '.join([t.show()+'\n' for t in E2])
        # The Permutation
        for p1 in Equation.permutations(range(len(E0))):
            for p2 in Equation.permutations(range(len(E2))):
                P=[p1,p2]
                En = elemination.subFunc2(E0,E1,E2,P)
                Ec = copy.deepcopy(E)
                L1 = copy.deepcopy(L)
                Ec.extend(En)
                #print 'Permutation  '+ str(P)
                #print 'Ec\n'+''.join([t.show()+'\n' for t in Ec])
                #print 'E\n'+''.join([t.show()+'\n' for t in E])
                ans = eli_permutation(Ec,L1)
                #print 'After Call E0 :- \n '+' '.join([t.show()+'\n' for t in E0])
                #print 'After Call E1 :- \n '+' '.join([t.show()+'\n' for t in E1])
                #print 'After Call E2:-\n '+' '.join([t.show()+'\n' for t in E2])
                #print 'ANSWER TO THE Next BRANCH '+str(ans)
                if  ans != False:
                    print 'Before\n'+''.join([t.show()+'\n' for t in Ec])
                    return True
        return False

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
#eq2o = Equation.Eq([Equation.Term(1,[2])],'>=',[o])            # x2 >=0
eq2o = Equation.Eq([Equation.Term(1,[2])],'>=',[Equation.Term(0.9,[])])
eq2l = Equation.Eq([Equation.Term(1,[2])],'<=',[l])            # x2 <=1
#eq1o = Equation.Eq([Equation.Term(1,[1])],'>=',[o])            # x1 >=0
eq1o = Equation.Eq([Equation.Term(1,[1])],'>=',[Equation.Term(0.9,[])])
eq1l = Equation.Eq([Equation.Term(1,[1])],'<=',[l])            # x1 <=1
eq6o = Equation.Eq([Equation.Term(1,[6])],'>=',[o])            # x6 >=0
eq6l = Equation.Eq([Equation.Term(1,[6])],'<=',[l])            # x6 <=1
eq4o = Equation.Eq([Equation.Term(1,[4])],'>=',[o])            # x4 >=0
eq4l = Equation.Eq([Equation.Term(1,[4])],'<=',[l])            # x4 <=1

##print 'EQ1: ' + eq1.show()
##print 'EQ2: ' +eq2.show()
##print 'EQ3: ' + eq3.show()

E= [eq1,eq2,eq3,eq4,eq1l,eq2l,eq3l,eq4l,eq6l,eq1o,eq2o,eq4o,eq6o]
##print validVar(3,eq2)
#eliminateS(3,E)

##print 'Result :' + E[2].show()
#Equation.simplify(E[0])

##print 'Input sets of Equations \n'+''.join([t.show()+'\n' for t in E])

##print '\n'.join(str(t) for t in Equation.permutations(range(3)))

#ret = Equation.seperate(eq1,6)
##print ret.show()
##print eq1.show()
##print validVar(6,eq2)
#eliminateA(6,E)

print 'Before\n'+''.join([t.show()+'\n' for t in E])

L = [6,4,3,2,1]
'''
#eliminateA(6,E)
##print 'Finanly\n'+' '.join([t.show()+'\n ' for t in E])
#eliminateA(4,E)
#eli_permutation(E,L)
#E.append(eq3o)
##print 'Finanly\n'+' '.join([t.show()+'\n ' for t in E])

##print 'Solving ' + E[6].show()+ ' : ' + str(solve(E[6]))

##print 'SOLVE : '+str(elemination.solveE(E[-1:]))
'''
n = Equation.Eq([Equation.Term(1,[1]),o],'<=',[Equation.Term(0.7,[])])
#print n.show()

E =[n,eq1l]
#print 'Finanly\n'+''.join([t.show()+'\n' for t in E])

m0 = Equation.seperate(n,1)
m1 = Equation.seperate(eq1l,1)
#print m0.show()
#print m1.show()

m2 = Equation.equateR(m0.rN,m0.rD,m1.rN,m1.rD,'<=')
Equation.simplify(m2)


#print m2.show()

#print str(elemination.solve(m2))


e1 = Equation.Eq([Equation.Term(1,[1,3]),Equation.Term(1,[2])],'>=',[Equation.Term(1,[])])
e2 = Equation.Eq([Equation.Term(1,[1])],'>=',[Equation.Term(0.5,[]),o])
e3 = Equation.Eq([Equation.Term(1,[2])],'>=',[Equation.Term(0.75,[]),o])
e4 = Equation.Eq([Equation.Term(1,[3])],'>=',[Equation.Term(0.5,[]),o])

E =[e1,e2,e3,e4]
'''


#print eli_permutation(E,L)
