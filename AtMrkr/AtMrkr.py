
from stInfo import *
import glob
import re
import time
''' skeleton

Info =  Data.getSessionInfo(session)

lstAttendance = Info['macID']

'''


''' skeleton2


lstAttendance = Info['macID']

'''

def findNames():
    lst = glob.glob('./*.csv')
    
    fileList = []

    for j in lst:
        if re.match('.*(upload|Upload|UPLOAD).*',j):
            fileList.append(j)

    return fileList


def creatStudent(line,headerData):



    student = Student('Derp',line[0]) #make student object with macID info


    for i in range(len(line)):      #goes through each element in that line
        
        temp = headerData[i].split('_')
        if len(temp)==3 and temp[2][:2] == '12':        #checks if the current element is an attendance mark data,and figures out from which tutorial(session)
            session = Session(int(temp[0]),int(temp[1]))
            
            if line[i] != ' ' and line[i] != '' :
                mark = int(line[i])
                student.setAttMark(session,mark)
            

    return student





    
def updateStudent(line,headerData,student):


    
    for i in range(len(line)):      #goes through each element in that line
        
        temp = headerData[i].split('_')
        if len(temp)==3 and temp[2][:2] == '12':        #checks if the current element is an attendance mark data,and figures out from which tutorial(session)
            session = Session(int(temp[0]),int(temp[1]))


            
            if line[i] != ' ' and line[i] != '' :
                mark = int(line[i])
                student.setAttMark(session,mark)
                

            
##    return student
def updateSections(classList):

    fileName = "SectionData.csv"

    infile = open ( fileName, 'r')
    header = infile.readline().split(',')
    data = infile.read().split('\n')
    infile.close()

    data.pop(-1)
    idIndex = 0
    TutIndex = 0
    LabIndex = 0
    LecIndex = 0

    for i in range(len(header)):

        if header[i].find("Username") == 0:
            idIndex = i
        elif header[i].find("Tut") == 0:
            TutIndex = i
        elif header[i].find("Lab") == 0:
            LabIndex = i
        elif header[i].find("Lec") == 0:
            LecIndex = i
    
    
    for line in data:
        eachline = line.split(',')
        student = classList[eachline[idIndex]]
        student.setTutSec(eachline[TutIndex])
        student.setLabSec(eachline[LabIndex])
        student.setLecSec(eachline[LecIndex])

    return classList
        
    
def rawData():

    fileList = findNames()
    classList = {}                  # will have EVERYTHINHG about students,with macID keys
    
    for filename in fileList:   #goes through ALL csv files one by one and builds up classList


        
        infile = open(filename, 'r')
        bigMess = infile.read().split('\n')  # has all data from csv file
        infile.close()

        headerData = bigMess[0].split(',')  #header data into a list

        for longLine in bigMess[1:]:
            line = longLine.split(',')

##            ''' testing purposes '''
##            if line[0] == '#schwem':
##                print line
##            ''' end testing '''
            if classList.has_key(line[0]):
                updateStudent(line,headerData,classList[line[0]])

            else:
                classList[line[0]] = creatStudent(line,headerData)

##            '''extra part to fix the overlapping session data'''
##            if re.match('.*(leo|Leo|LEO).*',filename):
##                print filename
##                maxMark = 2
##                sessionEx = Session(3,12)
##
##                for i in range(len(line)):      #goes through each element in that line
##
##                    temp = headerData[i].split('_')
##                    if len(temp)==3 and temp[2][:2] == '12':        #checks if the current element is an attendance mark data,and figures out from which tutorial(session)
##                        session = Session(int(temp[0]),int(temp[1]))
##
##                        if line[i] != ' ' and line[i] != '' and session.date == sessionEx.date:
##                            mark = int(line[i])
##                            classList[line[0]].setAttMark(sessionEx,mark,True,maxMark)
##            ''' SO INEFFECIENT! '''
            

    classtList = updateSections(classList)

                
                    
    generateAvenueCSV(classList)
    return classList


def findStudentsWithAttMark(classList,attMarkList):
    lst = []
    for key in classList.keys():
        if classList[key].getAttMark() == attMarkList:
            lst.append(classList[key])
    return lst

def findStudentsWithTotal(classList, total ):

    lst = []
    for key in classList.keys():
        if classList[key].getTotal() == total:
            lst.append(classList[key])
    return lst

    
def findStudentsWithMarkOnSession(classList,session,mark):

    lst = []
    for key in classList.keys():
        if classList[key].getSingleAttMark(session) == mark:
            lst.append(classList[key])
    return lst

def generateAvenueCSV(classList):

    
    fileName2 = "Total_Attendance_"+ str(time.time())+".csv"

    fileName = "SpreadSheet_Attendance.csv"

    outfile = open(fileName,'w')
    
    header = "\xef\xbb\xbfUsername,Tut Section,Lab Section,Lec Section, Tut00 , Tut01,Tut02,Tut03,Tut04,Tut05,Tut06,Tut07,Tut08,Tut09,Tut10,Tut11,Tutorial Attendance Points Grade <Numeric MaxPoints:11>,End-of-Line Indicator"

    
    
    
    outfile.write(header+'\n')

    
    for key in classList:                  

                spreadData = str(key)+','+classList[key].getTutSect() +','+classList[key].getLabSect() +','+classList[key].getLecSect() + ','
                marks = ''
                for mark in classList[key].getAttMark():
                    marks += str(mark)+','

                marks += str(classList[key].getTotal())

                spreadData += marks+',#\n'

                outfile.write(spreadData)
                

    outfile.close()
    


    

    

    
##x = rawData()
