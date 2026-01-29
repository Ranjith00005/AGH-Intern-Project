import json
import subprocess
import tempfile
from pathlib import Path

def load_js(path: str) -> list[str]:
    path = Path(path).resolve()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        js_runner = tmpdir / "convert.js"
        json_out = tmpdir / "out.json"

        js_runner.write_text(
            f"""
const fs = require("fs");
const data = require("{path.as_posix()}");
fs.writeFileSync("{json_out.as_posix()}", JSON.stringify(data, null, 2));
""",
            encoding="utf-8"
        )

        subprocess.run(
            ["node", str(js_runner)],
            check=True
        )

        with open(json_out, "r", encoding="utf-8") as f:
            data = json.load(f)

    if isinstance(data, dict):
        return [str(v) for v in data.values()]
    elif isinstance(data, list):
        return [str(v) for v in data]
    else:
        return [str(data)]
