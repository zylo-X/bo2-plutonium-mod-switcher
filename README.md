# 🎮 Black Ops 2 Plutonium Mod Switcher

<div align="center">

![GitHub release](https://img.shields.io/github/v/release/zylo-X/bo2-plutonium-mod-switcher?style=for-the-badge)
![Downloads](https://img.shields.io/github/downloads/zylo-X/bo2-plutonium-mod-switcher/total?style=for-the-badge)
![License](https://img.shields.io/github/license/zylo-X/bo2-plutonium-mod-switcher?style=for-the-badge)

**Effortlessly switch between Black Ops 2 Plutonium mods without the hassle!**

*No more manual file copying, no more lost scripts, no more mod conflicts.*

[🚀 Download Latest Release](../../releases/latest)      • [🐛 Report Issues](../../issues)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔍 **Smart Auto-Detection**
- Automatically finds your Plutonium installation
- No manual path configuration needed
- Intelligent folder scanning

### 🖱️ **One-Click Switching**
- Simple, intuitive interface
- Switch mods with a single click
- Real-time mod status display

</td>
<td width="50%">

### 💾 **Safe & Reliable**
- Never lose your original files
- Clean folder management
- Automatic backup handling

### ⚡ **Lightweight & Fast**
- Single executable file
- No installation required
- Minimal system resources

</td>
</tr>
</table>

---

## 🎯 What This Tool Does

Fed up with manually copying and pasting `scripts` and `images` folders every time you want to switch mods? This tool **automates the entire process** for you!

### Before (Manual Process) 😫
```
1. Navigate to your Plutonium folder
2. Move current (original) scripts/images to a folder called original,Unmodded , anyname you want .....
├── 📁 Original/                 ← Your original files ⭐
│   ├── 📁 scripts/
│   └── 📁 images/
3. Copy mod folder contain mod's files; scripts/images 
├── 📁 ColdWar-Zombies/          ← Your mod
│   ├── 📁 scripts/
│   └── 📁 images/
4. Hope you didn't mess something up
```

### After (With Mod Switcher) 😎
```
1. Run mod_switcher.exe
2. Select your desired mod
3. Click "Switch Mod"
4. Done! 🎉
```

---

## 📁 Directory Structure

Your Plutonium directory should be organized like this:

```
📂 %localappdata%/Plutonium/storage/t6/
├── 🔧 mod_switcher.exe          ← Place the app here
├── 📁 scripts/                  ← Active mod files
├── 📁 images/                   ← Active mod files
├── 📁 Original/                 ← Your vanilla/original files ⭐
│   ├── 📁 scripts/
│   └── 📁 images/
├── 📁 ColdWar-Zombies/          ← Your first mod 
│   ├── 📁 scripts/
│   └── 📁 images/
├── 📁 Multiplayer-Bots/         ← Your second mod
│   ├── 📁 scripts/
├── 📁 Custom-Camos/              ← Your third mod
│   └── 📁 images/
├── 📁 demos/
├── 📁 main/
├── 📁 mods/
└── 📁 ... (other game folders)
```

> ⚠️ **Important:** Create a backup folder (e.g., `Original`, `Backup`) containing your original `scripts` and `images` folders before using any mods!

---

## 🚀 Installation & Usage

### For Regular Users (Recommended)

#### **Step 1: Download**
- 📥 [Download the latest `mod_switcher.exe`](../../releases/latest) from the Releases page
- The exe file is ready-to-use, no installation needed!

#### **Step 2: Setup**
1. prefered : Place `mod_switcher.exe` in your Plutonium directory:  
   `%localappdata%/Plutonium/storage/t6/`
  otherwise : since the app have path browser and autodetect it should be ok to place it in any directory

2. Organize your mods in separate folders (see [Directory Structure](#-directory-structure))

3. **Create a backup** of your original files in a folder named `Original` or anyname you want

#### **Step 3: Run & Switch**
1. 🖱️ Double-click `mod_switcher.exe`
2. 🔍 The app will auto-detect your game directory
3. 📋 Select your desired mod from the list
4. ⚡ Click **"Switch Mod"** button
5. ✅ Enjoy your mod!

<div align="center">

*Screenshot of the application interface*

<img width="622" height="595" alt="main" src="https://github.com/user-attachments/assets/b8b0e62c-c9ac-4fa2-8416-ed610c5c003b" />


</div>

---

### For Developers

If you want to modify the source code or contribute:

#### **Requirements**
```bash
pip install PyQt6
```

#### **Run from Source**
```bash
python mod_switcher.py
```

#### **Build Executable**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed mod_switcher.py
```

---

## 🛡️ Safety Features

- ✅ **Automatic Backup Detection**: Warns if no backup folder exists
- ✅ **Path Validation**: Ensures valid game directory selection
- ✅ **Error Handling**: Graceful handling of file operations
- ✅ **Conflict Prevention**: Clean removal before copying new files
- ✅ **Status Tracking**: Always shows currently active mod

---

## 🐛 Troubleshooting

<details>
<summary><b>❌ Auto-detection failed</b></summary>

- Click the **"Browse"** button and manually navigate to:  
  `C:\Users\[YourUsername]\AppData\Local\Plutonium\storage\t6\`
- Make sure the folder contains your mod directories

</details>

<details>
<summary><b>❌ No mods showing in the list</b></summary>

- Ensure each mod folder contains either a `scripts` or `images` subfolder
- Check that folder names don't contain special characters
- Verify you're not placing mods in the `raw` folder (it's ignored)

</details>

<details>
<summary><b>❌ Permission denied errors</b></summary>

- Run the application as Administrator
- Ensure the game is not running while switching mods
- Check that files are not read-only

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- 🐛 [Report bugs](../../issues/new?template=bug_report.md)
- 💡 [Suggest features](../../issues/new?template=feature_request.md)
- 🔧 Submit pull requests
- 📖 Improve documentation
- ⭐ Star the repository

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ❤️ Support

If this tool saved you time and hassle, consider:
- ⭐ Starring this repository
- 🐛 Reporting any issues you find
- 📢 Sharing with the Plutonium community

---

<div align="center">

**Made with ❤️ for the Black Ops 2 Plutonium Community**.
---
This tool was created by **Zylo_X Studios**.
---
*Happy modding! 🎮*

</div>
