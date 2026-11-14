#!/usr/bin/env python3
"""Export selected repository skills to a Codex workspace, without overwriting existing skills."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]


def select_skills(names, category):
    available = {p.parent.name: p.parent for p in ROOT.glob("*/SKILL.md") if not p.parent.name.startswith("_")}
    if names:
        missing = sorted(set(names) - available.keys())
        if missing:
            raise ValueError("Unknown skill(s): " + ", ".join(missing))
        selected = [available[name] for name in sorted(set(names))]
    else:
        selected = list(available.values())
    if category and category != "all":
        selected = [p for p in selected if re.search(r"^category:\s*['\"]?" + re.escape(category) + r"(?:['\"]?\s*(?:#.*)?)?$", (p / "SKILL.md").read_text(), re.M)]
    if not selected:
        raise ValueError("No skills match the selection.")
    return sorted(selected)


def export_skills(selected, destination, dry_run=False):
    destination = Path(destination).resolve()
    protected = (Path.home() / ".codex" / "skills" / "remote-skills").resolve()
    if destination == protected or protected in destination.parents:
        raise ValueError("Use the supported personal-skill flow for personal ChatGPT skills.")
    conflicts = [p.name for p in selected if (destination / p.name).exists()]
    if conflicts:
        raise ValueError("Existing skills are preserved; choose an empty destination: " + ", ".join(conflicts))
    if not dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        for source in selected:
            target = destination / source.name
            shutil.copytree(source, target)
            shutil.copy2(ROOT / "MODEL_POLICY.md", target / "MODEL_POLICY.md")
            shutil.copy2(ROOT / "model-policy.json", target / "model-policy.json")
            manifest = {
                "source_root": str(ROOT.resolve()),
                "source_skill": str(source / "SKILL.md"),
                "source_skill_sha256": hashlib.sha256((source / "SKILL.md").read_bytes()).hexdigest(),
                "standalone": False,
                "required_working_directory": str(ROOT.resolve()),
                "dependency_rule": "Keep the complete source checkout. Resolve knowledge, scripts, and cross-skill paths from source_root. Stop if missing or changed until reverified."
            }
            (target / "SOURCE.json").write_text(json.dumps(manifest, indent=2) + "\n")
            skill_file = target / "SKILL.md"
            text = skill_file.read_text()
            boundary = text.index("\n---", 4) + 4
            text = text[:boundary] + "\n\n## Required source context\n\nRead SOURCE.json first. This export requires the complete source checkout recorded there; it is not standalone. Run repository examples and resolve knowledge, scripts, and cross-skill references from its source_root, not this exported directory. Verify the recorded source-skill hash before use; stop affected steps if the checkout or dependencies are unavailable.\n" + text[boundary:]
            skill_file.write_text(text)
    return [str(destination / p.name) for p in selected]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", action="append", help="Exact skill name; may be repeated.")
    parser.add_argument("--category", "-c")
    parser.add_argument("--dir", "-d", type=Path, default=Path.cwd() / ".agents" / "skills")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        paths = export_skills(select_skills(args.skill, args.category), args.dir, args.dry_run)
    except ValueError as exc:
        parser.error(str(exc))
    print("\n".join(paths))
    print(f"{'Selected' if args.dry_run else 'Exported'} {len(paths)} workspace skills; retain the full source checkout. These exports are not standalone. Personal ChatGPT installation and the active host model are separate.")


if __name__ == "__main__":
    main()
