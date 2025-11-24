# Jezici specifični za domen (engl. *Domain Specific Languages*)
- u nastavku **JSD**
- Jezici koji se koriste za iskazivanje rešenja problema tačno određenog domena.
- Manje ili više pokrivaju domen problema. U idealnom slučaju ga pokrivaju tačno.
- Mogu biti vizuelni i tekstualni (mi ćemo se fokusirati na ove druge).
- Tekstualni JSD-ovi se obično prevode na jezik opšte namene (engl. 
  *General Purpose Language*, u nastavku JON). JON se dalje prevodi na 
  mašinski jezik, koji se izvršava na ciljnoj hardverskoj arhitekturi.

## *textX*
- *textX* koristi [*PEG* parser](https://en.wikipedia.org/wiki/Parsing_expression_grammar) 
  (posebna vrsta silaznog parsera).
- Bitan redosled navođenja izbora. 
- Prilikom pisanje *PEG* gramatike potrebno je razmišljati
  kao parser.
- Ove gramatike nisu deklarativne prirode. 
- Nije dovoljno samo navesti šta parser treba da uradi, već i kako.
- Rezultat rada *textX* parsera je sintaksno stablo iskazano *Python* objektima.
- Pogledati primere koda.


## Teme za dodatno istraživanje (fakultativno)

### Programski prevodioci
- Proces prevođenja JSD-a na JON obavlja programski prevodilac.
- Programski prevodilac je program koji program iskazan jezikom višeg nivoa
  (u našem slučaju JSD-om) 
  prevodi na ekvivalentan program iskazan jezikom nižeg nivoa
  (u našem slučaju JON-om).
- Programski prevodioci se obično sastoje iz dva dela: prednjeg i zadnjeg.
- Prednji deo obavlja: leksičku, sintaksnu i semantičku analizu, generisanje međukoda 
  i optimizaciju istog.
- Zadnji deo obavlja: generisanje koda i eventualno optimizaciju generisanog koda.
- Mi ćemo se na ovom kursu pretežno baviti sintaksnom analizom.
- Programske prevodioce ćemo pisati [textX alatom](http://textx.github.io/textX/stable/).

### Sintaksna analiza
- Proces u kome se proverava korektnost programa u skladu sa sintaksnim pravilima.
- Sintaksa pravila se iskazuju uglavnom nekom vrstom Bakus-Naurove forme
- Rezultat sintaksne analize je stablo parsiranja.
- Sintaksna analiza se drugačije naziva parsiranje.
- Obavljaju je parseri.
- Parsiranje može biti: silazno (engl. *top-down*) i uzlazno (engl. *bottom-up*).

#### Silazno parsiranje
- Silazno parsiranje kreće od početnog neterminalnog simbola
gramatike, koji predstavlja korenski čvor apstraktnog stabla sintakse. Spuštajući se
niz stablo, primenjuje pravila izvođenja sa namerom da dođe do terminalnih simbola
koji odgovaraju sekvenci karaktera izvornog koda.
- Ne podržavaju levu rekurziju. 
- Na SPP-u smo sami pisali silazni parser.

#### Uzlazno parsiranje
- Uzlazno parsiranje kreće od niza terminalnih simbola, koji
odgovaraju ulaznoj sekvenci karaktera izvornog koda. Pokušava da ih zameni sa
odgovarajućim neterminalnim simbolima, penjući se uz apstraktno stablo sintakse sve
do korenskog čvora. Ovaj čvor predstavlja početni neterminalni simbol gramatike
- Podržavaju levu rekurziju.
- Kao primer uzlaznih parsera, najčešće se navode *LR* parseri, za koje je
karakteristično da sekvencu terminalnih simbola čitaju sa leva na desno (engl. *Left-to-right*)
gradeći najviše desno izvođenje u obrnutom redosledu (engl. *Right-most derivation in
reverse*)
- Drugi naziv za *LR* parsere je *Shift-Reduce*. Kao što im samo ime kaže, 
  koriste dva tipa operacija shift i reduce.
- Na PP-u smo koristili Flex i Bison.
- Koga zanimaju *LR* parseri, može da pogleda [parglare](http://www.igordejanovic.net/parglare/grammar_language/).

## Literatura
- http://textx.github.io/textX/stable/Višetruko nasleđivanje
- http://www.igordejanovic.net/parglare/stable/
- http://textx.github.io/textX/stable/tutorials/hello_world/
- http://textx.github.io/textX/stable/tutorials/robot/
- http://textx.github.io/textX/stable/tutorials/entity/
- https://github.com/textX/textX
- https://github.com/textX/textX/blob/master/examples/expression/calc_processors.py