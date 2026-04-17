dzien 1

zainstalowalem vs studio, git, stm32cubeid, stm32cubeMXgi

Nie bylo zadnych problemow z pobieraniem

CZEGO SIE NAUCZYLEM
  nauczylem sie delikatnych podstaw jezyka c 
  robienie pierwszych programow z swieceniem diod i miganiem

nie mam zadnych pytan

zrobielm project 1 

dzien 2 

czego sie nauczylem
odczytywania sygnalow
zmiana trybow pracy diod za pomoca przycisku (np ze led10 swiecil po nacisnieciu przycisku led 10 miga i led 9 sie swieci)
zamiast uzywania caly czas if tez uzywania swticha i casow

nie bylo zadnych problemow

projekt STM32F303 Discovery
dzien 3 

czego sie nauczylem 
obsluchi i2c odczytywania sygnalu z miernikow tworzenie tabelek i laczenia danych

lekkie problemy mialem napoczatku z zaczeciem wogole ale po lekkiej pomocy chata zrozumialem o co chodzi i potem tylko mialem lekki problem z magnetometrem ale sobie poradzilem bez jakis wiekszych komplikacji

zrobilem projekcik1
dzien 4 

czego sie nauczylem 
obslugi timerow 
mialem lekkie problemy bo cubemx mi kod zle wygenerowal

zrobilem projket "timery moze"
"

sciaga

GIT
git clone – pobiera repezytorium z githuba na komputer
git status – sprawdza zmiany repezytorium
git add – dodanie plików do commita
git commit -m "wiadomość" - zapisuje zmiany lokanie
git push – wysyla te zmiany na github
git log - pokazuje logi z commitow i jaki maja opis i ich dane
git checkout -b "nazwa" - tworzy nowego brancha

STM
HAL_GPIO_ReadPin - odczytuje wartosc z pinu
HAL_GPIO_TogglePin - ustawia stan pinu na przeciwny
HAL_GPIO_WritePin - zapisuje stan pinu
GPIO_PIN_SET - ustawia sygnal pinu na 1
GPIO_PIN_RESET - ustawia sygnal pinu na 0
switch(zmienna) - sprawdza wartosc zmiennej 
case n - uzywane przy switchu zeby co zrobic przy jakies wartosci (trzeba jeszcze pod koniec case dac break zeby program nie lecial dalej z casami)
 HAL_I2C_Mem_Read - czyta mi z pamieci jakiegos danego przez I2C (pierw daje sie ktory i2c, adres czujnika, adres rejestru, rozmiar adresu, mag_data, ile bajtow czytac, przez jaki czas)
&& - and
int16_t ax = data[0] | (data[1] << 8); - laczy te dwa miejsca z tabeli w jedna 16 bitowa zmienna i przenosi data[1] o 8 bitow
uint8_t - tworzy 8 bitowa zmienna

przedrostki o zmiennych(volatile, static)
-volatile - wartosc jest sprawdzana ciagle
-static zmienna zapamietuje wartosc miedzy wywolaniami funkcji

TIMERY 
prescaler - oznacza ile razy zegar bedzie wolniejszy timer clock = cpu clock / prescaler
ARR - auto reload register - maksymalna liczba tickow przed resetem 
czas przez ktory bedzie liczyc - timer clock/counter period = x hz czas = 1/x
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) - wywoluje funkcje jak ktorys z timerow wyliczy czas
HAL_TIM_Base_Start_IT(&htim2); - startuje odliczanie timerow tim2
