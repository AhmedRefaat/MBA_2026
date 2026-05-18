# Lec-5 Groups and Managing Teamwork


## Stages og Group Development 

```mermaid
flowchart LR
    subgraph S1["🟢 STAGE 1\nFORMING"]
        direction TB
        A1["👥 Members meet\nfor first time"]
        A2["❓ Uncertainty\n& ambiguity"]
        A3["🎯 Goal Setting\n🧩 Role Definition\n🤝 Relationship Building\n📋 Procedural Framework"]
        A4["👔 Leader:\n• Team-building activities\n• Clarify goals\n• Open communication\n• Build trust"]
        A1 --> A2 --> A3 --> A4
    end

    subgraph S2["⚡ STAGE 2\nSTORMING"]
        direction TB
        B1["💥 Conflicts &\ndisagreements arise"]
        B2["⚔️ Disputes\n😤 Resistance\n🏋️ Role negotiation"]
        B3["👔 Leader:\n• Safe space for expression\n• Constructive conflict resolution\n• Facilitate harmony\n• Maintain morale"]
        B1 --> B2 --> B3
    end

    subgraph S3["🔄 STAGE 3\nNORMING"]
        direction TB
        C1["🤝 Conflict → Cohesion"]
        C2["✅ Acceptance & Alignment\n🫱🏼‍🫲🏽 Cooperation & Trust\n📏 Shared Norms"]
        C3["👔 Leader:\n• Facilitate norms\n• Clarify roles\n• Encourage accountability"]
        C1 --> C2 --> C3
    end

    subgraph S4["🚀 STAGE 4\nPERFORMING"]
        direction TB
        D1["⚡ Peak productivity\n& effectiveness"]
        D2["🎯 Goal achievement\n🧠 Autonomous work\n🔄 Flexible roles\n💡 Innovation"]
        D3["👔 Leader:\n• Delegate & empower\n• Remove obstacles\n• Foster innovation\n• Monitor progress"]
        D1 --> D2 --> D3
    end

    subgraph S5["🏁 STAGE 5\nADJOURNING"]
        direction TB
        E1["👋 Project wrapping up"]
        E2["📦 Task completion\n🪞 Reflection\n🚪 Disbanding\n🏆 Recognition"]
        E3["👔 Leader:\n• Structured transition\n• Document lessons\n• Acknowledge contributions\n• Best practices"]
        E1 --> E2 --> E3
    end

    S1 ==> S2 ==> S3 ==> S4 ==> S5

    style S1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#1b5e20
    style S2 fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c
    style S3 fill:#e8eaf6,stroke:#283593,stroke-width:3px,color:#1a237e
    style S4 fill:#e0f7fa,stroke:#00695c,stroke-width:3px,color:#004d40
    style S5 fill:#ede7f6,stroke:#4527a0,stroke-width:3px,color:#311b92
    style A1 fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20
    style A2 fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20
    style A3 fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style A4 fill:#81c784,stroke:#2e7d32,color:#1b5e20
    style B1 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style B2 fill:#ffcc80,stroke:#e65100,color:#bf360c
    style B3 fill:#ffb74d,stroke:#e65100,color:#bf360c
    style C1 fill:#c5cae9,stroke:#283593,color:#1a237e
    style C2 fill:#9fa8da,stroke:#283593,color:#1a237e
    style C3 fill:#7986cb,stroke:#283593,color:#1a237e
    style D1 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style D2 fill:#80cbc4,stroke:#00695c,color:#004d40
    style D3 fill:#4db6ac,stroke:#00695c,color:#004d40
    style E1 fill:#d1c4e9,stroke:#4527a0,color:#311b92
    style E2 fill:#b39ddb,stroke:#4527a0,color:#311b92
    style E3 fill:#9575cd,stroke:#4527a0,color:#311b92
```

### Stage-1 Forming

```mermaid
mindmap
  root((🟢 **FORMING**<br/>Stage 1))
    **Characteristics**
      Uncertainty & Ambiguity
      Cautious & Polite members
      Exploring purpose & structure
    **Key Features**
      🎯 Goal Setting
        Clear objectives
      🧩 Role Definition
        Assign responsibilities
      🤝 Relationship Building
        Trust & cooperation
      📋 Procedural Framework
        Rules & processes
    **Team Leader Role**
      🏗️ Team-Building Activities
        Workshops & ice-breakers
        Share backgrounds & skills
      📌 Clarify Goals & Expectations
        Define objectives & outcomes
        Each member knows their role
      💬 Open Communication
        Safe space for concerns
        Collaboration tools setup
      🤝 Build Trust & Cooperation
        Model cooperative behavior
        Collaboration over ego
    **Completion Marker**
      Members see themselves<br/>as part of a cohesive group
```

```mermaid
flowchart TB
    subgraph STAGE["🟢 STAGE 1 — FORMING"]
        direction TB
        A["👥 Members come together for the first time"]
        A --> B["❓ Uncertainty & Ambiguity"]
        A --> C["🤫 Cautious & Polite behavior"]
    end

    subgraph FEATURES["🔑 KEY FEATURES"]
        direction LR
        F1["🎯 Goal Setting\nEstablish clear objectives"]
        F2["🧩 Role Definition\nAssign responsibilities"]
        F3["🤝 Relationship Building\nBuild trust & cooperation"]
        F4["📋 Procedural Framework\nRules for decisions & comms"]
    end

    subgraph LEADER["👔 TEAM LEADER ROLE"]
        direction TB
        L1["🏗️ Team-Building\n• Workshops & ice-breakers\n• Share backgrounds & skills"]
        L2["📌 Clarify Goals\n• Define objectives & outcomes\n• Everyone knows their role"]
        L3["💬 Open Communication\n• Safe space for concerns\n• Set up collaboration tools"]
        L4["🤝 Build Trust\n• Model cooperative behavior\n• Collaboration over ego"]
    end

    subgraph DONE["✅ STAGE COMPLETE WHEN"]
        E["Members see themselves as\npart of a cohesive group"]
    end

    STAGE --> FEATURES
    FEATURES --> LEADER
    LEADER --> DONE

    style STAGE fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style FEATURES fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style LEADER fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style DONE fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#4a148c
    style A fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20
    style B fill:#ffcdd2,stroke:#c62828,color:#b71c1c
    style C fill:#ffcdd2,stroke:#c62828,color:#b71c1c
    style F1 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style F2 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style F3 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style F4 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L1 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style L2 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style L3 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style L4 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style E fill:#e1bee7,stroke:#6a1b9a,color:#4a148c
```


### Stage-2 Storming

```mermaid
flowchart TB
    subgraph STAGE["⚡ STAGE 2 — STORMING"]
        direction TB
        A["💥 Conflicts & disagreements arise"]
        A --> B["⚔️ Disputes about leadership,\nroles & goals"]
        A --> C["😤 Resistance & Frustration\nSlow progress, unattainable goals"]
        A --> D["🏋️ Role Negotiation\nEstablishing position & influence"]
    end

    subgraph EXAMPLE["📖 EXAMPLE — Marketing Campaign"]
        direction LR
        E1["🎨 Creative team\nInnovative but risky"]
        E2["📊 Analytics team\nData-driven & conservative"]
        E3["⏰ Arguments over\ntimelines & responsibilities"]
    end

    subgraph LEADER["👔 TEAM LEADER ROLE"]
        direction TB
        L1["🛡️ Safe Space for Expression\n• Share concerns openly\n• No fear of judgment"]
        L2["🔧 Constructive Conflict Resolution\n• Disagreements → problem-solving\n• Mediate & refocus on shared goals"]
        L3["🤝 Facilitate Harmony\n• Align diverse perspectives\n• Find common ground"]
        L4["💪 Maintain Team Morale\n• Reinforce value of working through conflict\n• Individual support for overwhelmed members"]
    end

    subgraph DONE["✅ WHY THIS STAGE MATTERS"]
        F["Builds foundation for\ntrust, collaboration &\nshared understanding"]
    end

    STAGE --> EXAMPLE
    EXAMPLE --> LEADER
    LEADER --> DONE

    style STAGE fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style EXAMPLE fill:#fce4ec,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style LEADER fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style DONE fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style A fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style B fill:#ffccbc,stroke:#d84315,color:#bf360c
    style C fill:#ffccbc,stroke:#d84315,color:#bf360c
    style D fill:#ffccbc,stroke:#d84315,color:#bf360c
    style E1 fill:#f8bbd0,stroke:#c62828,color:#b71c1c
    style E2 fill:#f8bbd0,stroke:#c62828,color:#b71c1c
    style E3 fill:#f8bbd0,stroke:#c62828,color:#b71c1c
    style L1 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L2 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L3 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L4 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style F fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20

```


### Stage-3 Norming

```mermaid
flowchart TB
    subgraph STAGE["🔄 STAGE 3 — NORMING"]
        direction TB
        A["🤝 Transition from conflict to cohesion"]
        A --> B["✅ Acceptance & Alignment\nAccept strengths, agree on roles"]
        A --> C["🫱🏼‍🫲🏽 Cooperation & Trust\nRelationships improve, respect grows"]
        A --> D["📏 Establishing Norms\nShared guidelines & workflows"]
    end

    subgraph INDICATORS["📊 NORMING STAGE INDICATORS"]
        direction LR
        I1["📅 Regular meetings\nClear agendas & outcomes"]
        I2["🎯 Task ownership\nDeliver on deadlines"]
        I3["🔄 Knowledge-sharing\nSteady progress"]
    end

    subgraph EXAMPLE["📖 EXAMPLE — Mobile App Start-up"]
        direction LR
        E1["🎨 UI/UX designer\naligns with dev requirements"]
        E2["📣 Marketing lead\ncollaborates for smooth launch"]
        E3["🛠️ Workflows established\nProject management tools"]
    end

    subgraph LEADER["👔 TEAM LEADER ROLE"]
        direction TB
        L1["📋 Facilitate Norms Development\n• Define guidelines & best practices\n• Align expectations & work standards"]
        L2["🧩 Clarify Roles & Responsibilities\n• Verify tasks & contributions\n• Address remaining ambiguities"]
        L3["💪 Encourage Accountability & Support\n• Culture of mutual accountability\n• Celebrate small successes"]
    end

    STAGE --> INDICATORS
    INDICATORS --> EXAMPLE
    EXAMPLE --> LEADER

    style STAGE fill:#e8eaf6,stroke:#283593,stroke-width:2px,color:#1a237e
    style INDICATORS fill:#e0f7fa,stroke:#00695c,stroke-width:2px,color:#004d40
    style EXAMPLE fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#880e4f
    style LEADER fill:#fff8e1,stroke:#f57f17,stroke-width:2px,color:#e65100
    style A fill:#c5cae9,stroke:#283593,color:#1a237e
    style B fill:#9fa8da,stroke:#283593,color:#1a237e
    style C fill:#9fa8da,stroke:#283593,color:#1a237e
    style D fill:#9fa8da,stroke:#283593,color:#1a237e
    style I1 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style I2 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style I3 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style E1 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style E2 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style E3 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style L1 fill:#ffecb3,stroke:#f57f17,color:#e65100
    style L2 fill:#ffecb3,stroke:#f57f17,color:#e65100
    style L3 fill:#ffecb3,stroke:#f57f17,color:#e65100

```

### Stage-4 Performing

```mermaid
flowchart TB
    subgraph STAGE["🚀 STAGE 4 — PERFORMING"]
        direction TB
        A["⭐ Team reaches peak functionality"]
        A --> B["🎯 Role Mastery\nDeliver with minimal supervision"]
        A --> C["🤝 High Collaboration\nCohesive unit, collective success"]
        A --> D["🏆 Goal Achievement\nComplete tasks & deliver results"]
        A --> E["🔄 Continuous Improvement\nInnovate, solve & enhance"]
    end

    subgraph EXAMPLE["📖 EXAMPLE — Global Ad Campaign"]
        direction LR
        E1["🎨 Creative team\nInnovative ad content"]
        E2["💻 Digital marketing\nOptimize online placements"]
        E3["📈 Analytics team\nReal-time monitoring\n& strategy adjustments"]
    end

    subgraph LEADER["👔 TEAM LEADER ROLE"]
        direction TB
        L1["🧭 Guiding & Coaching\n• Advisor for challenges\n• Mentorship for skills & confidence"]
        L2["📋 Monitor Progress & Feedback\n• Track milestones & alignment\n• Recognize achievements"]
        L3["⚖️ Fairness & Equitable Workload\n• Review task distribution\n• Prevent overburdening"]
        L4["🔄 Foster Continuous Improvement\n• Post-project reviews\n• Identify lessons learned"]
    end

    STAGE --> EXAMPLE
    EXAMPLE --> LEADER

    style STAGE fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style EXAMPLE fill:#ede7f6,stroke:#4527a0,stroke-width:2px,color:#311b92
    style LEADER fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style A fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20
    style B fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style C fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style D fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style E fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style E1 fill:#d1c4e9,stroke:#4527a0,color:#311b92
    style E2 fill:#d1c4e9,stroke:#4527a0,color:#311b92
    style E3 fill:#d1c4e9,stroke:#4527a0,color:#311b92
    style L1 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L2 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L3 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style L4 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
```


### Stage-5 Adjourning

```mermaid
flowchart TB
    subgraph STAGE["🏁 STAGE 5 — ADJOURNING"]
        direction TB
        A["👋 Team approaches end of project"]
        A --> B["📦 Task Completion\nFinal deliverables prepared & implemented"]
        A --> C["🪞 Reflection\nSuccesses, challenges & lessons learned"]
        A --> D["🚪 Disbanding\nMembers move to new roles/projects"]
        A --> E["🏆 Recognition\nAcknowledge contributions & celebrate"]
    end

    subgraph MOOD["🎭 TEAM MOOD"]
        direction LR
        M1["😊 Accomplishment"]
        M2["🥲 Nostalgia"]
        M3["😞 Disappointment\nif unsuccessful"]
    end

    subgraph EXAMPLE["📖 EXAMPLE — Merger Integration Team"]
        direction LR
        E1["📄 Final reports\nsubmitted to leadership"]
        E2["📋 Evaluation meeting\nstrengths & improvements"]
        E3["🔀 Members return to\ndepartments or new roles"]
    end

    subgraph LEADER["👔 TEAM LEADER ROLE"]
        direction TB
        L1["🔄 Structured Transition\n• Guide members to new roles\n• Smooth handover of responsibilities"]
        L2["🪞 Conclude with Reflection\n• Discuss lessons learned\n• Document for future teams"]
        L3["🎉 Acknowledge Contributions\n• Recognition, awards, gatherings\n• Thank members individually & collectively"]
        L4["📝 Document Best Practices\n• Capture processes & strategies\n• Share findings with stakeholders"]
    end

    STAGE --> MOOD
    MOOD --> EXAMPLE
    EXAMPLE --> LEADER

    style STAGE fill:#ede7f6,stroke:#4527a0,stroke-width:2px,color:#311b92
    style MOOD fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style EXAMPLE fill:#e0f2f1,stroke:#00695c,stroke-width:2px,color:#004d40
    style LEADER fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#880e4f
    style A fill:#d1c4e9,stroke:#4527a0,color:#311b92
    style B fill:#b39ddb,stroke:#4527a0,color:#311b92
    style C fill:#b39ddb,stroke:#4527a0,color:#311b92
    style D fill:#b39ddb,stroke:#4527a0,color:#311b92
    style E fill:#b39ddb,stroke:#4527a0,color:#311b92
    style M1 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style M2 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style M3 fill:#ffe0b2,stroke:#e65100,color:#bf360c
    style E1 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style E2 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style E3 fill:#b2dfdb,stroke:#00695c,color:#004d40
    style L1 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style L2 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style L3 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
    style L4 fill:#f8bbd0,stroke:#ad1457,color:#880e4f
```


#### RACI Chart

```mermaid
flowchart TB
    subgraph TITLE["📊 RACI CHART — Responsibility Assignment Matrix"]
        direction TB
        T1["Eliminates confusion • Reduces overlap • Prevents dropped tasks • Lowers conflicts"]
    end

    subgraph R["🔵 R — RESPONSIBLE"]
        direction TB
        R1["👷 The person who DOES the work"]
        R2["✅ Can have MULTIPLE Rs per task"]
        R3["📌 Example: Graphic designer\nwho creates the visuals"]
        R1 --> R2 --> R3
    end

    subgraph A["🔴 A — ACCOUNTABLE"]
        direction TB
        A1["👤 Ultimately ANSWERABLE\nfor task success"]
        A2["⚠️ ONLY ONE A per task\n— Most important rule!"]
        A3["📌 Example: Marketing Manager\nwho signs off final campaign"]
        A1 --> A2 --> A3
    end

    subgraph C["🟡 C — CONSULTED"]
        direction TB
        C1["🗣️ Input & expertise\nactively sought"]
        C2["↔️ TWO-WAY communication"]
        C3["📌 Example: Legal team\nreviews campaign copy"]
        C1 --> C2 --> C3
    end

    subgraph I["🟢 I — INFORMED"]
        direction TB
        I1["📬 Kept up-to-date\non progress & outcomes"]
        I2["➡️ ONE-WAY communication"]
        I3["📌 Example: CEO receives\nsummary report at launch"]
        I1 --> I2 --> I3
    end

    TITLE --> R
    TITLE --> A
    TITLE --> C
    TITLE --> I

    style TITLE fill:#37474f,stroke:#263238,stroke-width:3px,color:#ffffff
    style T1 fill:#455a64,stroke:#263238,color:#ffffff

    style R fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#0d47a1
    style R1 fill:#bbdefb,stroke:#1565c0,color:#0d47a1
    style R2 fill:#90caf9,stroke:#1565c0,color:#0d47a1
    style R3 fill:#64b5f6,stroke:#1565c0,color:#0d47a1

    style A fill:#ffebee,stroke:#c62828,stroke-width:3px,color:#b71c1c
    style A1 fill:#ffcdd2,stroke:#c62828,color:#b71c1c
    style A2 fill:#ef9a9a,stroke:#c62828,color:#b71c1c
    style A3 fill:#e57373,stroke:#c62828,color:#b71c1c

    style C fill:#fffde7,stroke:#f9a825,stroke-width:3px,color:#f57f17
    style C1 fill:#fff9c4,stroke:#f9a825,color:#f57f17
    style C2 fill:#fff176,stroke:#f9a825,color:#f57f17
    style C3 fill:#ffee58,stroke:#f9a825,color:#f57f17

    style I fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#1b5e20
    style I1 fill:#c8e6c9,stroke:#2e7d32,color:#1b5e20
    style I2 fill:#a5d6a7,stroke:#2e7d32,color:#1b5e20
    style I3 fill:#81c784,stroke:#2e7d32,color:#1b5e20
```

## Conflict Types

### Quick Memory Rule

- Task conflict = WHAT
- Relationship conflict = WHO
- Process conflict = HOW

If I remember What / Who / How, I can rebuild the answer quickly in the exam.

### Task Conflict

Task conflict is about the content of the work itself: what should be done first, what the priorities are, and what goal the team should focus on.

In an automotive software environment, this can happen when one engineer wants to prioritize an ADAS warning function, while another wants to focus first on ECU diagnostic logging before the release.

- Usually idea-based, not personal
- Can be healthy if it stays professional
- Main question: What should we build or prioritize first?

#### How to Deal With Task Conflict

- Encourage structured debate based on safety impact, customer value, release risk, and technical feasibility.
- Clarify the real objective early by asking: What problem are we solving first?
- Stay neutral as a leader, summarize both views, and guide the team toward a data-driven decision.
- Outcome goal: turn disagreement into better prioritization and innovation.

#### Task Conflict Exam Version

Task conflict in automotive software development occurs when team members disagree about what should be done first or which feature should have higher priority. For example, one engineer may want to prioritize an ADAS warning function, while another pushes for ECU diagnostic logging before release. This type of conflict is usually cognitive and can be healthy if handled professionally. The leader should encourage structured discussion, clarify the main objective, and guide the team toward a fact-based decision.

```mermaid
flowchart LR
    A[Task Conflict\nWHAT to build?] --> B[ADAS warning first\nor ECU diagnostic logging first?]
    B --> C[Clarify goal + compare impact]
    C --> D[Better decision]
```

### Relationship Conflict

Relationship conflict is based on interpersonal tension, differences in communication style, personality clashes, or ego issues.

In an automotive software environment, this may happen between a software integrator and a test engineer during defect triage meetings, where one speaks very directly and the other feels blamed for repeated delays.

- Emotional in nature
- Usually the most damaging if ignored
- Main question: Who is clashing?

#### How to Deal With Relationship Conflict

- Address the issue early through private one-to-one discussions.
- Focus on observable behavior, not personality.
- Mediate only after understanding both sides separately.
- Build psychological safety through respectful communication and trust-building.
- If the conflict becomes severe, temporarily separate responsibilities or reassign roles.

#### Relationship Conflict Exam Version

Relationship conflict in automotive software development arises from personal tension, communication style, or ego differences between team members. For example, a software integrator and a test engineer may repeatedly clash during defect discussions because of sharp communication and mutual frustration. This type of conflict is emotional and can damage teamwork if not addressed early. The leader should handle it privately, focus on behavior rather than personality, and mediate with empathy to rebuild trust and cooperation.

```mermaid
flowchart LR
    A[Relationship Conflict\nWHO is clashing?] --> B[Integrator vs tester\ncommunication tension]
    B --> C[Private check-in + mediation]
    C --> D[Trust restored]
```

### Process Conflict

Process conflict is about how the work should be executed, including methods, responsibilities, approvals, timelines, and resource ownership.

In an automotive software environment, this may happen when the team disagrees on who owns final ECU release approval, or whether a change should follow a formal review path or a faster sprint workflow.

- Procedural and logistical at first
- Can become personal if roles are unclear
- Main question: How should the work be done?

#### How to Deal With Process Conflict

- Map the workflow visually using a RACI matrix or a simple process diagram.
- Define who is responsible, who approves, and who must be consulted.
- Agree on process rules and sign-off points.
- Revisit the process regularly before major releases, sprints, or audits.
- Outcome goal: remove ambiguity so the team can focus on delivery.

#### Process Conflict Exam Version

Process conflict in automotive software development occurs when team members disagree on how the work should be carried out. For example, the team may argue about who has final sign-off authority for an ECU release or whether the change should follow a formal review process or a sprint-based workflow. This conflict is mainly procedural, but it can become personal if roles are unclear. The leader should clarify the workflow, define responsibilities, and create agreement on the process so that confusion is reduced and execution becomes smoother.

```mermaid
flowchart LR
    A[Process Conflict\nHOW to work?] --> B[Who approves ECU release?\nWhich workflow to follow?]
    B --> C[Define process + roles]
    C --> D[Less ambiguity]
```
