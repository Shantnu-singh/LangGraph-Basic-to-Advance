## Why Langgrapgh When we had Langchain
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


## LangGraph Core Concepts
- orchestration framework to create intelligent and, stateful and multi-step workflow

1) LLM workflow: series of Taks for exection, that use LLM in sometask
- Common workflows 
    - Promt Chaining (e.g: topic->outline->detail report)
    - Routing, (use as Decision making, and then execute based on that )
    - Pareallization (task ->subtask, and run subtask parallel), like youtube content Moderation
    - Orchestrator (task-> multi parellel subtask), but each subtask work is not predefined
    - Evaulater optimizer (have Generator LLM and Evaulater LLM, until Evaluter satstified), norally use to creative things

2) Gragh, Node and Edge
- each taks can ne a node (python fuction) and the whole workflow can be represted as graph
- edges tell use, how node are connected (sequentail, parellel, branching and Loops)

3) State
- for LLM workflow we need some data throughout the execution, 
- State is Dict (key-values pair) that have all the data for LLM workflow and it pass through all the nodes
- State is shared and mutubale for each Node

4) Reducers
- for workflow like chatbot mutubale states is bad things
- Reducers define how a state will change by nodes
- Each key can have it's own reducer

5) LangGrapgh Execution Model
- inpired from Google pregel
- Step 1: Grapgh Deficntion
    - state, Nodes and edges
- Step 2:Complilation
.compile(), check for structure of graph

- step 3: Invocation
- run the graph
- send intital state to first Node

- Step 4: Super step began
- internmediate Nodes

- step 4 : terminate
- last node gets state, and things terminate
