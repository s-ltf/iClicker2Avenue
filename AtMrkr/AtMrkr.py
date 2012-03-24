
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

    
    fileName = "Total_Attendance_"+ str(time.time())+".csv"

    outfile = open(fileName,'w')
    
    outfile.write('\xef\xbb\xbfUsername,Tutorial Attendance Points Grade <Numeric MaxPoints:11>,End-of-Line Indicator\n')

    for key in classList:                  
                  data = str(key)+','+str(classList[key].getTotal())+',#\n'

                  outfile.write(data)

    outfile.close()
