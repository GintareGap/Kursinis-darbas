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
+ Kompozicija/Agregacija


POLIMORFIZMAS

-Tai yra objektinio programavimo principas, kai metodai, esantys skirtingose klasėse, bet su vienodais pavadinimais, gali atlikti skirtingus veiksmus, kurie nurodyti jų viduje.

~ Polimorfizmas kode:
  
  "add_friend()" metodas tėvinėje klasėje Account().
  
  Skirtas draugų pridėjimui į sąrašą atitinkamo žaidėjo ir atitinkamo žaidėjo pridėjimas į to       draugo draugų sąrašą.
  ```python
  def add_friend(self, friend):
        if friend not in self._friends:
            self._friends.append(friend)
        if self not in friend._friends:
            friend._friends.append(self)
  ```
  "add_friend()" metodas dukterinėje klasėje StandardAccount().
  
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
  "add_friend()" metodas dukterinėje klasėje PremiumAccount().
  
  Skirtas patikrinti, ar premium tipo paskyrą turintis žaidėjas nebando pridėti į draugus           žaidėją, turintį standartinio tipo paskyrą, kuris jau pasiekė draugų limitą. Jei nevykdo "if"    sąlygų, šis metodas kreipiasi į bendravardį metodą, esantį tėvinėje klasėje Account().
  ```python
  def add_friend(self, friend):
        if isinstance(friend, StandardAccount) and not friend.can_add_friend():
            print(f"\n{friend.username} pasiekė maksimalų draugų limitą (5).\n")
            return False
        super().add_friend(friend)
        return True
  ```



    
    

