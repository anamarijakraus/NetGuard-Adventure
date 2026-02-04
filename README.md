# NetGuard Adventure

NetGuard Adventure is a 2D educational game developed in Python using Pygame, designed to teach children about safe internet behavior through interactive gameplay, quizzes, and reward-based progression.

The game combines classic platform mechanics with cybersecurity-themed questions, helping players learn how to make safer online decisions while advancing through multiple difficulty modes. Available in English and Macedonian, the game ensures accessibility for a diverse audience.

 **[Play NetGuard Adventure in Your Browser!](https://corpus32.itch.io/netguard-adventure)**

---

##  Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Requirements](#installation--requirements)
- [Usage](#usage)
- [Game Mechanics & Educational Logic](#game-mechanics--educational-logic)
- [Contributors & Acknowledgments](#contributors--acknowledgments)

---

##  Project Overview

NetGuard Adventure focuses on learning through interaction rather than passive instruction. Players control a character navigating levels filled with platforms, enemies, collectibles, and question triggers related to online safety.

### Educational Objectives

- Recognize phishing and scam attempts
- Understand safe password and account practices
- Learn how to react to suspicious online behavior
- Reinforce learning through hints, XP, and rewards

---

##  Features

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

##  Project Structure

```
NetGuard-Adventure/
├── main.py              # Main game logic
├── assets/              # Static game resources
│   ├── images/          # Sprites, backgrounds, UI elements
│   ├── sounds/          # Music and sound effects
│   ├── fonts/           # Custom fonts
└── README.md            # Project documentation
```

### Key Components

#### `main.py`

Responsible for:

- Game initialization and configuration
- Game state handling
- Player movement and physics
- Collision detection
- Question and hint logic
- XP and coin tracking
- Rendering UI elements and popups

---

##  Installation & Requirements

### Prerequisites

- Python **3.9 or higher**

### Required Python Packages

```
pygame>=2.5
```

---

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anamarijakraus/NetGuard-Adventure.git
cd NetGuard-Adventure
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

```bash
pip install pygame
```

### 4. Run the Game

```bash
python main.py
```
---

##  Usage

### Playing the Game

**Option 1: Play in Browser (No Installation Required)**

Visit **[NetGuard Adventure on itch.io](https://corpus32.itch.io/netguard-adventure)** to play directly in your web browser!

**Option 2: Run Locally**

1. Run `main.py`
2. The main menu appears
3. Select a language (Macedonian or English)
4. Select a difficulty mode to begin playing

---

##  Game Mechanics & Educational Logic

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

##  Contributors & Acknowledgments

This project was developed for the course **Video game programming** (PNVI) at the Faculty of Computer Science and Engineering (FINKI), Ss. Cyril and Methodius University, Skopje, Macedonia.

### Development Team

- **Ana Marija Kraus**
- **Stefan Lazarevski**

### Mentor

- **Katarina Trojachanec Dineva PhD**
