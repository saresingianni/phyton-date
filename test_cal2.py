import requests
import calendar
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
'''
gianni inserendo una data controllo festivita, loscopo e di i
nserire una data per controllare se essa appartenga
a un evento anniverasario di uno stato  "
'''
import datetime
from datetime import date

stati_list = ['Italia' , 'svizzera' , 'austria','francia' , 'germania' , 'brasile','portogallo','spagna','stati-uniti']
size_menu = (len(stati_list))
anniversario=""
#print (size_menu)q

def diff_dates(date1, date2):
    #print ("diff_dates")
    return abs(date2-date1).days



def ricerca_festivita (my_raccolta,
                       anno_check,mese_check,giorno_check,
                       anno_data_entry,mese_data_entry,giorno_data_entry):
                       #print("sono dentro ")
                       d1 = date(anno_check,mese_check,giorno_check)
                       #print("passato d1 ")
                       d2 = date(anno_data_entry,mese_data_entry,giorno_data_entry)
                       #print("passato d2 ")
                       result1 = diff_dates(d2, d1)
                       #print("result1  "+str(result1))
                      
                      
                       if result1==0 :
                         my_raccolta["anniversario"]=True
                       else:
                         my_raccolta["anniversario"]=False
                       
                      
                       
                       #for key, value in my_raccolta.items() :
                       #    if( my_raccolta["anniversario"]!=True):
                       #      print (key, value)
                      
                       return my_raccolta




def ricerca_giorno_festivo (my_raccolta,year,mese_data_entry,giorno_data_entry):
                            a=calendar.weekday(year,mese_data_entry,giorno_data_entry)
                            days=["Lunedi","Martedi","Mercoledi","Giovedi","Venerdi","Sabato","Domenica"]
                            if(days[a]=="Sabato" or days[a]=="Domenica"):
                                 my_raccolta["giorno_festivo"]=True
                            elif(days[a]=="Lunedi" or days[a]=="Martedi" or
                                 days[a]=="Mercoledi" or days[a]=="Giovedi" or
                                 days[a]=="Giovedi"):
                                 my_raccolta["giorno_festivo"]=False
                            return my_raccolta



def is_size(check_input,size_menu):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    #print(repr(check_input))
    #print(repr(size_menu))
    if check_input < size_menu :
        return True
    return False


def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False

def is_string_only(check_input):
    '''
    function checking if your string is all letters
    return : bool
    '''    
    if check_input.isalpha():
        return True
    return False

def is_string_with_space(check_input):
    '''
    function checking if your string is all letters, but including space(s)
    return : bool
    '''   
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
            elif char.isalpha() or char.isspace():
                valid = True
    return valid

def is_string_or_num(check_input):
    '''
    function checking if your string is all letters or numbers
    return : bool
    '''       
    if check_input.isalnum():
        return True
    return False

def is_float(check_input):
    '''
    function checking if your string is a floating point
    return : bool
    '''   
    if '.' in check_input:
        split_number = check_input.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                return True
    return False


#menu:
today = datetime.date.today()
anno_check =today.year
print (f'fai la tua scelta per Anno :'+str(anno_check))
for index, item in enumerate(stati_list):
    print(f'{index} : {item}')
print (f'premi \'q\' per uscire dal programma\n')

#set user input to nothing to force entry into the while loop
user_input = ''
my_raccolta=dict()
str_trovato_anniversario=''
str_trovato_cardinale=''
while user_input != 'q' :
    user_input = input('inserisci la scelta desiderata : ')
    #print("test")
    #print(is_size(int(user_input),size_menu))
    #make sure the user types an actual integer if the input is not q (to quit)
    while user_input != 'q' and not is_digit(user_input) and is_string_only(user_input) : 
        print (f'per favore riprova , é richiesto un intero come input')


        user_input = input('inserisci la scelta desiderata :')
         
    #if the user does not want to quit, we will print the choice
    if user_input != 'q':
      if not(is_float(user_input)):
        if (is_string_or_num(user_input)):
         if is_size(int(user_input),size_menu):


            try:
              inputDate_me = input("inserisci la data nel formato 'dd/mm' : ")
              format = "%d/%m/%Y"
              day_me,month_me= inputDate_me.split('/')
              #print("day_me."+str(day_me))
              #print("month_me."+str(month_me))

              inputDate_me= day_me+"/"+month_me+"/"+str(anno_check)
              datetime.datetime.strptime(inputDate_me, format)
             
              
              #inputDate = input("inserisci la data nel formato 'dd/mm/yy' : ")
             
              #datetime.datetime.strptime(inputDate, format)
              #day,month,year = inputDate.split('/')
              print("la data e inserita in modo corretto."+str(inputDate_me))
              #print("la data e inserita in modo corretto."+str(inputDate))
              #print(my_raccolta)
              isValidDate = True
              try :
                         datetime.datetime(anno_check,int(month_me),int(day_me))
                         #datetime.datetime(int(year),int(month),int(day))
                         year=anno_check
              except ValueError :
                          isValidDate = False
              if(isValidDate) :
                print ("la data inserita  è valida  ..")
                
                testo = requests.get("https://giorni-festivi.eu/ical/"+stati_list[int(user_input)]+"/"+str(anno_check)).text
               

                gcal = Calendar.from_ical(testo)
                # size=0
                # for component in gcal.walk():
                #    if component.name == "VEVENT":
                #         size=size+1
                #        print (str(size)+" "+component.name)
                #        gcal = Calendar.from_ical(testo)
               

                for component in gcal.walk():

                 if component.name == "VEVENT":


                    descrizione = component.get('SUMMARY')
                    #print(descrizione)
                    date_start = component.get('DTSTART')
                    #print (date_start.to_ical())
                    date_end1 = component.get('DTEND')
                    #print (date_end1.to_ical())
                    date_time = component.get('DTSTAMP')
                    #print (date_time.to_ical())
                   
                    mese_check=date_start.dt.month
                    giorno_check=date_start.dt.day
                    #print (trovato_festivita)
                    
                    my_raccolta= {'stato':stati_list[int(user_input)],
                                  'descrizione':descrizione,
                                  'date_start':date_start,
                                  'date_end1':date_end1,
                                  'date_time':date_time,
                                  'anniversario':False,
                                  'giorno_festivo':False}   

                   

                    
                    ricerca_festivita (my_raccolta,
                                        anno_check,mese_check,giorno_check,
                                        anno_check,int(month_me),int(day_me))
                    ricerca_giorno_festivo (my_raccolta,
                                        anno_check,int(month_me),int(day_me))
                    #print ('******test*********')
                    for key, value in my_raccolta.items() :
                      if(key=='anniversario' and value==True):
                       str_trovato_anniversario="Per la seguente data inserita "+str(day_me)+"/"+ str(month_me)+"/"+ str(anno_check) +" per lo stato " +my_raccolta["stato"] +" esiste l' anniversario del " +descrizione
                       #print(str_trovato_anniversario)
                       #print ('key == value')
                       #print (key, value)

                        #if(key=='descrizione'):
                          #print ('key == value')
                         # print (key, value)
                        #elif(key=='date_start'):
                          #print ('key == value')
                          #print (key, date_start.to_ical())
                        #elif(key=='date_end1'):
                          #print ('key == value')
                          #print (key, date_end1.to_ical())
                        #elif(key=='date_time'):
                          #print ('key == value')
                          #print (key, date_time.to_ical())
                        #elif(key=='anniversario'):
                         # print ('key == value')
                         # print (key, value)
                        #elif(key=='giorno_festivo'):
                              #print ('key == value')
                          #print (key, value)
                
                if(len(str_trovato_anniversario)>0) :
                 print(str_trovato_anniversario)
                else:
                     #for key, value in my_raccolta.items() :
                       #print (key, value)
                       if(my_raccolta["giorno_festivo"]==True) :
                        #print (key, value)
                        print("Per la seguente data inserita "+str(day_me)+"/"+ str(month_me)+"/"+ str(anno_check) +" per lo stato " +my_raccolta["stato"] +" non esiste un anniversario  ed è un giorno Festivo")
                       if(my_raccolta["giorno_festivo"]==False) :
                        #print (key, value)
                        print("Per la seguente data inserita "+str(day_me)+"/"+ str(month_me)+"/"+ str(anno_check) +" per lo stato " +my_raccolta["stato"] +" non esiste un anniversario  ed è un giorno Feriale")
                
 
                str_trovato_anniversario=''
              
              else :
                print ("la data inserita  non è valida  .")
                

            except ValueError:
              print("La data non è corretta deve essere 'dd/mm' ")
            else:
               #controllo se il dato e un intero not q (uscita )
              while user_input != 'q' and not is_digit(user_input):
                  print (f'prego riprova, e richiesto un intero')
                  user_input = input('inserisce la scelta giusta ')
                  #if the user does not want to quit, we will print the choice
                  if user_input != 'q':
                      print (f'Hai selezionato {stati_list[int(user_input)]}')

 

      
