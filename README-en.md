# 📔 Today's Self Journal

> **Record your day in one line, and AI will read your emotions**
>
> A warm, pastel-toned emotional journal app to explore your inner self.

---

## 🎯 Project Overview

**'Today's Self Journal'** is an **emotional journal app** that analyzes your feelings and asks reflective questions when you record your day in a single line.

Beyond simple journaling, it offers **3-level reflective questions** to help you understand your emotions on a deeper level.

### ✨ Key Features

- 🎭 **6 Emotion Recognition**: Confusion, Avoidance, Achievement, Anticipation, Anxiety, Serenity
- 💬 **3-Level Reflective Questions**: Surface → Meaning → Existential inquiry
- 🎨 **3 Tone Choices**: Pastel (warm) / Poetic (metaphorical) / Philosophical (deep)
- 📊 **Emotion Trend Tracking**: Weekly emotion flow & pattern analysis
- 💾 **Local Storage**: Privacy-first (no cloud upload)
- 🤖 **AI-Powered Analysis**: Groq Llama model (extensible)

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Lunorsun/mcp-realtime-chainlit.git
cd mcp-realtime-chainlit

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file with your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-2-13b-chat
```

Get your Groq API key from [Groq Console](https://console.groq.com).

### Run

```bash
chainlit run journal_ui.py
```

Open `http://localhost:8000` in your browser.

---

## 📖 Usage Guide

### 1️⃣ Getting Started

When you open the app, you'll see **tone selection** buttons:

- **Warm & Gentle (Default)**: Comforting, supportive questions
- **Poetic & Metaphorical**: Lyrical expressions of emotions
- **Deep & Philosophical**: Existential meaning exploration

### 2️⃣ Record Your Emotion

Write one line about your day:

```
Examples:
"I felt so proud today because I completed my project"
"I was really nervous about the exam at school"
"I enjoyed peaceful time alone at home"
```

### 3️⃣ View Analysis Results

After input, you'll see **4 cards**:

#### 📌 Card 1: Today's Emotion Signature
```
○ Confusion
●●○○○
Direction: Internal
```
- Emotion type
- Intensity (1-5)
- Direction (Internal/External)

#### 📌 Card 2: Daily Event Flow
```
• I had a project meeting at work
  - Location: Office | Cause: Meeting
• I was alone at home relaxing
  - Location: Home | Cause: Rest
```

#### 📌 Card 3: Reflective Questions (3-Level)
```
1. What was the gentlest thought in your heart today?
2. What comfort was that thought trying to give you?
3. What small thread led you to this very moment?
```

#### 📌 Card 4: Epilogue + Recommendation
```
**Epilogue**: Today you gently reached out to your heart...

**Advice**: Anxiety is just your way of protecting yourself. 
Take a deep breath and notice it's okay to feel this way.
```

### 4️⃣ Use Commands

#### `/help`
View all features and how to use them.

#### `/weekly`
Get this week's emotion summary.

#### `/flow`
Visualize your recent 5-emotion flow.

#### `/insight`
Get personalized weekly insights.

#### `/tone_change`
Re-select the question tone.

---

## 🔍 Emotion Classification

The app recognizes **6 emotions**:

| Emotion | Icon | Description |
|---------|------|-------------|
| **Achievement** | ◆ | Joy of reaching goals |
| **Anticipation** | ▲ | Positive future outlook |
| **Anxiety** | ▼ | Fear of uncertainty |
| **Serenity** | ★ | Inner peace & stability |
| **Avoidance** | ● | Fleeing from difficulty |
| **Confusion** | ○ | Direction lost |

---

## 🛠️ Technology Stack

- **Framework**: Chainlit (Web UI)
- **Language**: Python 3.12+
- **AI Model**: Groq Llama-2-13b-chat
- **Storage**: Local JSON

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

**Explore your inner self with Today's Self Journal 🌙**

