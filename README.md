# Kursinis-darbas

# Introduction

APIE KĄ DARBAS:

Darbo tema- Žaidimo paskyrų tvarkymas. Tai programa, kuri simuliuoja žaidėjų paskyrų duomenų registravimą, paskyrų pridėjimą/pašalinimą iš sistemos, žaidėjų tarpusavio ryšį(pridėjimas į draugus) ir galimybę standartinio tipo paskyros keitimą į premium.

KAIP PALEISTI PROGRAMĄ:
+ Atidaryti dokumentą "kursinis.py" per pasirinktą programą (Naudota "Studio Visual Code")
+ Pridėti dokumentą "accounts_info.txt", kuriame surašyti žaidėjų registracijos duomenys
+ Paleisti programą (Run and debug)

KAIP NAUDOTIS PROGRAMA:
+ Žaidėjų registracijos duomenys surašomi į dokumentą "accounts_info.txt", kur vienoje eilutėje pateikiami visi duomenys atskiriant tik kableliu ir tokia tvarka: Vardas,Pavardė,Slapyvardis,Prisijungimo data(y-m-d),Paskyros tipas
+ Rašant kodo apačioje per objektą galima atlikti šiuos veiksmus su žaidėjų paskyromis nauojant jų slapyvardžius:
  
    Pakeisti (paupdatinti) iš standartinės paskyros į premium:
    ```python
    manager.update_to_premium("jonukas")
    ```

    Pridėti į draugus:
    ```python
    manager.add_friend_by_username("jonukas", "Emma_xo")
    ```

    Pašalinti iš draugų:
    ```python
    manager.remove_friend_by_username("Hey_Dom", "Emilai")
    ```
    Išrašyti norimą paskyrų sąrašą (Visų paskyrų/Premium paskyrų/Standart paskyrų):
    ```python
    output_file.write(manager.display_all_accounts("Premium"))
    ```

+ Paleidžiama programa
+ Veiksmai, atlikti su paskyromis matomi ant ekrano
+ Duomenys apie kiekvieną žaidėją bei pasirinkti žaidėjų sąrašai matomi ir išsaugojami atsirai susikūrusiame dokumente "accounts_output.txt"
  

# Analysis

FUNKCINIAI REIKALAVIMAI:
+ Polimorfizmas
+ Abstakcija
+ Paveldėjimas
+ Inkapsuliacija


PAPILDOMI REIKALAVIMAI:
+ Agregacija
+ Design pattern
+ Skaitymas/Rašymas iš dokumentų


POLIMORFIZMAS

-Tai yra objektinio programavimo principas, kai metodai, esantys skirtingose klasėse, bet su vienodais pavadinimais, gali atlikti skirtingus veiksmus, kurie nurodyti jų viduje.

Polimorfizmas kode:
  
  "add_friend()" metodas tėvinėje klasėje "Account()".
  
  Skirtas draugų pridėjimui į sąrašą atitinkamo žaidėjo ir atitinkamo žaidėjo pridėjimas į to       draugo draugų sąrašą.
  ```python
  def add_friend(self, friend):
      if friend not in self._friends:
        self._friends.append(friend)
      if self not in friend._friends:
        friend._friends.append(self)
  ```
  "add_friend()" metodas dukterinėje klasėje "StandardAccount()".
  
  Skirtas patikrinti, ar standartinio tipo paskyrą turintis žaidėjas neviršija nustatyto draugų     limito(5), tikrinama kreipiantis į metodą "can_add_friend", esantį toje pačioje klasėje. Jei     nevykdo "if" sąlygų, šis metodas kreipiasi į bendravardį metodą, esantį tėvinėje klasėje         Account().
  ```python
  def add_friend(self, friend):
      if not self.can_add_friend():
        print(f"\n{self.username} pasiekė maksimalų draugų limitą (5).\n")
        return False
      if isinstance(friend, StandardAccount) and not friend.can_add_friend():
        print(f"\n{friend.username} pasiekė maksimalų draugų limitą (5).\n")
        return False
      super().add_friend(friend)
      return True
  ```
  "add_friend()" metodas dukterinėje klasėje "PremiumAccount()".
  
  Skirtas patikrinti, ar premium tipo paskyrą turintis žaidėjas nebando pridėti į draugus           žaidėją, turintį standartinio tipo paskyrą, kuris jau pasiekė draugų limitą. Jei nevykdo "if"    sąlygų, šis metodas kreipiasi į bendravardį metodą, esantį tėvinėje klasėje Account().
  ```python
  def add_friend(self, friend):
      if isinstance(friend, StandardAccount) and not friend.can_add_friend():
        print(f"\n{friend.username} pasiekė maksimalų draugų limitą (5).\n")
        return False
      super().add_friend(friend)
      return True
  ```

ABSTAKCIJA

-Tai objektinio programavimo principas, kuris leidžia kurti metodus ar klases, kurie tik nurodo galimus veiksmus, bet nenurodo, kaip tie veiksmai atliekami.

Abstakcija kode:

  1) Bendra abstakti bazinė klasė "Account(ABC)", kuri negali būti iškviečiama, bet reikalinga     bendram apibrėžimui 2 tipų (Standart ir Premium) paskyroms, bet nevykdo visų detalių. Klasė     paveldi iš ABC (Abstact Base Class).
     ```python
     from abc import ABC, abstractmethod

     class Account(ABC):
     ```
  2) Abstaktus metodas "account_type" tėvinėje klasėje "Account()", kuris nurodo, kad paskyra       turi turėti kokį nors tipo, bet nepriskiria jokio. Dukterinėse klasėse "StandardAccount()"      ir "PremiumAccount()" pasikartoja metodas "account_type" ir tada nurodo atitinkamai             paskyros tipą.
     ```python
     class Account(ABC):
     
         @property
         @abstractmethod
         def account_type(self):
             pass
     ```

     ```python
     class StandardAccount(Account):

          @property
          def account_type(self):
              return "Standart"
     ```
     ```python
     class PremiumAccount(Account):

          @property
          def account_type(self):
              return "Premium"
     ```

PAVELDĖJIMAS

-Tai objektinio programavimo principas, kai yra tėvinė klasė ir jai priskiriamos dukterinės klasės, kurios paveldi visas savybes ir metodus, kurie priklauso nurodytai tėvinei klasei, bet turėti ir savų, kurių nėra tėvinėje.

Paveldėjimas kode:

  Klasė "Account()" panaudota kaip tėvinė klasė, kurios dukterinės klasės yra     
  "StandardAccount()" ir "PremiumAccount()". Šios dukterinės klasės paveldi informaciją apie 
  žaidėją: first_name, last_name, username, join_date, friends (draugų sąrašas) ir metodus: 
  "add_friend", "remove_friend", "get_account_info", "friends_list", "account_type", 
  "friends_list", "get_account_info". Abi dukterinės klasės perrašo metodą "add_friend" ir 
  papildo abstaktų metodą "account_type". Papildomai klasė "StandardAccount()" turi savo metodą 
  "can_add_friend".

  Tėvinė klasė:
  ```python
  class Account(ABC):
  ```
  Dukterinės klasės:
  ```python
  class StandardAccount(Account):
  ```
  ```python
  class PremiumAccount(Account):
  ```

     
INKAPSULIACIJA

-Tai yra objektinio programavimo pricipas, kuris leidžia reguliuoti prieigą prie duomenų informacijos. Paslėptą arba apsaugotą informaciją gali pasiekti tik pats objektas, o išoriniai objektai turi pasitelkti sąsajas, getterius/setterius (@property). Kad kintamasis arba metodas būtų apsaugotas prirašoms vienas apatinis brūkšnelis "_", o privačiam prirašomi 2 brūkšneliai "__"

  Inkapsuliacija kode:
  
  1) Apsaugoti kintamieji:
     ```python
     def __init__(self, first_name, last_name, username, join_date):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._join_date = join_date
        self._friends = []
     
  2) Apsaugotas kintamasis "_friends" pasiekiamas ir keičiamas tik per metodus "add_friend", "remove_friend", "friends_list".
     
  3) Apsaugoti kintamieji pasiekiami per dekoratorių "@property", kuris leidžia metodą naudoti kaip kintamąjį dėl patogesnio rašymo. (pvz. vietoj viso "self._first_name" (arba jei kitoje klasėje: "Account._first_name") galima toliau kode rašyti tiesiog "first_name")
     ```python
     @property
     def first_name(self):
        return self._first_name
      ```


AGREGACIJA

-Tai yra pragramoje naudojamas objektų tarpusavio ryšys, kuris leidžia iš vieno kreiptis į kitą, bet neapriboja jų egzistavimo (sunaikinus vieną, kitas nesusinaikins).

  Agregacija kode:

  Kiekvienas žaidėjas turi draugų sąrašą, per kurį žaidėjas gali kreiptis į draugus arba draugai į žaidėją, bet panaikinus specifinio žaidėjo paskyrą, jo draugų paskyros nebus panaikamos.


DESIGN PATTERN

-Tai yra programos kodo rašymo šablonas, naudojamas, kad kodo struktūra būtų tvarkinga, o kodas patogiau skaitomas/rašomas.

Šiame kode naudojamas "Singleton" dizaino šablonas, kuris užtikrina, kad atitinkama klasė turėtų tik vieną instanciją, į kuria visada kreipiamasi, nepaisant koks yra objekto pavadinimas. "Singleton" šiame kode užtikrina, kad būtų tik vienas "manager" ir visi su paskyromis susiję veiksmai būtų atliekami tik viename serveryje. Dėl to visi veiksmai yra sinchronizuoti.
```python
class AccountManager():

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccountManager, cls).__new__(cls)
            cls._instance._accounts = []
        return cls._instance

    def get_account_by_username(self, username):
        for acc in self._accounts:
            if acc.username == username:
                return acc
        return None
```
Galima sukurti kelis objektus klasei "AccountManager()", bet visi jie kreipsis į vieną instanciją
```python
manager = AccountManager()
```

SKAITYMAS/RAŠYMAS IŠ DOKUMENTŲ

-Ši programa skaito iš dokumento "accounts_info.txt", kuriame pateikiami pirminiai duomenys apie žaidėjus.
-Programa rašo į dokumentą "accounts_output.txt", kuriame pateikiami struktūrizuoti pradiniai duomenys apie kiekvieną žaidėją ir (galimai) papildyti draugų sąrašai bei pakeisti paskyrų tipai. Taip pat į dokumentą išrašomi pasirinktiniai sąrašai, tai gali būti visų paskyrų, standartinių paskyrų arba premium paskyrų sąrašai.

Skaitymas:
```python
with open("accounts_info.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            first_name, last_name, username, join_date, account_type = line.split(",")
            join_date = datetime.strptime(join_date, "%Y-%m-%d")

            if account_type == "Standart":
                account = StandardAccount(first_name, last_name, username, join_date)
            elif account_type == "Premium":
                account = PremiumAccount(first_name, last_name, username, join_date)
            else:
                print(f"Nežinomas paskyros tipas: {account_type}")
                continue

            manager.add_account(account)
```
Rašymas:
```python
with open("accounts_output.txt", "w", encoding="utf-8") as output_file:
        for player in manager.get_all_accounts():
            output_file.write(player.get_account_info())
            output_file.write("\n" + "=" * 40 + "\n")

        output_file.write(manager.display_all_accounts("Premium"))
        output_file.write("\n" + "=" * 40 + "\n")
        output_file.write(manager.display_all_accounts("Standart"))
        output_file.write("\n" + "=" * 40 + "\n")
        output_file.write(manager.display_all_accounts())
```


REZULTATAI

+ Programa nuskaito duomenis apie kiekvieną žaidėją iš dokumento "accounts_info.txt".
+ Pagal nurodymus programa gali: pakeisti į premium paskyrą, pašalinti/pridėti žaidėją, sukurti/pašalnti žaidėjų tarpusavio ryšį (žaidėjai prideda/pašalina vienas kitą į/iš draugų)
+ Programa išsaugo atliktus pakeitimus, kurie tiesiogiai matomi ant ekrano ir išsisaugo sistemoje apie kiekvieną žaidėją
+ Programoje veiksmai atliekami naudojant žaidėjo slapyvardį, kurio, pagal dabartinį kodą, negalima pakeisti
+ Papildomas sunkumas atsiranda keičiant žaidėjo paskyros tipą, kadangi sukuriamas naujas žaidėjas su indentiška informacija, išskyrus paskyros tipas kitas. Būtina kurti naują žaidėją, nes tik taip užtikrinama, kad žaidėjas priklauso teisingai klasei ir turi preium paskyros privilegijas.

# Conclusions

Programa, skirta žaidėjų paskyrų tvarkymui yra labai universali, kadangi programoje skaitoma ir tvarkoma standartinė informacija. Šis kodas geba perskaityti informaciją, ją išrašyti tvarkingesniu formatu, pateikti 3 skirtingus žaidėjų sąrašus, žaidėjų paskyros gali būti susietos pridedant vienas kitą į draugų sąrašą, taip pat ryšius galima panaikinti. Žaidėjų paskyras galima pakeisti iš srandartinės į premium. Naudojamas "Singleton" šablonas, kad nesusidarytų atskiri sąrašai paskyroms ir visos būtų sinchronizuotai tvarkomos.
Ateityje būtų galima išplėsti premium paskyros privilegijas(pvz. paskyros "bio" pridėjimas). Taip pat daugiamečiai ištikimi žaidėjai galėtų "užsitarnauti" standartinės paskyros pakeitimą į premium ir kt.






    
    

