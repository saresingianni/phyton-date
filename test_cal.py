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
#print (size_menu)

def diff_dates(date1, date2):
    #print ("diff_dates")
    return abs(date2-date1).days

def main_festivita(indice,size,trovato_giorno_festivo,trovato_giorno_lavorativo,
                   anno_check,mese_check,giorno_check,
                   anno_data_entry,mese_data_entry,giorno_data_entry,
                   year,descrizione,stato):
   
    #print ("main_festivita")
    #print (str(indice),str(size))
    #print (tovato_festivita)
    #print (anno_check)
    #print (mese_check)
    #print (giorno_check)
    #print ("***********")
    #print (anno_data_entry)
    #print (mese_data_entry)
    #print (giorno_data_entry)
    #print (descrizione)
    #print ("test date")
    #print ("d1")
    #d1 = date(2013,9,13)
    d1 = date(anno_check,mese_check,giorno_check)
    #print ("d2")
    d2 = date(anno_data_entry,mese_data_entry,giorno_data_entry)
    d3 = date(year,mese_data_entry,giorno_data_entry)
    #d2 = date(2013,9,13)
    result1 = diff_dates(d2, d1)
    anniversario_test=[' ']
    #print ('{} days between {} and {}'.format(result1, d1, d2)+" abbiamo trovato una festivita "+descrizione)
    #print ('{} days between {} and {}'.format(result1, d1, d2))
    a=calendar.weekday(year,mese_data_entry,giorno_data_entry)
    days=["Lunedi","Martedi","Mercoledi","Giovedi","Venerdi","Sabato","Domenica",""]
    #print("result1 "+str(result1)+" "+str(indice) + " "+str(size))


    if(days[a]=="Sabato" or days[a]=="Domenica"):
       trovato_giorno_festivo=True

    elif(days[a]=="Lunedi" or days[a]=="Martedi" or
       days[a]=="Mercoledi" or days[a]=="Giovedi" or
       days[a]=="Giovedi"):
       trovato_giorno_lavorativo=True

   
    
    if(result1==0):
        print("Per la seguente data inserita "+str(giorno_data_entry)+"/"+ str(mese_data_entry)
            +"/"+ str(year) +" per lo stato " +stato +" abbiamo trovato l' anniversario  del "+descrizione
            )
    else:
      if(trovato_giorno_festivo):
         if(indice==size):
             print("di "+days[a])
       
      elif(trovato_giorno_lavorativo):
          if(indice==size):
              print("di "+days[a]+" ")



                   
      
           

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
               
                trovato_giorno_festivo=False;
                trovato_giorno_lavorativo=False;
               
                #print ("testo")
                #print (testo)
                #print ("***********")
                gcal = Calendar.from_ical(testo)
                size=0
                for component in gcal.walk():
                    if component.name == "VEVENT":
                        size=size+1
                #        print (str(size)+" "+component.name)
                #        gcal = Calendar.from_ical(testo)
               
                indice=0
               
                
                
                for component in gcal.walk():

                 if component.name == "VEVENT":

                    indice=indice+1
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


                   
                    #main_festivita(indice,size,
                    #               trovato_giorno_festivo,trovato_giorno_lavorativo,
                    #               anno_check,mese_check,giorno_check,anno_check,
                    #               int(month),int(day),int(year),
                    #               descrizione,stati_list[int(user_input)])
                    main_festivita(indice,size,
                                   trovato_giorno_festivo,trovato_giorno_lavorativo,
                                   anno_check,mese_check,giorno_check,anno_check,
                                   int(month_me),int(day_me),int(year),
                                   descrizione,stati_list[int(user_input)]) 

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
 

      
