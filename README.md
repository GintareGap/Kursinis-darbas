# Kursinis-darbas

# Introduction

APIE KĄ DARBAS:
Darbo tema- Žaidimo paskyrų tvarkimas. Tai programa, kuri simuliuoja žaidėjų paskyrų duomenų registravimą, paskyrų pridėjimą/pašalinimą iš sistemos, žaidėjų tarpusavio ryšį(pridėjimas į draugus) ir galimybę standartinio tipo paskyros keitimą į premium.

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
  



    
    

