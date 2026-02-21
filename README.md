**EN:** [NetGuard Adventure — English Version](#netguard-adventure-en)

**MK:** [NetGuard Adventure — Македонска Верзија](#netguard-adventure-mk)

---

# NetGuard Adventure [EN]

NetGuard Adventure is a 2D educational game developed in Python using Pygame, designed to teach children about safe internet behavior through interactive gameplay, quizzes, and reward-based progression.

The game combines classic platform mechanics with cybersecurity-themed questions, helping players learn how to make safer online decisions while advancing through multiple difficulty modes. Available in English and Macedonian, the game ensures accessibility for a diverse audience.

**[Play NetGuard Adventure in Your Browser!](https://corpus32.itch.io/netguard-adventure)**

---

## Gameplay Showcase

Check out the game in action! Watch the gameplay demonstration on YouTube:

**[NetGuard Adventure Gameplay!](https://www.youtube.com/watch?v=y_zCDHagSLc)**

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Installation & Requirements](#installation--requirements)
- [Usage](#usage)
- [Game Mechanics & Educational Logic](#game-mechanics--educational-logic)
- [Making](#making)

---

## Project Overview

NetGuard Adventure focuses on learning through interaction rather than passive instruction. Players control a character navigating levels filled with platforms, enemies, collectibles, and question triggers related to online safety.

### Educational Objectives

- Recognize phishing and scam attempts
- Understand safe password and account practices
- Learn how to react to suspicious online behavior
- Reinforce learning through hints, XP, and rewards

---

## How to Play

NetGuard Adventure features three distinct game modes, each offering unique mechanics and challenges.

### Easy Mode (Auto-Runner)
*Focus on timing and quick decision-making.*

* **Objective:** You move forward automatically. Jump over obstacles and collect coins. Reach the door at the end of the path to complete the level.
* **Controls:**
    * `SPACE` or `Arrow Key UP`: Jump
    * `S`: Open the Shop
    * `1, 2, 3`: Select answers for questions

### Normal Mode (Platformer)
*Classic exploration and enemy avoidance.*

* **Objective:** Navigate through platforms while avoiding enemies. Use the navy blue platforms for an extra bounce boost. Reach the door at the end of the stage to win.
* **Controls:**
    * `LEFT / RIGHT Arrows`: Move horizontally
    * `SPACE` or `Arrow Key UP`: Jump
    * `S`: Open the Shop
    * `1, 2, 3`: Select answers for questions

### Hard Mode (Vertical Climber)
*Advanced movement and precision.*

* **Objective:** Climb upward by jumping between platforms. Be careful, don't fall! Utilize your double jump and navy blue bounce platforms to reach the door at the very top.
* **Controls:**
    * `LEFT / RIGHT Arrows`: Move horizontally
    * `SPACE` or `Arrow Key UP`: Jump (**Double Jump enabled**)
    * `1, 2, 3`: Select answers for questions

---

## Features

### Core Gameplay Features

- Single-player platformer gameplay
- Multiple difficulty modes (Easy, Normal, Hard)
- State-based game flow (gameplay, questions, results)
- XP and coin reward system
- Hint system to support learning
- Sound effects and background music

### Educational Features

- Internet safety questions integrated into gameplay
- Immediate feedback on player choices
- Optional hints explaining correct behavior
- Progressive difficulty scaling across modes

---

## Project Structure

```
NetGuard-Adventure/
├── main.py              # Main game logic
├── assets/              # Static game resources
│   ├── images/          # Sprites, backgrounds, UI elements
│   ├── sounds/          # Music and sound effects
│   ├── fonts/           # Custom fonts
└── README.md            # Project documentation
```

---

## Installation & Requirements

### Prerequisites

- Python **3.9 or higher**

### Required Python Packages

```
pygame>=2.5
```

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/anamarijakraus/NetGuard-Adventure.git
cd NetGuard-Adventure
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install pygame
```

#### 4. Run the Game

```bash
python main.py
```

---

## Usage

### Playing the Game

**Option 1: Play in Browser (No Installation Required)**

Visit **[NetGuard Adventure on itch.io](https://corpus32.itch.io/netguard-adventure)** to play directly in your web browser!

**Option 2: Run Locally**

1. Run `main.py`
2. The main menu appears
3. Select a language (Macedonian or English)
4. Select a difficulty mode to begin playing

---

## Game Mechanics & Educational Logic

### Difficulty Modes

Each difficulty mode includes unique level layouts and question sets:

- **Easy** – Introductory internet safety concepts
- **Normal** – More realistic online scenarios
- **Hard** – Complex cybersecurity decision-making

### Question System

Questions are triggered by in-game objects. Each question includes multiple answers, with only one being correct.

**Correct answers:**
- Gives coins to later be used in the shop

**Incorrect answers:**
- Removes one life and encourages learning through hints

### Hint & Reward System

Hint objects can be collected during gameplay. Hints explain correct online behavior and collecting them grants:

- XP that unlocks a badge through progression and it's shown in the players profile

This system encourages exploration and learning without punishment.

---

## Making

This project was developed for the course **Video game programming** (PNVI) at the Faculty of Computer Science and Engineering (FINKI), Ss. Cyril and Methodius University, Skopje, Macedonia.

### Development Team

- **Ana Marija Kraus**
- **Stefan Lazarevski**

### Mentor

- **Katarina Trojachanec Dineva PhD**
- **Igor Goshev**

---
---

# NetGuard Adventure [MK]

NetGuard Adventure е 2D едукативна игра развиена во Python со користење на Pygame, дизајнирана да ги научи децата за безбедно однесување на интернет преку интерактивна игра, квизови и наградна прогресија.

Комбинира игри на платформа со прашања на тема сајбербезбедност, помагајќи им на играчите да научат како да донесуваат побезбедни одлуки онлајн додека напредуваат низ повеќе нивоа на тежина. Достапна на англиски и македонски јазик, играта обезбедува пристапност за разновидна публика.

**[Играјте NetGuard Adventure во вашиот прелистувач!](https://corpus32.itch.io/netguard-adventure)**

---

## Приказ на игра

Погледнете ја играта во акција со демонстрацијата на играта на YouTube:

**[NetGuard Adventure Gameplay!](https://www.youtube.com/watch?v=y_zCDHagSLc)**

---

## Содржина

- [Преглед на проектот](#преглед-на-проектот)
- [Карактеристики](#карактеристики)
- [Како да играте](#како-да-играте)
- [Структура на проектот](#структура-на-проектот)
- [Инсталација и барања](#инсталација-и-барања)
- [Користење](#користење)
- [Механики на игра и едукативна логика](#механики-на-игра-и-едукативна-логика)
- [Изработка](#изработка)

---

## Преглед на проектот

NetGuard Adventure се фокусира на учење преку интеракција, наместо пасивна настава. Играчите контролираат лик кој се движи низ нивоа исполнети со платформи, непријатели, предмети за собирање и прашања поврзани со безбедноста на интернет.

### Едукативни цели

- Препознавање на обиди за фишинг и измами
- Разбирање на безбедни практики за лозинки и сметки
- Учење како да се реагира на сомнително онлајн однесување
- Зајакнување на учењето преку совети, XP и награди

---

## Како да играте

NetGuard Adventure нуди три различни режими на игра, секој со уникатни механики и предизвици.

### Лесен режим (Auto-Runner)
*Фокус на тајминг и брзо одлучување.*

* **Цел:** Се движите напред автоматски. Скокате преку пречки и собирате парички. Стигнете до вратата на крајот на патот за да го завршите нивото.
* **Контроли:**
    * `SPACE` или `Стрелка ГОРЕ`: Скок
    * `S`: Отворете ја Продавницата
    * `1, 2, 3`: Изберете одговори на прашања

### Нормален режим (Платформер)
*Класично истражување и избегнување на непријатели.*

* **Цел:** Движете се низ платформите додека избегнувате непријатели. Користете ги темносините платформи за поголем скок. Стигнете до вратата на крајот на нивото за да победите.
* **Контроли:**
    * `Стрелки ЛЕВО / ДЕСНО`: Хоризонтално движење
    * `SPACE` или `Стрелка ГОРЕ`: Скок
    * `S`: Отворете ја Продавницата
    * `1, 2, 3`: Изберете одговори на прашања

### Тежок режим (Вертикално Качување)
*Напредно движење и прецизност.*

* **Цел:** Качувајте се нагоре скокајќи помеѓу платформите. Внимавајте, да не паднете! Искористете го двојниот скок и темносините платформи за поголем скок за да стигнете до вратата на самиот врв.
* **Контроли:**
    * `Стрелки ЛЕВО / ДЕСНО`: Хоризонтално движење
    * `SPACE` или `Стрелка ГОРЕ`: Скок (**Двоен скок овозможен**)
    * `1, 2, 3`: Изберете одговори на прашања

---

## Карактеристики

### Основни карактеристики на играта

- Игра за еден играч во платформер стил
- Повеќе нивоа на тежина (Лесно, Нормално, Тешко)
- Тек на игра базиран на состојби (игра, прашања, резултати)
- Систем за награди со XP и парички
- Систем на совети за поддршка на учењето
- Звучни ефекти и музика во позадина

### Едукативни карактеристики

- Прашања за безбедност на интернет интегрирани во играта
- Непосредна повратна информација за изборите на играчот
- Опционални совети кои го објаснуваат правилното однесување
- Прогресивно зголемување на тежината низ режимите

---

## Структура на проектот

```
NetGuard-Adventure/
├── main.py              # Главна логика на играта
├── assets/              # Статички ресурси на играта
│   ├── images/          # Спрајтови, позадини, UI елементи
│   ├── sounds/          # Музика и звучни ефекти
│   ├── fonts/           # Прилагодени фонтови
└── README.md            # Документација на проектот
```

---

## Инсталација и барања

### Предуслови

- Python **3.9 или повисоко**

### Потребни python пакети

```
pygame>=2.5
```

### Чекор-по-чекор инсталација

#### 1. Клонирајте го репозиториумот

```bash
git clone https://github.com/anamarijakraus/NetGuard-Adventure.git
cd NetGuard-Adventure
```

#### 2. Создадете виртуелна средина

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

#### 3. Инсталирајте зависности

```bash
pip install pygame
```

#### 4. Стартувајте ја играта

```bash
python main.py
```

---

## Користење

### Играње на играта

**Опција 1: Играјте во прелистувач (Без инсталација)**

Посетете **[NetGuard Adventure на itch.io](https://corpus32.itch.io/netguard-adventure)** за да играте директно во вашиот веб прелистувач!

**Опција 2: Стартувајте локално**

1. Стартувајте го `main.py`
2. Се појавува главното мени
3. Изберете јазик (Македонски или Англиски)
4. Изберете режим на тежина за да започнете со играње

---

## Механики на игра и едукативна логика

### Режими на тежина

Секој режим на тежина вклучува уникатен распоред на нивоа и збир на прашања:

- **Лесно** – Воведни концепти за безбедност на интернет
- **Нормално** – Пореалистични онлајн сценарија
- **Тешко** – Сложено одлучување во областа на сајбербезбедноста

### Систем на прашања

Прашањата се активираат од објекти во играта. Секое прашање содржи повеќе одговори, при што само еден е точен.

**Точни одговори:**
- Даваат парички кои подоцна можат да се користат во продавницата

**Неточни одговори:**
- Отстрануваат еден живот и го поттикнуваат учењето преку совети

### Систем на совети и награди

Предмети со совети можат да се соберат за време на играта. Советите го објаснуваат правилното онлајн однесување, а нивното собирање дава:

- XP кој преку прогресија отклучува значка прикажана во профилот на играчот

Овој систем ги поттикнува истражувањето и учењето без казнување.

---

## Изработка

Овој проект е развиен за курсот **Програмирање на видео игри** (PNVI) на Факултетот за компјутерски науки и инженерство (ФИНКИ), Универзитет „Св. Кирил и Методиј", Скопје, Македонија.

### Тим

- **Ана Марија Краус**
- **Стефан Лазаревски**

### Ментори

- **д-р Катарина Тројачанец Динева**
- **Игор Гошев**
