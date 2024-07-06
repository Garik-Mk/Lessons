
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import WORD


dateBasic = pd.read_csv("db/data.csv")
dateBasic.set_index("Unnamed: 0",inplace= True)

# Training sample
answer1 = pd.read_csv("db/answe[0-2].csv")
answer2 = pd.read_csv("db/answe(2-4].csv")
answer3 = pd.read_csv("db/answe(4-5].csv")
answer1.set_index("Unnamed: 0",inplace=True)
answer2.set_index("Unnamed: 0",inplace=True)
answer3.set_index("Unnamed: 0",inplace=True)

answerNp1 = np.array([])
for i in answer1.index: 
    answerNp1 = np.append( answerNp1 , answer1.loc[[i]] )
answerNp1= answerNp1.reshape(17,8)

answerNp2= np.array([])
for i in answer2.index: 
    answerNp2 = np.append( answerNp2 , answer2.loc[[i]] )
answerNp2= answerNp2.reshape(17,8)

answerNp3 = np.array([])
for i in answer3.index: 
    answerNp3 = np.append( answerNp3 , answer3.loc[[i]] )
answerNp3= answerNp3.reshape(17,8)

# conuntries vars (for function countriTop )
erkir1 = ""
erkir2 = ""
whoseT = ""

popTar = [0,0,0,0,0,0,0,0]
supFlag = ""


support1 = []
support2 = []
year = 2024

# collect informathion about countries (who is powerful country,who controls the therritory)
def countriTop(country1,country2,whoseT1):
    global erkir1
    global erkir2 
    global whoseT

    # who controls the therritory

    whoseT = whoseT1.get()

    # who is powerful country

    # get countries  
    country1 = country1.get()
    country2 = country2.get()
    # form data get power parameters 
    countryList1 = dateBasic.loc[[f"{country1}"] ,["armyPower" , "mostPowerful" , "economyGPD"]]
    countryList2 = dateBasic.loc[ [ f"{country2}"] , ["armyPower" , "mostPowerful" , "economyGPD"]]
    # make np arrays with power parameters 
    countryList1 = countryList1.to_numpy()
    countryList2 = countryList2.to_numpy()

    # decide who is powerful
    countryList1 = np.sum(countryList1>countryList2)
    if( countryList1 > 1):
        erkir1 = country1
        erkir2 = country2
    else:
        erkir1 = country2
        erkir2 = country1

    # work with GUI

    # corect next display parameters
    labelSup1["text"] = f"Who support {erkir1}"
    labelSup2["text"] = f"Who support {erkir2}"
    # show next display
    labelYear.grid(pady=(15,0)) 
    

# collect information about supporters (if there are supporters make list ,  and get year)  
def makeList(year1,supList1, supList2):
    global support1 
    global support2
    global year 

    # get year
    year = 2024
    year = int(year1.get())

    # if there are supporters make list
    support1 = []
    support2 = []
    for i in supList1:
       i = i.get()
       if(i != "" ):
           support1.append(i)
    for i in supList2:
       i = i.get()
       if(i != "" ):
           support2.append(i)  

    # work with GUI
    # show next display
    outBtn3.grid( pady=(10,3))


# from received data prepare object
def mainFunc(erkir1 , erkir2 , support1,support2, year):
    # create Numpy array for featers 
    # for countries
    pop1 = dateBasic.loc [ [f"{erkir1}"]]
    pop2 = dateBasic.loc[[f"{erkir2}"]]
    pop1 = pop1.to_numpy()
    pop2 = pop2.to_numpy()

    # for supporters
    popSup1 = np.array([])
    for i in range(len(support1)):
        popS1 = dateBasic.loc[ [f"{support1[i]}"] ]
        popS1 = popS1.to_numpy()
        popSup1 = np.append(popSup1 , popS1[0])

    popSup1 = popSup1.reshape(int(len(popSup1)/7) , 7  )

    popSup2 = np.array([])
    for i in range(len(support2)):
        popS2 = dateBasic.loc[ [f"{support2[i]}"] ]
        popS2 = popS2.to_numpy()
        popSup2 = np.append(popSup2 , popS2[0])

    popSup2 = popSup2.reshape(int(len(popSup2)/7) , 7  )


    # coefficient support power 
    ksupPow1 = []
    for i in range( len(popSup1)) :
        k1 = (1 - abs(pop1[0][4] - popSup1[i][4]))/4   + (1 - abs(pop1[0][5] - popSup1[i][5]))*2/3 + (1 - abs(pop1[0][6] - popSup1[i][6]))/12
        ksupPow1.append(k1)

    ksupPow2 = [] 
    for i in range( len(popSup2)) :
        k1 = (1 - abs(pop2[0][4] - popSup2[i][4]))/4   + (1 - abs(pop2[0][5] - popSup2[i][5]))*2/3 + (1 - abs(pop2[0][6] - popSup2[i][6]))/12
        ksupPow2.append(k1)


    # year dividers for coefficient support power (Russia vs Ukrain war)
    divider1 = [4,4,4]
    divider2 = [4,4,4]

    def changeQuan( changing , supList, dividerN,changeNum  ):
        if(changing in supList):
            dividerN[supList.index(changing)] = changeNum

    if(year >= 2022):   
        changeQuan("russia",support1,divider1, 8)
        changeQuan( "unitedstates" ,support1, divider1 , 2)
        changeQuan("russia", support2,divider2,8)
        changeQuan( "unitedstates",support2, divider2 ,2)
    
    # add support feater in pop(featers array)
    def addFeaterPop(popSupN , ksupPowN , dividerN , popN):
        k2 = 0
        for i in range(len(popSupN)):
            k2 +=  (popSupN[i][0] + popSupN[i][1]+ popSupN[i][2]) *ksupPowN[i]/(3 * dividerN[i])
        return np.append(popN,k2)

    pop1 = addFeaterPop(popSup1,ksupPow1,divider1,pop1)
    pop2 = addFeaterPop(popSup2,ksupPow2,divider2,pop2)


    global supFlag 

    if(whoseT == erkir1):
        supFlag = erkir1
    elif(whoseT == erkir2):
        supFlag= erkir2

    
    # outBtn3.grid(pady=(1000,3))
    # labelYear.grid(pady=(1500,0) )

    global popTar
    popTar = pop1-pop2
    outBtn4.grid(pady=(10,0))


# get answer for object and output 
def outPut(popTar,answerNp1 ,answerNp2,answerNp3):
    getTask = popTar
    s1 = 0
    for i in answerNp1:
        s1 += abs(getTask- i)
    s2 = 0
    for i in answerNp2:
        s2 += abs(getTask- i)
    s3 = 0
    for i in answerNp3:
        s3 += abs(getTask- i)

    s1 = s1/17
    s2 = s2/17
    s3 = s3/17

    s1 = s1*[4,3,3,1,1,1,0.1,7]
    s2 = s2*[4,3,3,1,1,1,0.1,7]
    s3 = s3*[4,3,3,1,1,1,0.1,7]

    a1 = sum(s1)
    a2 = sum(s2)
    a3 = sum(s3)
    
    global erkir1
    global erkir2 
    global support1
    global support2
    erkir1 = erkir1.strip()
    erkir2 = erkir2.strip()
    banakcox = f"{erkir1}"
    chbanakcox = f"{erkir2}"
    if(popTar[1] < 0):
        banakcox = f"{erkir2}"
        chbanakcox = f"{erkir1}"
    ajakcGum1 =""
    ajakcGum2 =""
    
    supArt2 = ""
    supArt21 = ""
    if(len(support1) != 0 ):
        ajakcGum1 ="և նրա աջակիցների գումարային"

    if(len(support2) != 0 ):
        ajakcGum2 ="և նրա աջակիցների գումարային"
        if(len(support2)==1):
            supArt2 = f"{support2[0]} -ի աջակցությամբ"  
            supArt21 = f" և {support2[0]}- ի"  
        elif(len(support2)==2):
            supArt2 = f"{support2[0]} -ի,{support2[1]} -ի աջակցությամբ" 
            supArt21 = f" և {support2[0]}- ի,{support2[1]}- ի" 
        else:
            supArt2 = f"{support2[0]} -ի,{support2[1]} -ի, {support2[2]} -ի աջակցությամբ" 
            supArt21 = f" և {support2[0]}- ի,{support2[1]}- ի,{support2[2]} -ի" 
    gravPah= "գրավելու"
    gravPah1 = "գրավումը"
    if(supFlag == erkir1):
        gravPah = "պահպանելու"  
        gravPah1 = "պահպանումը"


    answer1 = f"""
    {erkir1} -ի {ajakcGum1} հզորությունը մոտավոր հավասար է 

    {erkir2} -ի {ajakcGum2}  հզորությանը տվյալ իրավիճակում։

    խնդիրը լուծվելու է դիվանագիտական ճանապարհով։
    Քանի որ խնդիրը լուծվելու է դիվանագիտական ճանապարհով խնդրի լուծումը կախված
    է մի շարք գործոններից բայց հիմնական գործոնը դա {erkir1} -ի և {erkir2} -ի
    դիվանագիտական հզորությունն է:

    Ամենայն հավանականությամբ  խնդիրը լուծվելու է {banakcox} -ի օգտին քանի որ {banakcox} -ի
    դիվանագիտական հզորությունը ավելի մեծ է քան {chbanakcox} - ի դիվանագիտական հզորությունը։
    """ 
    answer2 = f"""
    {erkir1} ը/ն {gravPah}  է կոնֆլիկտային տարածքը քանի որ {erkir1} -ի 
    {ajakcGum1} հզորությունը մեծ է  
    {erkir2} -ի {ajakcGum2} հզորությունից տվյալ իրավիճակում։

    Բայց {erkir2} -ի {supArt21} համար ընդունելի չէ
    տարածքի {gravPah1} {erkir1} -ի կողմից և  {erkir2}  ը/ն
    {supArt2} փորձելու է դիվանագիտական ճանապարհով
    վերադարձնել տարացքը։ 
    (դիվանագիտական քանի որ գումարային հզորությունը թույլ չի տալիս պատերազմել {erkir1} -ի դեմ)

    Չնայած {erkir2} -ի ջանքերի մեծ հավանականությամբ խնդիրը լուծվելու է {erkir1} -ի օգտին քանի
    որ {erkir1} ը/ն շատ ավելի հզոր է քան {erkir2} ը/ն։
    """
    answer3 = f"""
    {erkir1} -ի {ajakcGum1} հզորությունը շատ ավելի մեծ է քան  
    {erkir2} -ի {ajakcGum2} հզորությունը տվյալ իրավիճակում։
    Կամ {erkir1} ը/ն գրավելու է վիճելի տարածքը եվ {erkir2} ը/ն ընդունելու է տարածքի կորուստը 
    քանի որ այն շատ թույլ է։
    Կամ {erkir2} -ը առանց պատերազմ զիճելու է վիճելի տարածքը {erkir1} -ին
    """
    answer =""""""
    if( a1<a2 and a1<a3 ):
        print("answer1")
        answer = answer1
    elif(a2<a1 and a2<a3):
        print("answer2")
        answer = answer2
    else: 
        print("answer3")
        answer = answer3

    textOutput.delete("1.0","end")
    textOutput.insert(0.0,answer)
    labelYear.grid(pady=(1500,0) ) #pd1500
    outBtn3.grid( pady=(1000,3))
    outBtn4.grid( pady=(1000,0))
  




# Tkinter 

win = tk.Tk()

# icon
Photo = tk.PhotoImage(file= 'Photos/icon.png')
win.iconphoto(False,Photo)

win.config(bg= "#d87379")
#d87379
#DDA0DD
win.title("History model")


win.geometry("1000x800+200+100")
win.resizable(False,False)
win.minsize(400,300)
win.maxsize(1000,600)


# get countries info
label1 = tk.Label(win,text= "Enter first county" ,background="#d87379",fg ="#bbdcf0")
label1.grid(row=0,column=0 )
text1 = tk.Entry(win,bg="#e4edf2" ,borderwidth=0 ,fg="#011f4b",highlightthickness=1)
text1.grid(row=1,column=0,padx=(15,0))

label2= tk.Label(win,text= "Enter Second county",background="#d87379",fg ="#bbdcf0")
label2.grid(row=0,column=1)
text2 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
text2.grid(row=1,column=1,padx=(20,0))

labelWhose= tk.Label(win,text= "Enter Who controls the territory",background="#d87379",fg ="#bbdcf0" )
labelWhose.grid(row=2,column=0,columnspan=2)
textWhose = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textWhose.grid(row=3,column=0 ,columnspan=2)

btn1 = tk.Button(win,text="Next" ,fg ="#92d2f9", highlightbackground="#d87379",command= lambda:countriTop(text1,text2,textWhose ) )
btn1.grid(row=4,column=0,columnspan=2 , pady=(10,0))

# get Supporters info
labelYear = tk.Label(win,text=f"Enter year" ,background="#d87379",fg ="#bbdcf0")
textYear = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
labelYear.grid(row =5 ,column=0,pady=(1500,0),columnspan=2 ) #pd1500
textYear.grid(row=6 ,column=0 ,columnspan=2)

labelSup1= tk.Label(win,text= f"Enter countries that support {erkir1}",background="#d87379",fg ="#bbdcf0")
labelSup1.grid(row=7 ,column=0 ,pady=(5,2),columnspan=2)
textSup11 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup11.grid(row=8 ,column=0)
textSup12 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup12.grid(row=8 ,column=1)
textSup13 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup13.grid(row=9 ,column=0, pady=(6,0),columnspan=2)

labelSup2= tk.Label(win,text= f"nter countries that support {erkir2}",background="#d87379",fg ="#bbdcf0")
labelSup2.grid(row=10 ,column=0 ,pady=(5,2),columnspan=2)
textSup21 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup21.grid(row=11 ,column=0)
textSup22 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup22.grid(row=11,column=1)
textSup23 = tk.Entry(win,bg="#e4edf2",borderwidth=0,fg="#011f4b",highlightthickness=1)
textSup23.grid(row=12 ,column=0, pady=(6,0),columnspan=2)

btn2 = tk.Button(text="Next",fg ="#92d2f9", highlightbackground="#d87379" ,command =lambda: makeList(textYear ,[textSup11,textSup12,textSup13] , [textSup21,textSup22,textSup23]) )
btn2.grid(row=13,column=0,columnspan=2,pady=(10,0))

# output answer
outBtn3 = tk.Label(win,text ="Data is ready",background="#d87379",fg ="#bbdcf0")
outBtn3.grid( row=14,column=0, columnspan=2 ,pady=(1000,3)) # pd 1000
btn3 = tk.Button(text="prepare an answer",fg ="#92d2f9", highlightbackground="#d87379",command= lambda: mainFunc(erkir1,erkir2,support1,support2,year) )
btn3.grid( row=15,column=0, columnspan=2)

outBtn4 = tk.Label(win,text ="Answer is ready",background="#d87379",fg ="#bbdcf0")
show = tk.Button(win,text= "Show answer" ,fg ="#92d2f9",highlightbackground="#d87379",command = lambda:outPut(popTar,answerNp1 ,answerNp2,answerNp3) ) 
outBtn4.grid(row=16,column=0,columnspan=3 , pady=(1000,0))
show.grid(row=17,column=0,columnspan=3)

textOutput = tk.Text(win,wrap = WORD ,background="#d87379",foreground="white" ,borderwidth=0,selectborderwidth=0,highlightthickness=0)

textOutput.grid(row= 0, column=3 ,rowspan=38 ,stick = "nswe" ,padx=(30,0),pady=(15,0)  )

win.mainloop()













    