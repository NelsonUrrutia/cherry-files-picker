# 🍒 Cherry Files Picker CLI 🗂️

> **Cherry Files Picker CLI** is a tool designed to move files from a source branch to a target branch and create a single, clean commit

## The idea

I often encountered a scenario where a file or several files were modified across multiple commits. And by the time they where ready to push to production, I had to manually select all the commits related to those files, to `cherry pick` them and merge them into production.

Then, I realized what I really wanted was the final result, the approved code version of the files, not the detailed history of commits.

Cherry Files Picker CLI draws inspiration from Git's `cherry pick` command but with a different goal. The core idea of the project is to **emphasizes data over history**.

Yes, there're probably git commands that can achieve similar results, and maybe I'm just to lazy to search them.
Nevertheless my goal with this project is to improve my workflow, create a useful tool and feel accomplishment from the fact of having an idea and make it a reality.

## How it works

### Requirements

- Git
- Python

### Workflow

> **Note** use `Control + c` command to stop the process at execution time

1. **Start the tool**
   Run the command within your Git repository:

```
  cherry-files-picker
```

2. **Select branches**
   The tool prompts for:

- _Source branch_: the branch containing the approved versions of the files.
- _Target branch_: the branch that will receive the changes.

Both branches are validated to ensure they exist locally.

3. **Select files**
   You are asked to enter one or more file paths.

- Each path is validated against the source branch.
- Only existing files are accepted.

4. **Prepare the commit**
   The tool asks for:

- A commit title
- A commit description

These will be used to create a single commit in the target branch.

5. **Review and apply**
   A summary is displayed, showing:

- Source branch
- Target branch
- Selected files
- Commit message

After confirmation, the tool checks out into the target branch, applies the files, and creates the commit.

## Distribution and installation

For the time been the tool is distributed as a **source-based tool**.
The project is intended to be used by cloning the repository and installing it in editable mode.

After cloning the repo in your machine, open the project directory and run:

```
  pipx install -e .
```

OR

```
  pip install -e .
```

This makes the `cherry-files-picker` command available globally.

#### To uninstall, run:

```
  pipx uninstall cherry-files-picker
```

OR

```
  pip uninstall cherry-files-picker
```

## Considerations

- **Local-only operations**: it does not execute commands like `git pull`, `git push`, or any remote interactions. Managing remotes is your responsibility.

- **Immediate file replacement**: files in the target branch are instantly replaced by the source branch's versions. The tool does not include merge logic or conflict resolution beyond Git's native defaults.

## Future ideas

These are potential enhancements, not part of the current scope:

- Publish it on [PyPi](https://pypi.org/)
