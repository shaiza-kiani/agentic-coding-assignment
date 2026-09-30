# <Pi>

## 1. What it is
Pi is an AI coding assistant used to understand and work with a software project. It was tested as part of the AI coding tools practical assignment.

## 2. Cost and access:
Pi was tested using the free route through OpenRouter.The free models were used because the assignment required testing an accessible/free option

## 3. Install and run (reproducible)
Pi was set up and successfully started.
```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```
pi --version 0.87.1

## 4. How it understands the codebase
Pi successfully completed the Understand step.
It inspected the project and provided a useful understanding of the existing codebase.
It also successfully read and followed the project's AGENTS.md instructions during the planning step.
## 5. Customization support
| Feature | Supported / Unsupported / Untested | Notes |
|---|---|---|
| Project instructions (AGENTS.md etc.) |Tested | Pi followed the project instructions during
| Skills | | |
| Plugins/extensions | | |
| MCP | | |

## 6. Practical task
Prompt:
Add a clear() method to Cart with a test. Show me your plan first. Follow AGENTS.md.
Pi successfully completed the planning/instruction stage, but the Change step did not complete.
The model returned an error twice while attempting to perform the change.
Result: Not completed.
Task 2: Fix the existing bug
The second practical task was to diagnose and fix the failing test:
test_adding_same_sku_increases_quantity
Pi did not reach the Debug/Change stage because the previous Change step had not succeeded.
Result: Not completed.
## 7. Permissions and approvals
Pi's interaction and model responses were observed during testing.
The failed Change attempts prevented a complete test of its editing and approval workflow.
## 8. Worked / failed / manual corrections
Worked
Pi was successfully set up using the free OpenRouter route.

It successfully understood the project.
It successfully read and followed AGENTS.md.
Its planning response provided useful information about the requested change.
Failed
The Change step failed twice with model errors.
Because Change did not complete, the Debug and Verify stages could not be completed.
No valid feature/fix commits were produced from the Pi workflow.
No before/after test evidence could be collected for the completed Pi task.
Manual corrections
No fabricated results were added after the failed attempts. The incomplete result is documented as a limitation of the tested free models.
Available evidence includes:
Pi setup evidence
Free-model/OpenRouter configuration
Model error responses
AGENTS.md instruction-following evidence
Successful Understand/planning response
Reflection
Pi showed that it can understand a project and follow repository-level instructions, but the tested free-model route was not reliable enough to complete the full coding workflow.
The main limitation was not the planning stage; it was the model failure during implementation. Because Change failed, there was no reliable way to continue to Debug and Verify.
## 9. Best use, limits, recommendation
Best use: Good for understanding a codebase, reading AGENTS.md, and making plans.
Limits: Free models failed during the Change step, so Debug and Verify could not be completed.
Recommendation: Useful for planning, but the tested free-model setup was not reliable enough for completing coding tasks.
