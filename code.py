data = [['CROUS Duvillard','IUT', ('walk', 5)],['IUT','Gare de Belfort', ('BUS 3', 10)],
        ['Gare de Belfort','Gare de Montbeliard', ('TER', 15)],
        ['Gare de Montbeliard','Campus', ('BUS T1', 15)]]
       # ['Campus','UFR STGI Building C', ('Walk', 3)]
        #['UFR STGI Building C','C01', ('Walk', 1)]] 
       # ['C01','C02', ('Walk', 1)],['Gare de Belfort','Gare de Montbeliard', ('Bus X', 20)]]
place = {'CROUS Duvillard':0,
         'IUT': 1, 
         'Gare de Belfort':2 , 
         'Gare de Montbeliard':3 , 
         'Campus':4 
         #'UFR STGI Building C':5,
         #'C01':6
         #'C02':7      
        }
def build_MatrixOD(place, data):
    mxod=[]
    for i in range(len(place)):
        array = [0 for i in range(len(place))] 
        mxod.append(array)
    for i in data:
        origin=place[i[0]]
        dest=place[i[1]]
        if ( mxod[origin][dest] == 0):
            mxod[origin][dest]=i[2]
            mxod[dest][origin]=i[2]
        elif(mxod[origin][dest][1] > i[2][1]):
            mxod[origin][dest]=i[2]
            mxod[dest][origin]=i[2]
    
    return mxod
matOD=build_MatrixOD(place, data)
def get_key(val):
    for key, value in place.items():
        if val == value:
            return key
    return "None"
def check_complete(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i!=j and mat[i][j]==0 :
                print("False")
                return False
    print("True")

    return True
def Make_transitive(mat, place):
    if check_complete(mat):
        return mat
    else :
        save=[]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]!=0 and i != j:
                    for k in range(len(mat)):
                        if mat[j][k]!=0 and j != k and i != k:
                            station= get_key(j)
                            dist= mat[i][j][1]+mat[j][k][1]
                            save.append([i,k,(mat[j][k][0],dist)])
        for j in range(len(save)):
            i=save[j][0]
            k=save[j][1]
            if(mat[i][k]==0):
                mat[i][k]=(save[j][2])
                mat[i][k]=(save[j][2])
        Make_transitive(mat, place)
    
mat = Make_transitive(matOD, place)
mat