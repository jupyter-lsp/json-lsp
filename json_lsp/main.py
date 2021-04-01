import pathlib
import shutil

PATH_TO_BIN_JS = (
    pathlib.Path(__file__).parent /
    'node_modules' / 'vscode-json-languageserver-bin' / 'jsonServerMain.js'
)


def load(app):
    node = shutil.which("node")

    return {
        "json-language-server": {
            "version": 2,
            "argv": [node, str(PATH_TO_BIN_JS), "--stdio"],
            "languages": ["json"],
            "mime_types": [
                "application/json", "application/x-json", "application/ld+json"
            ]
        }
    }
