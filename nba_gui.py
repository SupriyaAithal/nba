# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
import numpy as np

ua = [[0,0,0],[0,0,0],[0,0,0]]
ub = [[0,0,0],[0,0,0],[0,0,0]]
uc = [[0,0,0],[0,0,0],[0,0,0]]
pa = [[0,0,0],[0,0,0]]
pb = [[0,0,0],[0,0,0]]
Ea = [[0,0,0],[0,0,0],[0,0,0]]
Eb = [[0,0,0],[0,0,0],[0,0,0]]
Ec = [[0,0,0],[0,0,0],[0,0,0]]
Ed = [[0,0,0],[0,0,0]]
Ee = [[0,0,0],[0,0,0]]
sumua = [0,0,0]
sumub = [0,0,0]
sumuc = [0,0,0]
sumpa = [0,0,0]
sumpb = [0,0,0]
tsum = [0,0,0]
Fac = [0,0,0]
nofac = [0,0,0]
sfr = [0,0,0]
avgsfr = [0,0,0]

A = [[0,0,0],[0,0,0],[0,0,0]]
N = [0,0,0]
avg = [[0,0,0],[0,0,0],[0,0,0]]
fac = [[0,0,0],[0,0,0],[0,0,0]]
sumavg = [0,0,0]
num = [0,0,0]
Rf = [[0,0,0],[0,0,0],[0,0,0]]
sumrf = [0,0,0]
CRM = 0
        
        
        
def func():
    def student_faculty_ratio():
        
        def ufirst():
            try:
                global ua
                for i in range (0,3):
                    for j in range (0,3):
                        ua[i][j] = Ea[i][j].get()
                ua = [list(map(int, i)) for i in ua]
                for k in range(0,3):
                    for l in range(0,3):
                        sumua[k] = sumua[k] + ua[l][k]
                E11d['text'] = sumua[0]
                E12d['text'] = sumua[1]
                E13d['text'] = sumua[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        
        def usecond():
            try:
                global ub
                for i in range (0,3):
                    for j in range (0,3):
                        ub[i][j] = Eb[i][j].get()
                ub = [list(map(int, i)) for i in ub]
                for k in range(0,3):
                    for l in range(0,3):
                        sumub[k] = sumub[k] + ub[l][k]
                E21d['text'] = sumub[0]
                E22d['text'] = sumub[1]
                E23d['text'] = sumub[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def uthird():
            try:
                global uc
                for i in range (0,3):
                    for j in range (0,3):
                        uc[i][j] = Ec[i][j].get()
                uc = [list(map(int, i)) for i in uc]
                for k in range(0,3):
                    for l in range(0,3):
                        sumuc[k] = sumuc[k] + uc[l][k]
                E31d['text'] = sumuc[0]
                E32d['text'] = sumuc[1]
                E33d['text'] = sumuc[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def pfirst():
            try:
                global pa
                for i in range (0,2):
                    for j in range (0,3):
                        pa[i][j] = Ed[i][j].get()
                pa = [list(map(int, i)) for i in pa]
                for k in range(0,3):
                    for l in range(0,2):
                        sumpa[k] = sumpa[k] + pa[l][k]
                E41d['text'] = sumpa[0]
                E42d['text'] = sumpa[1]
                E43d['text'] = sumpa[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def psecond():
            try:
                global pb
                for i in range (0,2):
                    for j in range (0,3):
                        pb[i][j] = Ee[i][j].get()
                pb = [list(map(int, i)) for i in pb]
                for k in range(0,3):
                    for l in range(0,2):
                        sumpb[k] = sumpb[k] + pb[l][k]
                E51d['text'] = sumpb[0]
                E52d['text'] = sumpb[1]
                E53d['text'] = sumpb[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def totalStud():
            try:
                global tsum
                for i in range(0,3):
                    a = sumua[i] + sumub[i] + sumuc[i] + sumpa[i] + sumpb[i]
                    tsum[i] = a
                S0a['text'] = tsum[0]
                S0b['text'] = tsum[1]
                S0c['text'] = tsum[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def sfratio():
            try:
                global nofac
                global tsum
                for i in range(0,3):
                    nofac[i] = Fac[i].get()
                nofac = list(map(int, nofac))
                for i in range(0,3):
                    d = tsum[i]/nofac[i]
                    sfr[i] = round(d,2)
                SF0a['text'] = sfr[0]
                SF0b['text'] = sfr[1]
                SF0c['text'] = sfr[2]
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        def avgsfratio():
            try:
                global sfr
                a = sum(list(map(float,sfr)))
                b = a/3.0
                ASF0a['text'] = round(b,2)
                err1['text'] = ""
            except:
                err1['text'] = "Error occurred"
        
        L0 = Label(branch, text="Student-Faculty Ratio (SFR)").grid(row =0)
        L1 = Label(branch, text="Enter the number of students in UG 2nd Year (u1):").grid(row=1)
        H1 = Label(branch, text="2017-18").grid(row=1, column=1)
        H2 = Label(branch, text="2016-17").grid(row=1, column=2)
        H3 = Label(branch, text="2015-16").grid(row=1, column=3)
        E0a = Label(branch,text="u1.1").grid(row=2,column=0)
        Ea[0][0] = Entry(branch, bd =5)
        Ea[0][1] = Entry(branch, bd =5)
        Ea[0][2] = Entry(branch, bd =5)
        E10b = Label(branch,text="u1.2").grid(row=3,column=0)
        Ea[1][0] = Entry(branch, bd =5)
        Ea[1][1] = Entry(branch, bd =5)
        Ea[1][2] = Entry(branch, bd =5)
        E10 = Label(branch,text="u1.3").grid(row=4,column=0)
        Ea[2][0] = Entry(branch, bd =5)
        Ea[2][1] = Entry(branch, bd =5)
        Ea[2][2] = Entry(branch, bd =5)
        B1 = Button(branch, text ="UG1(u1.1+u1.2+u1.3)(click)", command = ufirst).grid(row=5,column=0)
        E11d = Label(branch, text = "")
        E12d = Label(branch, text = "")
        E13d = Label(branch, text = "")
        Ea[0][0].grid(row=2,column=1)
        Ea[0][1].grid(row=2,column=2)
        Ea[0][2].grid(row=2,column=3)
        Ea[1][0].grid(row=3,column=1)
        Ea[1][1].grid(row=3,column=2)
        Ea[1][2].grid(row=3,column=3)
        Ea[2][0].grid(row=4,column=1)
        Ea[2][1].grid(row=4,column=2)
        Ea[2][2].grid(row=4,column=3)
        E11d.grid(row=5,column=1)
        E12d.grid(row=5,column=2)
        E13d.grid(row=5,column=3)
        
        L2 = Label(branch, text="Enter the number of students in UG 3rd Year (u2):").grid(row=6)
        E20a = Label(branch,text="u2.1").grid(row=7,column=0)
        Eb[0][0] = Entry(branch, bd =5)
        Eb[0][1] = Entry(branch, bd =5)
        Eb[0][2] = Entry(branch, bd =5)
        E20b = Label(branch,text="u2.2").grid(row=8,column=0)
        Eb[1][0] = Entry(branch, bd =5)
        Eb[1][1] = Entry(branch, bd =5)
        Eb[1][2] = Entry(branch, bd =5)
        E20c = Label(branch,text="u2.3").grid(row=9,column=0)
        Eb[2][0] = Entry(branch, bd =5)
        Eb[2][1] = Entry(branch, bd =5)
        Eb[2][2] = Entry(branch, bd =5)
        B2 = Button(branch, text ="UG2(u2.1+u2.2+u2.3)(click)", command = usecond).grid(row=10,column=0)
        E21d = Label(branch, text = "")
        E22d = Label(branch, text = "")
        E23d = Label(branch, text = "")
        Eb[0][0].grid(row=7,column=1)
        Eb[0][1].grid(row=7,column=2)
        Eb[0][2].grid(row=7,column=3)
        Eb[1][0].grid(row=8,column=1)
        Eb[1][1].grid(row=8,column=2)
        Eb[1][2].grid(row=8,column=3)
        Eb[2][0].grid(row=9,column=1)
        Eb[2][1].grid(row=9,column=2)
        Eb[2][2].grid(row=9,column=3)
        E21d.grid(row=10,column=1)
        E22d.grid(row=10,column=2)
        E23d.grid(row=10,column=3)
        
        L3 = Label(branch, text="Enter the number of students in UG 4th Year (u3):").grid(row=11)
        E30a = Label(branch,text="u3.1").grid(row=12,column=0)
        Ec[0][0] = Entry(branch, bd =5)
        Ec[0][1] = Entry(branch, bd =5)
        Ec[0][2] = Entry(branch, bd =5)
        E30b = Label(branch,text="u3.2").grid(row=13,column=0)
        Ec[1][0] = Entry(branch, bd =5)
        Ec[1][1] = Entry(branch, bd =5)
        Ec[1][2] = Entry(branch, bd =5)
        E30c = Label(branch,text="u3.3").grid(row=14,column=0)
        Ec[2][0] = Entry(branch, bd =5)
        Ec[2][1] = Entry(branch, bd =5)
        Ec[2][2] = Entry(branch, bd =5)
        B3 = Button(branch, text ="UG3(u3.1+u3.2+u3.3)(click)", command = uthird).grid(row=15,column=0)
        E31d = Label(branch, text = "")
        E32d = Label(branch, text = "")
        E33d = Label(branch, text = "")
        Ec[0][0].grid(row=12,column=1)
        Ec[0][1].grid(row=12,column=2)
        Ec[0][2].grid(row=12,column=3)
        Ec[1][0].grid(row=13,column=1)
        Ec[1][1].grid(row=13,column=2)
        Ec[1][2].grid(row=13,column=3)
        Ec[2][0].grid(row=14,column=1)
        Ec[2][1].grid(row=14,column=2)
        Ec[2][2].grid(row=14,column=3)
        E31d.grid(row=15,column=1)
        E32d.grid(row=15,column=2)
        E33d.grid(row=15,column=3)
        
        L4 = Label(branch, text="Enter the number of students in UG 1st Year (p1):").grid(row=16)
        E40a = Label(branch,text="p1.1").grid(row=17,column=0)
        Ed[0][0] = Entry(branch, bd =5)
        Ed[0][1] = Entry(branch, bd =5)
        Ed[0][2] = Entry(branch, bd =5)
        E40b = Label(branch,text="p1.2").grid(row=18,column=0)
        Ed[1][0] = Entry(branch, bd =5)
        Ed[1][1] = Entry(branch, bd =5)
        Ed[1][2] = Entry(branch, bd =5)
        B4 = Button(branch, text ="PG1(p1.1+p1.2)(click)", command = pfirst).grid(row=19,column=0)
        E41d = Label(branch, text = "")
        E42d = Label(branch, text = "")
        E43d = Label(branch, text = "")
        Ed[0][0].grid(row=17,column=1)
        Ed[0][1].grid(row=17,column=2)
        Ed[0][2].grid(row=17,column=3)
        Ed[1][0].grid(row=18,column=1)
        Ed[1][1].grid(row=18,column=2)
        Ed[1][2].grid(row=18,column=3)
        E41d.grid(row=19,column=1)
        E42d.grid(row=19,column=2)
        E43d.grid(row=19,column=3)
        
        L5 = Label(branch, text="Enter the number of students in UG 2nd Year (p2):").grid(row=20)
        E50a = Label(branch,text="p2.1").grid(row=21,column=0)
        Ee[0][0] = Entry(branch, bd =5)
        Ee[0][1] = Entry(branch, bd =5)
        Ee[0][2] = Entry(branch, bd =5)
        E50b = Label(branch,text="p1.2").grid(row=22,column=0)
        Ee[1][0] = Entry(branch, bd =5)
        Ee[1][1] = Entry(branch, bd =5)
        Ee[1][2] = Entry(branch, bd =5)
        B5 = Button(branch, text ="PG1(p1.1+p1.2)(click)", command = psecond).grid(row=23,column=0)
        E51d = Label(branch, text = "")
        E52d = Label(branch, text = "")
        E53d = Label(branch, text = "")
        Ee[0][0].grid(row=21,column=1)
        Ee[0][1].grid(row=21,column=2)
        Ee[0][2].grid(row=21,column=3)
        Ee[1][0].grid(row=22,column=1)
        Ee[1][1].grid(row=22,column=2)
        Ee[1][2].grid(row=22,column=3)
        E51d.grid(row=23,column=1)
        E52d.grid(row=23,column=2)
        E53d.grid(row=23,column=3)
        
        S0 = Button(branch, text="Total number of students in the department(click)", command = totalStud).grid(row=24)
        S0a = Label(branch, text = "")
        S0b = Label(branch, text = "")
        S0c = Label(branch, text = "")
        S0a.grid(row=24,column=1)
        S0b.grid(row=24,column=2)
        S0c.grid(row=24,column=3)
        
        F0 = Label(branch, text="Number of Faculty in the department").grid(row=25)
        Fac[0]= Entry(branch, bd =5)
        Fac[1] = Entry(branch, bd =5)
        Fac[2] = Entry(branch, bd =5)
        Fac[0].grid(row=25,column=1)
        Fac[1].grid(row=25,column=2)
        Fac[2].grid(row=25,column=3)
        
        SF0 = Button(branch, text="Student Faculty Ratio(click)", command = sfratio).grid(row=26)
        SF0a = Label(branch, text = "")
        SF0b = Label(branch, text = "")
        SF0c = Label(branch, text = "")
        SF0a.grid(row=26,column=1)
        SF0b.grid(row=26,column=2)
        SF0c.grid(row=26,column=3)
        
        ASF0 = Button(branch, text="Average Student Faculty Ratio(click)", command = avgsfratio).grid(row=29)
        ASF0a = Label(branch, text = "")
        ASF0a.grid(row=29,column=2)
        Button(branch, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=29,column=12)
        err1= Label(branch, text="")
        err1.grid(row =40,column=2)
    
    def faculty_cadre_proportion():
        def numcal():
            try:
                global num
                for i in range(0,3):
                    num[i] = N[i].get()
                num = list(map(int, num))
                err2['text'] = ""
            except:
                err2['text'] = "Error occurred"
        
        def requiredF():
            try:
                global num
                global Rf
                Rf = [list(map(float, i)) for i in avg]
                for i in range(0,3):
                    for j in range(0,3):
                        if(j==0):
                            Rf[i][j] = round((1/9),2)*(num[i]/15)
                        elif(j==1):
                            Rf[i][j] = round((2/9),2)*(num[i]/15)
                        else:
                            Rf[i][j] = round((6/9),2)*(num[i]/15)
                for i in range(0,3):
                    for j in range(0,3):
                        Rf[i][j] = round(Rf[i][j],2)
                for k in range(0,3):
                    for l in range(0,3):
                        sumrf[k] = sumrf[k] + Rf[l][k]
                    sumrf[k] = sumrf[k]/3
                for i in range(0,3):
                    sumrf[i] = round(sumrf[i],2)
                F1['text'] = Rf[0][0]
                F2['text'] = Rf[0][1]
                F3['text'] = Rf[0][2]
                F4['text'] = Rf[1][0]
                F5['text'] = Rf[1][1]
                F6['text'] = Rf[1][2]
                F7['text'] = Rf[2][0]
                F8['text'] = Rf[2][1]
                F9['text'] = Rf[2][2]
                Fr1['text'] = sumrf[0]
                Fr2['text'] = sumrf[1]
                Fr3['text'] = sumrf[2]
                err2['text'] = ""
            except:
                err2['text'] = "Error occurred"
        
        def avgno():
            try:
                global avg
                numcal()
                requiredF()
                for i in range (0,3):
                    for j in range (0,3):
                        avg[i][j] = A[i][j].get()
                avg = [list(map(int, i)) for i in avg]
                for k in range(0,3):
                    for l in range(0,3):
                        sumavg[k] = sumavg[k] + avg[l][k]
                    sumavg[k] = sumavg[k]/3
                for i in range(0,3):
                    sumavg[i] = round(sumavg[i],2)
                A1['text'] = sumavg[0]
                A2['text'] = sumavg[1]
                A3['text'] = sumavg[2]
                err2['text'] = ""
            except:
                err2['text'] = "Error occurred"
        
        def cRM():
            try:
                global sumavg
                global sumrf
                CRM = ((sumavg[0]/sumrf[0]) + ((sumavg[1]/sumrf[1])*0.6) + ((sumavg[2]/sumrf[2])*0.4))*12.5
                cmr0['text'] = round(CRM,2)
                err2['text'] = ""
            except:
                err2['text'] = "Error occurred"
        
        
        L0 = Label(branch, text="Faculty Cadre Proportion").grid(row =0)
        L1 = Label(branch, text ="Enter total number of students").grid(row=1)
        La = Label(branch, text ="CAY[17-18]").grid(row=1,column=2)
        Lb = Label(branch, text ="CAYm1[16-17]").grid(row=1,column=4)
        Lc = Label(branch, text ="CAYm2[15-16]").grid(row=1,column=6)
        N[0] = Entry(branch, bd =5)
        N[1] = Entry(branch, bd =5)
        N[2] = Entry(branch, bd =5)
        N[0].grid(row = 2, column = 2)
        N[1].grid(row = 2, column = 4)
        N[2].grid(row = 2, column = 6)
        L2 = Label(branch, text="Professors").grid(row =3, column =2)
        L3 = Label(branch, text="Associate Professors").grid(row =3, column =4)
        L4 = Label(branch, text="Assistant Professors").grid(row =3, column =6)
        L5 = Label(branch, text="Required F1").grid(row =4, column =2)
        L6 = Label(branch, text="Available").grid(row =4, column =3)
        L7 = Label(branch, text="Required F2").grid(row =4, column =4)
        L8 = Label(branch, text="Available").grid(row =4, column =5)
        L9 = Label(branch, text="Required F3").grid(row =4, column =6)
        L10 = Label(branch, text="Available").grid(row =4, column =7)
        L11 = Label(branch, text="Year").grid(row =3)
        L12 = Label(branch, text="CAY[17-18]").grid(row =5)
        L13 = Label(branch, text="CAYm1[16-17]").grid(row =6)
        L14 = Label(branch, text="CAYm2[15-16]").grid(row =7)
        
        A[0][0] = Entry(branch, bd =5)
        A[0][1] = Entry(branch, bd =5)
        A[0][2] = Entry(branch, bd =5)
        A[1][0] = Entry(branch, bd =5)
        A[1][1] = Entry(branch, bd =5)
        A[1][2] = Entry(branch, bd =5)
        A[2][0] = Entry(branch, bd =5)
        A[2][1] = Entry(branch, bd =5)
        A[2][2] = Entry(branch, bd =5)
        A[0][0].grid(row=5,column=3)
        A[0][1].grid(row=5,column=5)
        A[0][2].grid(row=5,column=7)
        A[1][0].grid(row=6,column=3)
        A[1][1].grid(row=6,column=5)
        A[1][2].grid(row=6,column=7)
        A[2][0].grid(row=7,column=3)
        A[2][1].grid(row=7,column=5)
        A[2][2].grid(row=7,column=7)
        A1 = Label(branch, text = "")
        A2 = Label(branch, text = "")
        A3 = Label(branch, text = "")
        A1.grid(row=8,column=3)
        A2.grid(row=8,column=5)
        A3.grid(row=8,column=7)
        
        F1 = Label(branch, text = "")
        F2 = Label(branch, text = "")
        F3 = Label(branch, text = "")
        F4 = Label(branch, text = "")
        F5 = Label(branch, text = "")
        F6 = Label(branch, text = "")
        F7 = Label(branch, text = "")
        F8 = Label(branch, text = "")
        F9 = Label(branch, text = "")
        Fr1 = Label(branch, text = "")
        Fr2 = Label(branch, text = "")
        Fr3 = Label(branch, text = "")
        F1.grid(row=5,column=2)
        F2.grid(row=5,column=4)
        F3.grid(row=5,column=6)
        F4.grid(row=6,column=2)
        F5.grid(row=6,column=4)
        F6.grid(row=6,column=6)
        F7.grid(row=7,column=2)
        F8.grid(row=7,column=4)
        F9.grid(row=7,column=6)
        Fr1.grid(row=8,column=2)
        Fr2.grid(row=8,column=4)
        Fr3.grid(row=8,column=6)
        
        B1 = Button(branch, text ="Average number(click)", command = avgno).grid(row=8,column=0)
        B2 = Button(branch, text ="Cadre Ratio Marks(click)", command = cRM).grid(row=9,column=0)
        cmr0 = Label(branch, text ="")
        cmr0.grid(row=9, column=2)  
        Button(branch, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=30,column=12)
        err2= Label(branch, text="")
        err2.grid(row=40,column=4)
        
    def fac_qual():
        #import numpy as np
        x=[0,0,0]
        y=[0,0,0]
        f=[0,0,0]
        
        xx=[0,0,0]
        yy=[0,0,0]
        ff=[0,0,0]
        
        fq=[0,0,0]
        
        def fq_calc():
            try:
                for i in range(0,3):
                    xx[i] = x[i].get()
                    yy[i] = y[i].get()
                    ff[i] = f[i].get()
                	
                num1 = list(map(int, xx))
                num2 = list(map(int, yy))
                num3 = list(map(int, ff))
                
                for i in range (0,3):
                    fq[i]=2.5*(((10*num1[i])+(4*num2[i]))/num3[i])
                	
                fq1['text']=fq[0]
                fq2['text']=fq[1]
                fq3['text']=fq[2]
                err3['text'] = ""
            except:
                err3['text'] = "Error occurred"  
        
        def fq_avg():
            try:
                afq['text']=np.mean(fq)
                err3['text'] = ""
            except:
                err3['text'] = "Error occurred"
        
        var = StringVar()
        l1 = Label( branch, text="Years")
        l1.grid(row=1,column=1)
        l2 = Label( branch, text="CAY[17-18]")
        l2.grid(row=2,column=1)
        l3 = Label( branch, text="CAY[16-17]")
        l3.grid(row=3,column=1)
        l4 = Label( branch, text="CAY[15-16]")
        l4.grid(row=4,column=1)
        l5 = Label( branch, text="X")
        l5.grid(row=1,column=2)
        l6 = Label( branch, text="Y")
        l6.grid(row=1,column=3)
        l7 = Label( branch, text="F")
        l7.grid(row=1,column=4)
        l8 = Label( branch, text="FQ" )
        l8.grid(row=1,column=5)
        
        #no. of regular faculty with Ph.D
        x[0] = Entry(branch, bd =5)
        x[0].grid(row=2,column=2)
        x[1] = Entry(branch, bd =5)
        x[1].grid(row=3,column=2)
        x[2] = Entry(branch, bd =5)
        x[2].grid(row=4,column=2)
        
        #no. of regular faculty with M.Tech.
        y[0] = Entry(branch, bd =5)
        y[0].grid(row=2,column=3)
        y[1]= Entry(branch, bd =5)
        y[1].grid(row=3,column=3)
        y[2]= Entry(branch, bd =5)
        y[2].grid(row=4,column=3)
        
        #no. of regular faculty required to comply 1:15 Faculty Student ratio
        f[0] = Entry(branch, bd =5)
        f[0].grid(row=2,column=4)
        f[1] = Entry(branch, bd =5)
        f[1].grid(row=3,column=4)
        f[2] = Entry(branch, bd =5)
        f[2].grid(row=4,column=4)
        
        #Faculty Qualification
        fq1 = Label( branch, text="" )
        fq1.grid(row=2,column=5)
        fq2 = Label( branch, text="" )
        fq2.grid(row=3,column=5)
        fq3 = Label( branch, text="")
        fq3.grid(row=4,column=5)
        
        #Average FQ
        afq = Label( branch, text="" )
        afq.grid(row=6,column=2)
        
        
        B1 = Button(branch, text ="Generate FQ", command = fq_calc).grid(row=5,column=1)
        B2 = Button(branch, text ="Average Assessment", command = fq_avg).grid(row=6,column=1)
        
        Button(branch, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=30,column=12)
        err3= Label(branch, text="")
        err3.grid(row=40,column=3)


    val=v.get()
    if (val!=0):    
        branch=Toplevel()
        branch.geometry('1920x1080')
        #branch.attributes('-zoomed', True)
        
        if(val==1):
            student_faculty_ratio()
        
        if(val==2):
            faculty_cadre_proportion()
            
        if(val==3):
            fac_qual()
            
        

root=Tk()
root.geometry('1920x1080')
#root.attributes('-fullscreen', True)

v=IntVar()
Radiobutton(root,text="Student Faculty ratio",variable=v,value=1,font=('Garamond',16)).place(x=20,y=160)
Radiobutton(root,text="Faculty Cadre proportion",variable=v,value=2,font=('Garamond',16)).place(x=20,y=210)
Radiobutton(root,text="Faculty qual",variable=v,value=3,font=('Garamond',16)).place(x=20,y=260)
Button(root, text="Next", command=func,font=('Times',16)).place(x=300,y=650)
Button(root, text="Exit", command=root.destroy,font=('Times',16)).place(x=400,y=650)


root.mainloop()
