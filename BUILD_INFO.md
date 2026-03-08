# Build Information

## Build Details

- **Build Date**: March 8, 2026
- **Build Type**: Windows Standalone Executable
- **Package Size**: 32.55 MB
- **Python Version**: 3.11.9
- **Build Tool**: PyInstaller 6.19.0

## Package Contents

```
UnpakRacing-Windows/
├── UnpakRacing.exe          # Main executable (32.08 MB)
├── README.md                # Full documentation (10.68 KB)
├── QUICK_START.txt          # Quick start guide
├── gameplay_assets/         # Game sprites
│   ├── car.png              # Player car texture
│   ├── enemy.png            # Enemy car texture
│   └── road.png             # Road tile texture
└── gui_assets/              # UI resources
    ├── home_bg.gif          # Home screen background (1.4 MB)
    ├── settings_bg.gif      # Settings screen background
    ├── mbim.png             # Mascot image
    ├── unpak_racing_logo.png
    ├── unpak_racing_icon.ico
    └── font/
        ├── Knewave-Regular.ttf
        └── OFL.txt
```

## Build Command

```bash
pyinstaller --onefile --windowed \
  --icon=gui_assets/unpak_racing_icon.ico \
  --add-data "gui_assets;gui_assets" \
  --add-data "gameplay_assets;gameplay_assets" \
  --name UnpakRacing \
  main.py
```

## Distribution Package

**File**: `UnpakRacing-Windows.zip` (32.55 MB)

This ZIP contains:
- Standalone executable (no Python installation required)
- All game assets
- Complete documentation
- Quick start guide

## Installation Instructions for End Users

1. Extract `UnpakRacing-Windows.zip`
2. Run `UnpakRacing.exe`
3. Enjoy the game!

No additional dependencies or installations required.

## Build Environment

- **OS**: Windows 10
- **Virtual Environment**: .venv (Python 3.11.9)
- **Dependencies**:
  - ursina (game engine)
  - pyinstaller (build tool)

## Notes

- The executable is self-contained and includes Python runtime
- Assets are embedded but also included externally for debugging
- Icon successfully embedded in the executable
- Windowed mode (no console window)
- All imports and dependencies resolved successfully

## Testing Checklist

Before release, ensure:
- [x] Executable builds without errors
- [x] All assets properly included
- [x] Icon displays correctly
- [x] No console window appears
- [ ] Game launches and runs smoothly
- [ ] All game features work (menu, gameplay, settings, game over)
- [ ] Controls respond correctly
- [ ] Collision detection functions
- [ ] Game over and retry work

## Known Build Artifacts

The following temporary build files were created (not included in distribution):
- `build/` - Intermediate build files
- `UnpakRacing.spec` - PyInstaller spec file
- `dist/UnpakRacing.exe` - Original executable (before packaging)

These can be safely deleted or ignored by end users.
