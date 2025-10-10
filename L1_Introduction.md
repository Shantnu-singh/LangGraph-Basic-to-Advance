## Why Langgrapgh Exist
- for projects with complex flow digram (non-linear)
    - Have Loop
    - Have condition 
    - and have jump steps
- In Langchain need glue code, hard to maintain, for big projects

- In LangGrapgh we represtend workflow in grapgh as node(fucntion), so we can make complex workflow
- can add condition edges
- Requires less glue code

2) State Handling
- context throughtout the workflow, need to be maintained
- conexted need update, deletion and creation
- need to track state (Key values pair)
- Langchain doesn't have state, it is stateless. we have to maintain it though glue code

- LG is stateful, all the node can aceess state(dict), and all the not is muttbale bu each node

3) Event Driven execution (Task execute after a external trigger happnes)
- LC does't suppourt this, it only have Sequential Execution (A chain when start, will end )
- LG nativey suppuort this, using checkpoint to store the states and then resuming it where we left

4) Fault Torlerance
- Need to long running workflow
- Small Fault (node level, api error)
- Large Fault(system level, EC2 server crash)
- LG Built in Fault Torlerance, 
    - Retry logic (small)
    - Recovery(using checkpointer)

5) Human in a Loop
- workflow need human approval (critcal point need this)
- LC doesn't have this, naitively
- LG is first class features 
- Using checkpointer and Sates

6) Nested workflow
- for workflow that need more complex workig
- each node can a simple task, or a workflow on it's own
- subgraph, a gragh that themselve a npde
- can created mutliagent systems
- can make reusebale workflow, that we can use in many places

7) observablikty
- refer to how easily you can moniter, debug and understand what you workflow is doing it runetime.
- for this we use, LangSmith(Can't understand glue code)
- very tight, bith LG and LS is connected
