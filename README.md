# Anti Hate System - AHS
<img src="https://github.com/Joberooo/AntiHateSystem/blob/main/images/logo.png" width="100%">


Aplikacja mająca na celu wykrywanie hejtu w treściach wyświetlanych an ekranie komputera i powiadamianie o nich drogą mejlową. Została ona przygotowana w ramach zadnia konkurowego na hackaton Hack4Lem.
Jest ona kierowana przede wszystkim do rodziców i opiekunów dzieci oraz nastolatków. Jej zadaniem jest poinformowanie ich o występowaniu hejtu w życiu młodych ludzi.

## Autorzy
*   [Patryk Barczak](https://github.com/Joberooo "Git")
*   [Piotr Ciećwierz](https://github.com/peterCcw "Git")
*   [Adrian Malik](https://github.com/h4dri "Git")
*   [Norbert Waszkowiak](https://github.com/kajkitsu "Git")


## Zasada działania i funkcjonalności
Aplikacja działa w formie lokalnie uruchamianego serwera Flask. Cyklicznie sprawdza ekran w poszukiwaniu ciągów tekstowych zawierających sformułowania obraźliwe.
Wykorzystuje ona dwa modele uczenia maszynowego - pierwszy do wyszukania ciągów tekstowych widocznych na ekranie oraz drugi drugi do analizy tych ciągów tekstowych.
W momencie wykrycia zadanej liczby obraźliwych wpisów, przesyła informację na skrzynkę mailową.

### Modele uczenia maszynowego

## Zrzuty ekranu 

<img src="https://github.com/Joberooo/AntiHateSystem/blob/main/images/home.png" width="80%">

<img src="https://github.com/Joberooo/AntiHateSystem/blob/main/images/info_panel.png" width="80%">

<img src="https://github.com/Joberooo/AntiHateSystem/blob/main/images/stats.png" width="80%">

<img src="https://github.com/Joberooo/AntiHateSystem/blob/main/images/settings.png" width="80%">
