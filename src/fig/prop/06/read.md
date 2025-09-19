flowchart TD
    %% Styles
    classDef box fill:#f9f9f9,stroke:#333,stroke-width:1px,rx:5px,ry:5px
    classDef excl fill:#ffe6e6,stroke:#cc0000,stroke-width:1px,rx:5px,ry:5px

    %% Nodes
    A[Identification<br/>Records identified (n = 230)]:::box
    B[Duplicates removed<br/>Remaining (n = 200)]:::box
    C[Screening<br/>Records screened (n = 120)]:::box
    D[Records excluded<br/>(n = 55)]:::excl
    E[Eligibility<br/>Full-text assessed (n = 65)]:::box
    F[Included<br/>Final corpus (n = 65)]:::box

    %% Flow
    A --> B --> C --> E --> F
    C --> D



    flowchart TD
    %% Styles
    classDef box fill:#f9f9f9,stroke:#333,stroke-width:1px,rx:5px,ry:5px
    classDef excl fill:#ffe6e6,stroke:#cc0000,stroke-width:1px,rx:5px,ry:5px

    %% Identification
    A1[Records identified through databases<br/>n = 210]:::box
    A2[Additional records identified through other sources<br/>n = 20]:::box
    A3[Total records identified<br/>n = 230]:::box

    %% Deduplication
    B[After duplicates removed<br/>Remaining n = 200]:::box

    %% Screening
    C[Screening<br/>Records screened n = 120]:::box
    D[Records excluded<br/>n = 55]:::excl

    %% Eligibility
    E[Eligibility<br/>Full-text assessed n = 65]:::box
    F[Full-text excluded with reasons<br/>n = 0]:::excl

    %% Included
    G[Included<br/>Final corpus n = 65]:::box

    %% Flows
    A1 --> A3
    A2 --> A3
    A3 --> B --> C --> E --> G
    C --> D
    E --> F