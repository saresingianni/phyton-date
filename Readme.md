
# Confronto di una data nel formato giorno/mese del anno attuale Utilizzando Pyhton 3.8

### Inserisco una data nel formato dd/mm su una scelta di stati per cercare se quella data appartiene ad una festività o ad anniversario 
 *  Indica il giorno della settimana ad esempio "Sabato" o "Domenica" o "Lunedi"


 <p align="left">
  <img src="foto/foto1.jpg" width="350" title="console del programma">
</p>
  *  come si nota abbiamo delle scelte tramite questo menu 

 <p align="left">
  <img src="foto/foto2.jpg" width="350" title="opzione di scelta">
</p>

 *  Selezionandouno stato selezionato interroghiamo il file che ci viene ritornato dalla seguente pagina web
 *  "https://giorni-festivi.eu"
 verrà preso e processato.
 * la prima cosa che fa è quello di controllare inserimento corretto della opzione di scelata e della formattazione della data

 <p align="left">
  <img src="foto/foto3.jpg" width="350" title="controllo">
</p>

*   una volta controllato parte un ciclo che recupera le eventuali occorrenze con una festivita nazionale
 se la trova viene sttampato l'occorenza viene indicata se il giorno trattato è di Sabato o di Domenica o un giorno 
 feriale

 <p align="left">
  <img src="foto/foto4.jpg" width="350" title="opzione di scelta">
</p>

si esce dal programma premendo q

### Librerie Aggiunte in Phton nel progetto
 
 

C:\Users\Gianni>pip list
 *  Package         Version
 *  altgraph        0.17
 *  arrow           0.14.7
 *  certifi         2020.6.20
 *  chardet         3.0.4
 *  future          0.18.2
 *  icalendar       4.0.6
 *  ics             0.7
 *  idna            2.10
 *  numpy           1.19.0
 *  pandas          1.0.5
 *  pefile          2019.4.18
 *  pip             19.2.3
 *  PyInstaller     3.6
 *  python-dateutil 2.8.1
 *  pytz            2020.1
 *  pywin32-ctypes  0.2.0
 *  requests        2.24.0
 *  setuptools      41.2.0
 *  six             1.15.0
 *  TatSu           5.5.0
 *  urllib3         1.25.9



il controllo del 'inserimento ven  contoller
     mmnmnm
     
    tt4t4t @GetMapping("/showUtenti")
    * def is_size(check_input,size_menu):<br>
 '''<br>
 funzione che controlla se hai inserito un numero piu grande delle opzioni di scelta<br>
 return : bool<br>
 '''<br>
 #print(repr(check_input))<br>
 #print(repr(size_menu))<br>
 if check_input < size_menu :<br>
          return True<br>
      return False<br>


 * def is_digit(check_input):<br>
 '''<br>
 function controlla se hai digitato un numero<br>
 return : bool<br>
 '''<br>
 if check_input.isdigit():<br>
         return True<br>
    return False<br>

 * def is_string_only(check_input):<br>
 '''<br>
  function controlla se hai inserito solo delle letter<br>
  '''  return : bool<br>
 ''' <br>      
      if check_input.isalpha():<br>
          return True<br>
      return False<br>

 * def is_string_with_space(check_input):<br>
      '''<br>
      function controlla se hai inserito degli spazi<br>
      return : bool<br>
      ''' <br>  
      valid = False<br>
      if ' ' in check_input:<br>
          for char in check_input:<br>
              if char.isdigit():<br>
                  valid = False<br>
              elif char.isalpha() or char.isspace():<br>
                  valid = True<br>
  return valid<br>

 * def is_string_or_num(check_input):<br>
     '''<br>
     function controlla se hai inserito lettere  eumeri<br>
     return : bool<br>
     '''<br>      
     if check_input.isalnum():<br>
          return True<br>
     return False<br>

 * def is_float(check_input):<br>
      '''<br>  
      function cotrolla se hai inserito virgole mobili<br>
      return : bool<br>
      '''   <br>
      if '.' in check_input:<br>
          split_number = check_input.split('.')<br>
          if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():<br>
                  return True<br>
      return False<br>


  * differenza di date<br>
  def diff_dates(date1, date2):<br>
      #print ("diff_dates")<br>
      return abs(date2-date1).days<br>
 


    gono inserite  tramite definizioni



 
chiamata alla lista che viene fornita nel metodo 
  
  
  contoller
     mmnmnm
     
    tt4t4t @GetMapping("/showUtenti")
    public ModelAndView showUtenti() {

        List < QuintoPiano > quintopianoU = quintoPianoRepository.findAll();

        Map < String, Object > params = new HashMap < String, Object > ();
        params.put("quintopianoU", quintopianoU);

        return new ModelAndView("showUtenti", params);
    } 
    
    
    la parte per la costursiobne della tabella avviene
    
    
   
* [ tramite questo script dove abbiamo la chiamata princpale e la costruzione della ricerca della tabella con i Datatable ]( https://datatables.net/)


 
 
   
       <script>
        $(document).ready(function(){
      
        var table = $('.dataTables-example').tableToJSON(); // Convert the table into a javascript object
  console.log(JSON.stringify(table));
  <!--alert(JSON.stringify(table)); -->
    
     

   
       $('.dataTables-example').DataTable({
                
                
                
                
                pageLength: 25,
                responsive: true,
                dom: '<"html5buttons"B>lTfgitp',
                buttons: [
                    {extend: 'copy'},
                    
                    
                    
                    {extend: 'csv'},
                    {extend: 'excel', title: 'ExampleFile'},
                    {extend: 'pdf', title: 'ExampleFile'},

                    {extend: 'print',
                     customize: function (win){
                            $(win.document.body).addClass('white-bg');
                            $(win.document.body).css('font-size', '10px');

                            $(win.document.body).find('table')
                                    .addClass('compact')
                                    .css('font-size', 'inherit');
                    }
                    }
                ]

            });

        });
 </script>
    


* [ qui per il donwload del file opzione Salva oggetto con nome]( target/EsempioFreeMarkerH2-0.0.1-SNAPSHOT.jar)

i comandi per farlo partire dal prompt  riga di comando 

java -jar EsempioFreeMarkerH2-0.0.1-SNAPSHOT.jar

il jar deve risiedere nella root del bash

* [ nel broswer http://localhost:8080 ]( http://localhost:8080)









# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Apache Maven documentation](https://maven.apache.org/guides/index.html)
* [Spring Boot Maven Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/maven-plugin/)
* [Spring Data JPA](https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/reference/htmlsingle/#boot-features-jpa-and-spring-data)
* [Apache Freemarker](https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/reference/htmlsingle/#boot-features-spring-mvc-template-engines)
* [Spring Web](https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/reference/htmlsingle/#boot-features-developing-web-applications)

### Guides
The following guides illustrate how to use some features concretely:

* [Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/)
* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/bookmarks/)

********************************
Tools and Technologies used

Spring Boot 2+

Maven 3+

STS or Eclipse IDE

Freemarker

JDK 8+ or OpenJDK 8+

H2 Database

Hibernate - 5.2.17.Final


Development Steps

Create a Spring Boot Application

Maven Dependencies

Project Structure

Contoller

Model

Repository

JPA Entity - Employee.java

JPA Repository - EmployeeRepository.java

Define Spring Controller - EmployeeController.java

Define View Templates

Run Application"# Python_date" 
