import time

def main():
    fileName = raw_input("Enter filename containting Tutorial attendance: ")
    
    classList = generate_classList(fileName)

    manual_edit(classList)
def generate_classList(fileName):
    classList = {}  #where all id and data will be held

    infile = open(fileName,'r')
    data = infile.read().split('\n')
    infile.close()

    
    data.remove(data[0])
    data.remove(data[-1])
    data.remove(data[-1])

    for line in data:
        
        eachline = line.split(',')
        classList[eachline[0][1:]] = int(eachline[1])
        

    return classList

def manual_edit(classList):

    while True:
        iD = raw_input("Enter ID to be edited (all will affect all files,or q to quit): ")
        if iD == 'q' or iD =='Q':
            break

        manualMark = input("Enter marks to be added: ")
        
        if iD =='all' or iD =="ALL":
        
            for key in classList:
                classList[key] +=manualMark
                if classList[key]>7:
                    classList[key] = 7
        else:
            try:
                classList[iD] += manualMark
                if classList[iD]>7:
                    classList[iD] = 7
            except:
                print "meh,ID doesn't exist,try again!"


    make_CSV(classList)

        
    
#Write out Final Data into an Avenue Compatible .csv file
def make_CSV(classList):
    fileName = "Total_tweaked_Attendance_"+ str(time.time())+".csv"

    outfile = open(fileName,'w')
    
    outfile.write('\xef\xbb\xbfUsername,Tutorial Attendance Points Grade <Numeric MaxPoints:11>,End-of-Line Indicator\n')

    for key in classList:                  
                  data = '#'+str(key)+','+str(classList[key])+',#\n'

                  outfile.write(data)

    outfile.close()



if __name__ == "__main__":
    main()
