# Skills
A skill is a saved set of instructions for one kind of job, like "review a
Python change" or "write a weekly report". It is usually a folder with a
main file (often called SKILL.md) that has a name, a short description and
the steps.

How it is found: the agent looks in its skills folders and reads only the
names and descriptions. It loads the full instructions only when the task
matches the description.

When a skill beats a plain prompt: when the same job comes up again and again,
needs several steps, or must always follow the same format. I write it once
and don't retype it.

Difference from AGENTS.md: AGENTS.md is rules for one project and is always
read. A skill can be used in many projects and is loaded only when needed.

Example (an idea I wrote, not tested): a "review-cart-change" skill with
these steps: read the diff, run pytest, check type hints, and list the risks.

Tested: I did not test a skill in this assignment.