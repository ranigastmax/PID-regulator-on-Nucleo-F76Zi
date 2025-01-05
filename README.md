### README in Polish

# Temperature Control System on STM32

## Opis projektu
Ten projekt dotyczy systemu sterowania temperaturą opracowanego na mikrokontrolerze STM32 z implementacją regulatora PID. Głównym celem było stworzenie układu pozwalającego na regulację temperatury w krokach co 0,5°C za pomocą przycisków '+' i '-'. Komunikacja odbywa się przez UART, co umożliwia sterowanie z aplikacji takich jak RealTerm. 

### Funkcjonalności
- Regulacja temperatury z krokiem 0,5°C.
- Komunikacja z użytkownikiem poprzez port UART.
- Regulacja PID, możliwość doboru parametrów
- Blad ustalony ponizej 1%

### Wymagania
- Mikrokontroler STM32 (np. STM32F103).
- Środowisko programistyczne STM32CubeIDE.
- Czujnik temperatury kompatybilny z STM32.
- Aplikacja do komunikacji szeregowej (np. RealTerm).

### Jak uruchomić
1. Skopiuj kod do projektu w STM32CubeIDE.
2. Skonfiguruj port UART w mikrokontrolerze.
3. Uruchom aplikację komunikacji szeregowej i połącz się z urządzeniem.
4. Używaj przycisków '+' i '-' do regulacji temperatury.

---

### README in English

# Temperature Control System on STM32

## Project Description
This project involves a temperature control system developed on an STM32 microcontroller with the implementation of a PID controller. The main goal was to create a system that allows temperature adjustment in 0.5°C steps using '+' and '-' buttons. Communication is done via UART, enabling control through applications like RealTerm.

### Features
- Temperature adjustment with 0.5°C steps.
- User communication via UART interface.
- PID control, ability to select parameters
-steady-state error below 1%

### Requirements
- STM32 microcontroller (e.g., STM32F103).
- STM32CubeIDE development environment.
- Temperature sensor compatible with STM32.
- Serial communication application (e.g., RealTerm).

### How to Run
1. Copy the code into an STM32CubeIDE project.
2. Configure the UART port on the microcontroller.
3. Launch a serial communication application and connect to the device.
4. Use the '+' and '-' buttons to adjust the temperature.
