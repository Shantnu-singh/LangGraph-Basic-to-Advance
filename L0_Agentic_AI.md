## GenAi 
- class of ai model that can generate new content like, text , img , audiom, code that resemble human-created data
- Example : Sore2 , Nano banana , ChatGpt , Codelamma , Elevenlabs , claude code

### GenAI vs Traditional AI
1) Traditional AI
- find patterns and giving prediction (Spam detection)
- solves problems like regression, classification, clusturing

2) GenAi
- try to learn distribution of data so it can generate new sample out of this
- best part, it mimic humans very well

### Application area
- creative and buisness writing (like in Gmail)
- software Devlopment ( generation , debugging)
- Customer Support
- Education (online education specially) : Doubt , personlised learning 
- Designing : graphics designers, thumbnails, Ads using Sora2 tools
- Used across industry, and it is constanly evolving and improving

### Limtation of tradition genai 
- can only generate not perform task
- has intelligence and reasoning but can't perform actions
- it is reactive not proactive
- doesn't have memory
- Generic text generation
- techniques like RAG can be used to slove some problems

### How Agentic AI can Solve these
- has tools so it can perform action also
- now it is proactivate
- can use intelliently tools 
- have contextual memory
- Is adpative
- A subset of GenAI

## Agentic AI
Example : a autonomus agent to hire a person in tech

### Key Characterstic
1) autonomous
- ability to make decison and make action without needed, step t step human instruction.
- it is proactivate
- autonomy in mutlifacts
a) Execution
b) Decision making
c) Tool Usages

#### Autonomy can be controlled by
- permission : limit what tools or action the agent can perform .
- Human in Loop: Insert checkpoint for human apprvals
- override control: Allow users tp stop, pause or change behaviours
- Guardrails/Policies : define hard rules and ethical boundries 

2) Goal oriented
- ai operate with persistent objectivte
- acts as compass for autonomy
- goals comes with constraints
- Goals are store in core memory
- Goals can be alterted

3) Planning
- agent ability to breakdown high level goals into structure sequence of action or subgoals

#### step 1 :
- generate mutiple candidate planss
#### step 2 :
- Evaluate each plan
    - efficinecy
    - Tools avaolibity
    - Cost
    - Risk
    - Alignment
#### step 3 :
- select the best plan with help of 
    - Human in Loop
    - A pre- programmed policy

4) Reasoning
- cognitivte ability for info interpration, draw conclusion and make decison, whole in planning and execution

#### Reasoning in Planning
- Goal decompostion
- Tool selction
- Resouce estimation: Estimation of time, dependices, risl

#### Reasoning in Execution
- DM making
- HITL handling: when to pause when to aks for help
- Error Handling: to handle failute

5) Adaptability
- ability to modify the plans, stratiges and action in responce to unexpected condition
- like in:
    - Failure(in APIs)
    - External feedback(Less no of application)
    - chnaging in Goals

6) COntext Awareness
- ability to understand, retain and use rrlevant info about task, past interation, user choice, and env

- Type of Context
    - Original Goal
    - Progress till Now
    - Env till Now
    - Tool responce
    - USer spcific prefrences
    - Policy and GuadeRails

- Have both short term and long term memory


## Core High Level component of Agents

1) Brains
- normally llm
- do planning, reasoning, tool secltion, communication

2) Orchestrator
- framework like Langgraogh
- task sequncing
- retry logic
- like manager

3) Tools
- exnternal action
- also Knowledge Base

4) Memory
- short term memory
- long term memory

5) supervisor
- Approval Request (HITL)
- Guaderails Enforcement
- Edge Case Excaltion: alert humans when conflict happens 
