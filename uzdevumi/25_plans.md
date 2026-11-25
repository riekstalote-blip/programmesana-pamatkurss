# Ievade
1. Pajautāt spēlētājam skaitli no 1-10
2. Nolasīt spēlētāja skaitli
# Apstrāde
3. Ģenerēt nejaušu skaitli no 1 līdz 10
4. Salīdzināt spēlētāja skaitli ar ģenerēto skaitli
# Izvade
5. Ja skaitļi sakrīt, parādīt "Tu uzvarēji".
6. Ja skaitļi nesakrīt, parādīt "Tu zaudēji".
7. Parādīt pareizo skaitli.

## |  Mainīgā vards     | datu tips|           ko glabā            |
### |:----------------- | :------: | -----------------------------:|
### | nejaušais_skaitlis|   int    | datora ģenerēto skaitli       |     
### | speletaja_skaitlis|   int    | spēlētāja ievadīto skaitli    |
### | starpiba          |   int    | starpību starp abiem skaitļiem|

starpiba=abs(speletaja_skaitlis - nejaušais_skaitlis)

speletaja_skaitlis - tiek ievadīts ar input().
nejaušais_skaitlis - tiek nejauši ģenerēts.
starpiba - tiek aprēķināta ar formulu.
Ja starpība ir 0, spēlētājs uzvar. Citādi spēlētājs zaudē

Mazi skaitļi: 
starpiba = abs(1 - 2) = 1
Vidēji skaitļi:
starpiba = abs(5 - 5) = 0
Lieli skaitļi:
starpiba = abs(10 - 8) = 2
  

## Secinājums
Formulu ir vērts pārbaudīt pirms visas programmas rakstīšanas, rakstīšanas, lai pārliecinātos, ka tā darbojas pareizi un nav aprēķinu kļūdu.

      