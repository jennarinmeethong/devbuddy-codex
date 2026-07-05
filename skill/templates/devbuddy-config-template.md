# devbuddy.config.md Template

Place this file at the project root (preferred, so it is committed and the project remembers its memory location) or next to `SKILL.md`. It overrides where DevBuddy memory lives.

Set at most one location key. `obsidian_vault` takes precedence over `memory_root`. With neither key, memory stays next to the installed skill (the default).

## obsidian_vault

Absolute path to an Obsidian vault. Memory is stored under `<obsidian_vault>/<obsidian_subfolder>` and written in Obsidian-native form (YAML frontmatter, `[[wikilinks]]` between memory files, and a per-project index note).

## obsidian_subfolder

Optional. Subfolder inside the vault for this project. Defaults to the project's directory name so multiple projects can share one vault without colliding.

```text
obsidian_vault: /Users/me/ObsidianVault
obsidian_subfolder: DevBuddy/MyProject
```

## memory_root

Path relative to the project root where memory files should be created and read. Use this for a non-Obsidian location inside the repo.

```text
memory_root: docs/devbuddy
```
