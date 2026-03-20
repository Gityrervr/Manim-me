# 🎬 Manim Video Studio

Full Manim environment running in GitHub Codespaces.  
No local install needed. Works in browser. Persists between sessions.

---

## 🚀 Quick Start

1. Click the green **Code** button above
2. Click **Codespaces** tab
3. Click **Create codespace on main**
4. Wait ~5 min for setup (first time only)
5. Open any `.ipynb` notebook and start rendering!

---

## 📁 Folder Structure

```
manim-videos/
├── .devcontainer/
│   ├── devcontainer.json   ← Codespace config
│   └── install.sh          ← Auto-installs everything
├── scenes/
│   ├── thales.py           ← Thales Theorem scene
│   └── ies_q1to7.py        ← IES 1995 Q1-Q7 scenes
├── render.ipynb            ← Notebook to render scenes
└── README.md
```

---

## ▶️ How to Render a Scene

### Option 1 — Terminal
```bash
python -m manim -qh scenes/thales.py ThalesTheorem
```

### Option 2 — Notebook
Open `render.ipynb` and run the cells.

### Quality flags
| Flag | Quality | FPS |
|------|---------|-----|
| `-ql` | 480p   | 15  |
| `-qm` | 720p   | 30  |
| `-qh` | 1080p  | 60  |
| `-qk` | 4K     | 60  |

---

## 📺 Finding your video

After rendering, videos are saved to:
```
media/videos/<filename>/<quality>/
```

Right-click the `.mp4` in the file explorer → **Download**

---

## 🔁 Reopening Later

Go to **github.com/codespaces** → click your codespace.  
Everything is already installed. Opens in seconds.

---

## ✨ Tips

- **GitHub Copilot** is enabled — it autocompletes Manim code as you type
- Use `MathTex(r"\frac{a}{b}")` for proper fractions
- Use `always_redraw(lambda: ...)` for live-updating objects
- Use `ValueTracker` to animate numeric values smoothly
