
class Student:
    

    def __init__ ( self, name, macID ):
        ''' Constructors, initializes with name,student number,and gives everyone a blank sleet of attendance marks'''       

        self.name = name
        self.macID = macID
        self.AttMarkTot = 0
        self.AttMark= [0]*12
##        self.AttMark[0] = 1 #giving everyone 1 mark ,for week 01
        self.sessionData = {}
        self.TutSect = ""
        self.LabSect = ""
        self.LecSect = ""

    def getName(self):
        return self.name

    def getMacID(self):
        return self.macID
    def getTotal(self):

        accum = 0
        for mark in self.AttMark:
            accum += mark

        self.AttMarkTot = accum
        
        return self.AttMarkTot

    def getSingleAttMark(self, session):

        index = getSessionIndex(session)
##        print "Att mark",self.AttMark

        return self.AttMark[index]
    def getAttMark(self):
        return self.AttMark

    
    def getTutSect(self):
        return self.TutSect
    def getLabSect(self):
        return self.LabSect
    def getLecSect(self):
        return self.LecSect

    def setTutSec(self, sect):
        self.TutSect = sect
        
    def setLabSec(self, sect):
        self.LabSect = sect
        
    def setLecSec(self, sect):
        self.LecSect = sect

    
    def setAttMark(self, session , mark ,exceed=False,maxMark = 1):

        index = getSessionIndex(session)

        if not exceed :
            if self.AttMark[index] <= maxMark and mark <= maxMark:
                self.AttMark[index] = int(mark)
                #check if I should do += instead.
                
        else:
            
            if self.AttMark[index] <= maxMark and mark <= maxMark:
                self.AttMark[index] = int(mark)
        

        

def getSessionIndex(session):#format of session must be a Session object ( session.month and session.date )
    mondays = [(1, 2), (1, 9), (1, 16), (1, 23), (1, 30), (2, 6), (2, 13),(2, 27), (3, 5), (3, 12), (3, 19), (3, 26)]   # for now hardcoded the start day of all
                                                                                                                        #our sessions.

##    print session.month,session.date
    for i in range(len(mondays)):
        month = mondays[i][0]
        if session.month ==  month:  # filters month
            date = mondays[i][1]


            if month == 2 and session.date < 6:
                rangeDate = [30,31,1,2,3,4,5]
            elif month == 3 and session.date < 5:
                rangeDate = [27,28,29,1,2,3,4]
                    
            else:
                    
                rangeDate = range(date,date+7)  #decides if date is within this range/session
##              print "range",rangeDate
            for day in rangeDate:
                if session.date == day:
                    return i
    return None
           
        	
class Session:

    def __init__ (self, month ,date):

        self.month = int(month)
        self.date = int(date)




##
##mondays = ['1_2', '1_9', '1_16', '1_23', '1_30', '2_6', '2_13', '2_20', '2_27', '3_5', '3_12', '3_19', '3_26']
##
##lst = []
##
##for i in mondays:
##    month,date = i.split('_')
##    lst.append( Session(month,date) )
##
##
##s1 = Student("sari",555)

        
