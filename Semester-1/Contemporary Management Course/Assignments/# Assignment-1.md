# Assignment-1 Solution


## Business Plan Goals (Word-friendly tables)

### Goal 1 — Competitor Benchmarking & Team Awareness
| Field | Content |
|---|---|
| Goal | Benchmark Chinese automakers’ Infotainment/Entertainment strengths and build team awareness |
| Time-frame | M0–M6 initial; refresh quarterly |
| Targets (What) | - Identify China top-10 best-sellers (mid + premium)<br>- Deep-dive competitor features (Infotainment/Entertainment)<br>- Run expert + dev exposure sessions (static + driving) |
| Measurements (KPIs) | - Top-10 list validated for next 6 months<br>- 20–40 key features documented and validated (expert + marketing)<br>- Evidence captured (forums/social complaints)<br>- Awareness: ≥10 hrs/person exposure (≈5 hrs review + 5 hrs driving) |
| Success criteria | Teams can explain competitor feature set and gaps; feature database stays current |

---

### Goal 2 — China Feature Roadmap (Define, Prioritize, Plan)
| Field | Content |
|---|---|
| Goal | Define and prioritize the China feature roadmap and delivery timeline |
| Time-frame | M3–M6 plan; M6–M18 execute |
| Targets (What) | - Split backlog: (a) enhance existing features, (b) build new competitor-only features<br>- Prioritize by market need and feasibility<br>- Publish release plan (resources + deadlines) |
| Measurements (KPIs) | - Prioritized backlog approved<br>- Release plan published (owners/resources/dates)<br>- ≥10 new features planned for delivery within 18 months<br>- Demo readiness before release (e.g., demo by month 7 if dev=10 months) |
| Success criteria | Roadmap is approved, resourced, and tracked against milestones |

---

### Goal 3 — Best Practices Standardization (SOP)
| Field | Content |
|---|---|
| Goal | Standardize best practices across teams using SOPs (Standard Operating Procedures) |
| Time-frame | M0–M6 define; M6–M18 enforce |
| Targets (What) | - Capture lessons learned from old projects<br>- Define SOP per major feature (dev + test + release)<br>- Share and train across teams |
| Measurements (KPIs) | - SOP coverage (% key features with SOP)<br>- Adoption rate (teams using SOP in reviews/plans)<br>- Stability improvement of unstable features ~65% within first half of timeline<br>- Test automation +70% vs previous generation |
| Success criteria | Consistent execution across teams; fewer repeated issues release-to-release |

---

### Goal 4 — Risk Management (Early Detection & Mitigation)
| Field | Content |
|---|---|
| Goal | Detect risks early and execute mitigations |
| Time-frame | Start M0; review monthly; formal gate quarterly |
| Targets (What) | - Maintain risk register (tech/schedule/supplier/quality/compliance)<br>- Assign owners and mitigation actions<br>- Track closure and residual risk |
| Measurements (KPIs) | - % risks with owner + mitigation plan<br>- Mitigation closure rate<br>- Lead time (months before release risk is detected)<br>- # late critical issues trending down QoQ |
| Success criteria | Fewer surprises; predictable delivery and quality |

---

### Goal 5 — Customer Awareness & Perceived Value
| Field | Content |
|---|---|
| Goal | Increase customer awareness and perceived value of our Infotainment/Entertainment system (China focus) |
| Time-frame | M6–M18 (prep M3–M6) |
| Targets (What) | - Pre-series demos and influencer/target-user trials<br>- Marketing enablement (feature messaging + demos)<br>- Collect structured user feedback |
| Measurements (KPIs) | - Pre-series vehicles distributed to testers/influencers<br>- Satisfaction ≥80% for new features (pilot/beta)<br>- Awareness indicators: campaign reach/engagement, demo attendance, product page views |
| Success criteria | Measurable awareness uplift and improved sentiment/feedback |

## Plan

### Plan Items (M0–M18)

1. Confirm scope and success metrics (M0–M1)
  - Confirm China scope (mid + premium segments) and the definition of “top-10” best sellers
  - Lock KPIs per goal and reporting cadence (weekly operational, monthly management)

2. Build competitor benchmark baseline (M0–M3)
  - Collect market data and identify top-10 Chinese best-sellers
  - Purchase/access vehicles and collect Infotainment/Entertainment feature evidence
  - Create the competitor feature catalog (20–40 key features)

3. Run awareness & exposure program (M2–M6)
  - Execute static + driving sessions for expert/dev teams
  - Publish a concise “China competitor insights” brief and keep it updated quarterly

4. Translate gaps into a China roadmap (M3–M6)
  - Split backlog: enhance existing vs build new competitor-only features
  - Prioritize features (market impact, feasibility, dependency, cost)
  - Create an 18-month release plan with owners, resources, and milestones

5. Execute delivery with built-in testing (M6–M18)
  - Deliver features per milestones (implementation + unit/integration/acceptance testing)
  - Produce working demos ahead of release for marketing/pilot readiness
  - Collect market feedback and adjust priorities when needed

6. Establish SOP and quality governance (M0–M6 define; M6–M18 enforce)
  - Capture lessons learned from old projects and identify “stable reference” features
  - Create SOP templates + Definition of Done + release readiness gates
  - Increase test automation and track stability improvement KPIs

7. Continuous risk management (M0–M18)
  - Maintain RAID log (risks/issues/dependencies) with owners and mitigation actions
  - Run weekly RAID review and monthly deep-dive; escalate major items early

8. Customer awareness and perceived value (M6–M18)
  - Run pilots/betas with target users/influencers and measure satisfaction
  - Prepare marketing enablement content (demos, feature messaging, comparisons)
  - Use voice-of-customer insights to refine features and roadmap

## Stratgies

* China-first competitive benchmarking + rapid roadmap: continuously benchmark top Chinese players, translate gaps into a prioritized backlog with committed release * milestones.
* Standardize execution via SOP + governance: unify best practices across teams (definition of done, reviews, testing, release gates) to improve quality and predictability.
* Closed-loop validation with early risk control: run early pilots/demos with target users/influencers, track KPIs, manage a risk register, and adjust priorities based on feedback and measured outcomes.



## Organizing Functions 

### Org Chart

```mermaid
graph TD
  SP["Executive Sponsor"] --> DL["Program Owner<br>(Dept Lead)"]
  DL --> PMO["PMO / Program Manager<br>(cadence, reporting, RAID)"]

  DL --> T1["Team 1: Competitive Intelligence<br>(benchmarking, insights)"]
  DL --> T2["Team 2: Product, Delivery & Testing<br>(roadmap, requirements, engineering, feature testing)"]
  DL --> T3["Team 3: Quality, SOP & Test Automation<br>(standards, quality gates, automation, KPIs)"]
  DL --> T4["Team 4: Customer, Marketing & Feedback<br>(awareness, pilots, VOC)"]

  T1 --> T1a["Key outputs:<br>Top-10 cars, feature catalog,<br>gap analysis, awareness sessions"]
  T2 --> T2a["Key outputs:<br>prioritized backlog,<br>release plan, feature delivery,<br>unit/integration/acceptance testing"]
  T3 --> T3a["Key outputs:<br>SOPs, DoD, quality gates,<br>test automation uplift, quality KPIs"]
  T4 --> T4a["Key outputs:<br>marketing enablement,<br>pilot plan, satisfaction KPIs,<br>voice-of-customer insights"]

  PMO -. "collects status + risks" .-> T1
  PMO -. "collects status + risks" .-> T2
  PMO -. "collects status + risks" .-> T3
  PMO -. "collects status + risks" .-> T4
  ```


```mermaid

graph TD
  SP["🏛️ Executive Sponsor"] --> DL["👔 Program Owner<br>(Dept Lead)"]
  DL --> PMO["📋 PMO / Program Manager<br>(cadence, reporting, RAID)"]

  DL --> T1["🔍 Team 1: Competitive Intelligence<br>(benchmarking, insights)"]
  DL --> T2["🚀 Team 2: Product, Delivery & Testing<br>(roadmap, requirements, engineering,<br>feature testing)"]
  DL --> T3["✅ Team 3: Quality, SOP & Test Automation<br>(standards, quality gates, automation, KPIs)"]
  DL --> T4["📣 Team 4: Customer, Marketing & Feedback<br>(awareness, pilots, VOC)"]

  T1 --> T1a["Key outputs:<br>Top-10 cars, feature catalog,<br>gap analysis, awareness sessions"]
  T2 --> T2a["Key outputs:<br>prioritized backlog,<br>release plan, feature delivery,<br>unit/integration/acceptance testing"]
  T3 --> T3a["Key outputs:<br>SOPs, DoD, quality gates,<br>test automation uplift, quality KPIs"]
  T4 --> T4a["Key outputs:<br>marketing enablement,<br>pilot plan, satisfaction KPIs,<br>voice-of-customer insights"]

  PMO -. "collects status + risks" .-> T1
  PMO -. "collects status + risks" .-> T2
  PMO -. "collects status + risks" .-> T3
  PMO -. "collects status + risks" .-> T4

  style SP fill:#1a237e,color:#fff,stroke:#0d1642,stroke-width:3px
  style DL fill:#283593,color:#fff,stroke:#1a237e,stroke-width:2px
  style PMO fill:#4a148c,color:#fff,stroke:#311b92,stroke-width:2px

  style T1 fill:#1565c0,color:#fff,stroke:#0d47a1,stroke-width:2px
  style T2 fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px
  style T3 fill:#e65100,color:#fff,stroke:#bf360c,stroke-width:2px
  style T4 fill:#ad1457,color:#fff,stroke:#880e4f,stroke-width:2px

  style T1a fill:#bbdefb,color:#0d47a1,stroke:#1565c0
  style T2a fill:#c8e6c9,color:#1b5e20,stroke:#2e7d32
  style T3a fill:#ffe0b2,color:#bf360c,stroke:#e65100
  style T4a fill:#f8bbd0,color:#880e4f,stroke:#ad1457

  ```


  ### What need to be done?

  1. Confirm scope and success metrics
    - Confirm China scope (mid + premium segments) and definition of “top-10” best sellers
    - Lock KPIs per goal and define reporting cadence

  2. Set up program governance and working artifacts
    - Create action log + RAID log (risks/issues/dependencies) + decision log
    - Agree templates: benchmark report, feature catalog, SOP format, release readiness checklist

  3. Benchmark competitors and build the evidence base
    - Identify top-10 China best-sellers and collect data/evidence
    - Build competitor feature catalog (20–40 key Infotainment/Entertainment features)
    - Validate findings (expert + marketing) and keep baseline refreshed quarterly

  4. Run team awareness and exposure activities
    - Execute static + driving sessions and ensure required awareness hours/person
    - Publish “competitor insights” brief and communicate it across teams

  5. Convert insights into a China feature roadmap
    - Split backlog: enhance existing features vs build new competitor-only features
    - Prioritize features (market impact, feasibility, dependencies, cost)
    - Define an 18-month release plan (owners, resources, milestones)

  6. Deliver features with built-in testing
    - Implement features and execute unit/integration/acceptance testing
    - Produce working demos ahead of release for pilot/marketing readiness
    - Track progress vs milestones and adjust plans when needed

  7. Standardize best practices through SOP (Standing Plan)
    - Capture lessons learned and define SOP per major feature (dev + test + release)
    - Define Definition of Done and quality gates for releases
    - Improve test automation and stability KPIs vs previous generation

  8. Run closed-loop customer validation and awareness
    - Execute pilots/betas with target users/influencers and measure satisfaction
    - Prepare marketing enablement (feature messaging, demos, comparisons)
    - Feed voice-of-customer insights back into backlog and corrective actions

  ### Who will do what ?

  | Role | Responsibilities |
  |---|---|
  | Executive Sponsor | Approve budget, resolve escalations, sign off major scope changes |
  | Program Owner (Dept Lead) | Set direction, approve roadmap priorities, chair steering reviews |
  | PMO / Program Manager | Run cadence (weekly/monthly), maintain RAID log, consolidate status, track KPIs |
  | Team 1 Lead — Competitive Intelligence | Own competitor benchmark, maintain feature catalog, run awareness sessions |
  | Team 2 Lead — Product, Delivery & Testing | Own backlog, release plan, feature implementation, and feature-level testing |
  | Team 3 Lead — Quality, SOP & Test Automation | Define SOPs, enforce quality gates, drive test automation uplift, track stability KPIs |
  | Team 4 Lead — Customer, Marketing & Feedback | Run pilots/betas, prepare marketing content, collect and analyze VOC feedback |


  ### How will it be done ?

  #### Workstreams

  | Workstream | Timeframe | How it will be done |
  |---|---|---|
  | Benchmark & Align | M0-M6 | Identify top competitors, build the feature catalog, validate findings, and align teams on the benchmark baseline |
  | Roadmap & Planning | M3-M6 | Convert gaps into a prioritized backlog, assign owners, define milestones, and publish the 18-month release plan |
  | Delivery & Testing | M6-M18 | Implement prioritized features, run unit/integration/acceptance testing, and prepare demos before release |
  | Standardize & Control | M0-M18 | Define and apply SOPs, Definition of Done, release readiness gates, and automation KPIs across all teams |
  | Customer Validation & Feedback | M6-M18 | Run pilots/betas, collect customer and market feedback, and feed insights into backlog updates and corrective actions |

  #### Execution Governance

  | Area | Approach |
  |---|---|
  | Coordination model | Weekly team sync, monthly management review, and quarterly strategy/checkpoint review |
  | Tracking tools | Feature backlog, release roadmap, KPI dashboard, and RAID log |
  | Decision method | Strategic priorities stay centralized with Program Owner; execution details stay decentralized within each team |
  | Control mechanism | PMO consolidates status, risks, and actions; Quality team checks compliance to SOP and quality gates |


  #### Timeline per Task


```mermaid
gantt
    title Infotainment / Entertainment China Plan — Workstreams Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y
    excludes    weekends

    section Foundation
    Benchmark & Align                :ws1, 2026-01-01, 2026-06-30
    Standardize & Control            :ws4, 2026-01-01, 2027-06-30

    section Planning
    Roadmap & Planning               :ws2, after ws1, 2026-07-31

    section Execution
    Delivery & Testing               :ws3, after ws2, 2027-06-30
    Customer Validation & Feedback   :ws5, after ws3, 2027-06-30
```

### Centralized and decentralized criteria

| Decision Area | Centralized / Decentralized | Owner | Why |
|---|---|---|---|
| Program goals, KPIs, and China scope | Centralized | Executive Sponsor + Program Owner | Ensure one clear direction and shared success criteria |
| Competitor benchmark baseline and top-10 target vehicles | Centralized | Program Owner + Team 1 Lead | Keep comparison logic consistent across teams |
| Feature priorities and release milestones | Centralized | Program Owner | Avoid conflicting priorities and protect strategic focus |
| Budget, major staffing changes, and scope trade-offs | Centralized | Executive Sponsor + Program Owner | These decisions affect the full program and require leadership approval |
| SOP standards, quality gates, and KPI definitions | Centralized | Team 3 Lead + Program Owner | Standardization is needed to ensure quality consistency |
| Risk acceptance, major escalations, and go/no-go decisions | Centralized | Program Owner + PMO + Sponsor | High-impact decisions need cross-program visibility and control |
| Market analysis execution and evidence collection | Decentralized | Team 1 | The team has the right expertise and can work faster operationally |
| Feature design, implementation approach, and sprint planning | Decentralized | Team 2 | Technical teams should choose the best delivery method within agreed priorities |
| Test execution details and automation implementation | Decentralized | Team 2 + Team 3 | Teams need flexibility to adapt testing to feature and platform needs |
| Pilot execution, campaign content, and customer feedback collection | Decentralized | Team 4 | Customer-facing activities must adapt quickly to target users and market feedback |
| Day-to-day issue resolution and task planning | Decentralized | Each Team Lead | Faster local decisions improve execution speed |

**Recommended model:** a **hybrid structure** — centralize strategic, budget, quality, and release decisions; decentralize technical execution, analysis activities, testing details, and customer-facing operations. This keeps the program aligned while preserving team agility.