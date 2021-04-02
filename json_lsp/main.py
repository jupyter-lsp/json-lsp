import pathlib
import shutil
import subprocess
import sys


NODE_LOCATION = (
    shutil.which("node") or
    shutil.which("node.exe") or
    shutil.which("node.cmd")
)
NODE = str(pathlib.Path(NODE_LOCATION).resolve())
PATH_TO_BIN_JS = str(
    (
        pathlib.Path(__file__).parent /
        'node_modules' / 'vscode-json-languageserver-bin' /
        'jsonServerMain.js'
    ).resolve()
)


def main():
    p = subprocess.Popen(
        [NODE, PATH_TO_BIN_JS, '--stdio', *sys.argv[1:]],
        stdin=sys.stdin, stdout=sys.stdout
    )
    sys.exit(p.wait())


def load(app):
    return {
        "json-language-server": {
            "version": 2,
            "argv": ['json-lsp'],
            "languages": ["json"],
            "mime_types": [
                "application/json", "application/x-json", "application/ld+json"
            ]
        }
    }


if __name__ == "__main__":
    main()
