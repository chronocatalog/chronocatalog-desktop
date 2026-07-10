# PyInstaller build for the macOS app bundle.
# Build with: pyinstaller --noconfirm ChronoCatalog.spec

a = Analysis(
    ["src/chronocatalog_desktop/__main__.py"],
    datas=[("src/chronocatalog_desktop/resources", "chronocatalog_desktop/resources")],
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="ChronoCatalog",
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    name="ChronoCatalog",
)

app = BUNDLE(
    coll,
    name="ChronoCatalog.app",
    icon="assets/icon.icns",
    bundle_identifier="org.chronocatalog.desktop",
    info_plist={
        "CFBundleDisplayName": "ChronoCatalog",
        "NSHighResolutionCapable": True,
        "LSMinimumSystemVersion": "12.0",
    },
)
