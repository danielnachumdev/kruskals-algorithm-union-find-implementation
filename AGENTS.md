# Kruskal’s algorithm – Agent Context

Implementation guide for coding agents changing **kruskals-algorithm-union-find-implementation**. Product pitch and user-facing usage: [`README.md`](README.md).

---

## Orientation

| Question | Answer |
| -------- | ------ |
| What is this? | Educational **Kruskal MST** in Python with a custom **union-find** |
| Entry / API | `Main.kruskals_algorithm`, `Main.generate_random_graph`; types in `Node.py`, `Edge.py` |
| Toolchain | Plain Python stdlib (no `pyproject.toml` / uv / pip deps on `main`) |
| Python | Uses `list[...]` annotations → treat as **3.9+** |
| Tests | `test_1.py` (script with `if __name__ == '__main__'`, not pytest discovery) — **never delete** |
| Secrets | None expected; do not invent credentials |

```text
.
├── .github/          # Optional: CODEOWNERS, dependabot, thin CI (shared actions)
├── Node.py           # Vertex
├── Edge.py           # Weighted undirected edge
├── Main.py           # Kruskal + union-find + random graph
├── test_1.py         # Random-graph MST size smoke test
├── README.md         # Marketing / user docs
└── AGENTS.md         # This file
```

Default branch: **`main`**.

Shared CI/CD (when workflows are present): [`danielnachumdev/actions`](https://github.com/danielnachumdev/actions) (`@latest`, `standards-ref: latest`). How to adopt: [`HOW-TO-USE.md`](https://github.com/danielnachumdev/actions/blob/v1/HOW-TO-USE.md). Thin CI may use `allow-empty: true` or a custom test command until a pytest suite exists.

---

## Develop

```bash
python test_1.py
# or import interactively
python -c "from Main import generate_random_graph, kruskals_algorithm; g=generate_random_graph(10,3); g[1]=sorted(g[1], key=lambda e: e.weight); print(len(kruskals_algorithm(g)))"
```

| Task | Command / note |
| ---- | -------------- |
| Smoke | `python test_1.py` |
| Types / lint | Not configured on `main` |
| Package install | N/A — run from repo root so `from Node import Node` resolves |

---

## Domain notes

- **Graph shape:** callers pass `[nodes, edges]` (`list[Node]`, `list[Edge]`). The name `graph` in `Main.py` is a type alias used in annotations.
- **Sort before Kruskal:** `kruskals_algorithm` does **not** sort. Callers (including `test_1.py`) must `sorted(..., key=lambda x: x.weight)`. Changing that contract requires updating README, tests, and any call sites together.
- **Union-find:** `make_sets` builds `indexers` (node → int), `pointers`, and `sets`. `find` / `union` are O(1) via those arrays — not classical path-compression / union-by-rank. Preserve the comment contract if you refactor.
- **Stop early:** loop stops when `|MST| == |V| - 1`. Disconnected inputs yield fewer edges; the smoke test assumes enough random edges for a tree.
- **`Edge`:** undirected equality (`src/dst` swap counts as equal). Constructor rejects `src == dst`. `fromString` parses `"N0 -> N1 (1.0)"`-style text.
- **`generate_random_graph`:** dedupes undirected pairs by `(min_idx, max_idx)`; requires `node_count > 1` and `edge_to_node_ratio > 0`.
- Keep this a **stdlib-only** teaching sample unless the user explicitly asks for packaging or a graph library.

---

## PRs, CI, and releases

1. Branch off `main`; open a PR into `main`.
2. Attach **exactly one** semver label: `noBump` | `bumpPatch` | `bumpMinor` | `bumpMajor`.
3. Docs-only / agent-context changes → **`noBump`**.
4. When CI exists: prefer required checks **`CI / CI`** and **`Semver / Semver`** from thin orchestrators calling `danielnachumdev/actions`.
5. Dependabot PRs stay on `noBump`.
6. Change shared CI/semver behavior in **`danielnachumdev/actions`**, not by re-vendoring here.

This repo is **not** a PyPI package — no semver-cd / publish path unless explicitly added later.

---

## Sensitive / ignored

Do not commit: `.venv/`, `venv/`, `__pycache__/`, API keys, or local secrets. Prefer adding a `.gitignore` if missing when touching tooling.
