# Accounting 4 Managers

## Ex-1: Journalize the following transactions to journal of ABC Co.

1. **Owner invested $100,000 cash in the business**
   1. *Assets-Cash_Dr* = 100K
   2. *Equity-Capital_Cr* = 100K
    
    ```mermaid
    graph LR
    subgraph IDENTIFY["1 IDENTIFY"]
        ID["FastForward receives $30,000 cash<br/>from Chas Taylor as owner contribution"]
    end

    subgraph ANALYZE["2 ANALYZE"]
        A1["Assets = Liabilities + Equity"]
        A3["Cash +30,000 = 0 + +30,000"]
        A1 --- A3
    end

    subgraph RECORD["3 RECORD"]
        R1["(1) Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp; 30,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        R2["&nbsp;&nbsp;&nbsp; C. Taylor, Capital &nbsp; 301 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 30,000"]
        R1 --- R2
    end

    subgraph POST["4 POST"]
        subgraph CASH["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C_DR["Dr: (1) 30,000"] ~~~ C_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CAPITAL["C. Taylor, Capital &nbsp;&nbsp;&nbsp;&nbsp; 301"]
            direction LR
            K_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ K_CR["Cr: (1) 30,000"]
        end
    end

    IDENTIFY --> ANALYZE
    ANALYZE --> RECORD
    RECORD -- "post debit to Cash" --> CASH
    RECORD -- "post credit to Capital" --> CAPITAL

    style IDENTIFY fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD fill:#fff8e1,stroke:#f57f17,color:#333
    style POST fill:#e3f2fd,stroke:#1565c0,color:#333
    style CASH fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CAPITAL fill:#bbdefb,stroke:#1565c0,color:#333
    style ID fill:#fce4ec,stroke:#c62828,color:#333
    style C_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style C_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style K_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style K_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
2. **The Co. borrowed a bank loan for $200,000 in cash**
   1. *Assets-Cash_Dr* = 200K
   2. *Liabilities-Cr* = 200K ➡️ `Liabilities-Accounts-Payable`

    ```mermaid
    graph LR
    subgraph IDENTIFY["1 IDENTIFY"]
        ID2["The Co. borrowed a bank loan<br/>for $200,000 in cash"]
    end

    subgraph ANALYZE["2 ANALYZE"]
        B1["Assets = Liabilities + Equity"]
        B3["Cash +200,000 = +200,000 + 0"]
        B1 --- B3
    end

    subgraph RECORD["3 RECORD"]
        S1["(2) Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp; 200,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        S2["&nbsp;&nbsp;&nbsp; Accounts Payable &nbsp;&nbsp;&nbsp; 201 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 200,000"]
        S1 --- S2
    end

    subgraph POST["4 POST"]
        subgraph CASH2["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C2_DR["Dr: (2) 200,000"] ~~~ C2_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph AP["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ AP_CR["Cr: (2) 200,000"]
        end
    end

    IDENTIFY --> ANALYZE
    ANALYZE --> RECORD
    RECORD -- "post debit to Cash" --> CASH2
    RECORD -- "post credit to Accounts Payable" --> AP

    style IDENTIFY fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD fill:#fff8e1,stroke:#f57f17,color:#333
    style POST fill:#e3f2fd,stroke:#1565c0,color:#333
    style CASH2 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style AP fill:#bbdefb,stroke:#1565c0,color:#333
    style ID2 fill:#fce4ec,stroke:#c62828,color:#333
    style C2_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style C2_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style AP_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style AP_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```

3. **The Co. provided cash services to clients for $50,000 cash**
   1. *Assets-Cash-Dr* = 50K
   2. *Equity-Revenue_Cr* = 50K

    ```mermaid
    graph LR
    subgraph IDENTIFY3["1 IDENTIFY"]
        ID3["The Co. provided cash services<br/>to clients for $50,000 cash"]
    end

    subgraph ANALYZE3["2 ANALYZE"]
        D1["Assets = Liabilities + Equity"]
        D3["Cash +50,000 = 0 + Revenue +50,000"]
        D1 --- D3
    end

    subgraph RECORD3["3 RECORD"]
        T1["(3) Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp; 50,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        T2["&nbsp;&nbsp;&nbsp; Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 50,000"]
        T1 --- T2
    end

    subgraph POST3["4 POST"]
        subgraph CASH3["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C3_DR["Dr: (3) 50,000"] ~~~ C3_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph REV["Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401"]
            direction LR
            REV_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ REV_CR["Cr: (3) 50,000"]
        end
    end

    IDENTIFY3 --> ANALYZE3
    ANALYZE3 --> RECORD3
    RECORD3 -- "post debit to Cash" --> CASH3
    RECORD3 -- "post credit to Revenue" --> REV

    style IDENTIFY3 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE3 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD3 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST3 fill:#e3f2fd,stroke:#1565c0,color:#333
    style CASH3 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style REV fill:#bbdefb,stroke:#1565c0,color:#333
    style ID3 fill:#fce4ec,stroke:#c62828,color:#333
    style C3_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style C3_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style REV_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style REV_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```

4. **The Co. provided credit services to a client for $20000 (on account)**
   1. *Assets-Accounts_Receivable_Dr* = 20K
   2. *Equity-Revenue_Cr* = 20K
   
    ```mermaid
    graph LR
    subgraph IDENTIFY4["1 IDENTIFY"]
        ID4["The Co. provided credit services<br/>to a client for $20,000 on account"]
    end

    subgraph ANALYZE4["2 ANALYZE"]
        E1["Assets = Liabilities + Equity"]
        E3["Accounts Receivable +20,000 = 0 + Revenue +20,000"]
        E1 --- E3
    end

    subgraph RECORD4["3 RECORD"]
        U1["(4) Accounts Receivable &nbsp;&nbsp; 102 &nbsp; 20,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        U2["&nbsp;&nbsp;&nbsp; Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20,000"]
        U1 --- U2
    end

    subgraph POST4["4 POST"]
        subgraph AR["Accounts Receivable &nbsp;&nbsp;&nbsp;&nbsp; 102"]
            direction LR
            AR_DR["Dr: (4) 20,000"] ~~~ AR_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph REV4["Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401"]
            direction LR
            REV4_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ REV4_CR["Cr: (4) 20,000"]
        end
    end

    IDENTIFY4 --> ANALYZE4
    ANALYZE4 --> RECORD4
    RECORD4 -- "post debit to Accts Receivable" --> AR
    RECORD4 -- "post credit to Revenue" --> REV4

    style IDENTIFY4 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE4 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD4 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST4 fill:#e3f2fd,stroke:#1565c0,color:#333
    style AR fill:#c8e6c9,stroke:#2e7d32,color:#333
    style REV4 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID4 fill:#fce4ec,stroke:#c62828,color:#333
    style AR_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style AR_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style REV4_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style REV4_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```

5. **The client in transaction 4 paid $5000 of her balance**
   1. *Assets-Cash_Dr* = 5K
   2. *Assets-Accounts_Receivable_Cr* = 15K
   ```mermaid
    graph LR
    subgraph IDENTIFY5["1 IDENTIFY"]
        ID5["Client from TX#4 paid $5,000<br/>of her $20,000 balance"]
    end

    subgraph ANALYZE5["2 ANALYZE"]
        F1["Assets = Liabilities + Equity"]
        F3["Cash +5,000 &amp; Accts Receivable -15,000 = 0 + 0"]
        F1 --- F3
    end

    subgraph RECORD5["3 RECORD"]
        V1["(5) Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp; 5,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        V2["&nbsp;&nbsp;&nbsp; Accounts Receivable &nbsp; 102 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 15,000"]
        V1 --- V2
    end

    subgraph POST5["4 POST"]
        subgraph CASH5["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C5_DR["Dr: (5) 5,000"] ~~~ C5_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph AR5["Accounts Receivable &nbsp;&nbsp;&nbsp;&nbsp; 102"]
            direction LR
            AR5_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ AR5_CR["Cr: (5) 15,000"]
        end
    end

    IDENTIFY5 --> ANALYZE5
    ANALYZE5 --> RECORD5
    RECORD5 -- "post debit to Cash" --> CASH5
    RECORD5 -- "post credit to Accts Receivable" --> AR5

    style IDENTIFY5 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE5 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD5 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST5 fill:#e3f2fd,stroke:#1565c0,color:#333
    style CASH5 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style AR5 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID5 fill:#fce4ec,stroke:#c62828,color:#333
    style C5_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style C5_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style AR5_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style AR5_CR fill:#90caf9,stroke:#1565c0,color:#333
   ```
6. **The Co. purchased equipment for $70,000 in cash**
   1. *Assets-Cash_Cr* = 70K
   2. *Assets-Equipments_Dr* = 70K
    ```mermaid
    graph LR
    subgraph IDENTIFY6["1 IDENTIFY"]
        ID6["The Co. purchased equipment<br/>for $70,000 in cash"]
    end

    subgraph ANALYZE6["2 ANALYZE"]
        G1["Assets = Liabilities + Equity"]
        G3["Equipment +70,000 &amp; Cash -70,000 = 0 + 0"]
        G1 --- G3
    end

    subgraph RECORD6["3 RECORD"]
        W1["(6) Equipment &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 103 &nbsp; 70,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        W2["&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 70,000"]
        W1 --- W2
    end

    subgraph POST6["4 POST"]
        subgraph EQUIP6["Equipment &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 103"]
            direction LR
            EQ6_DR["Dr: (6) 70,000"] ~~~ EQ6_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CASH6["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C6_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ C6_CR["Cr: (6) 70,000"]
        end
    end

    IDENTIFY6 --> ANALYZE6
    ANALYZE6 --> RECORD6
    RECORD6 -- "post debit to Equipment" --> EQUIP6
    RECORD6 -- "post credit to Cash" --> CASH6

    style IDENTIFY6 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE6 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD6 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST6 fill:#e3f2fd,stroke:#1565c0,color:#333
    style EQUIP6 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CASH6 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID6 fill:#fce4ec,stroke:#c62828,color:#333
    style EQ6_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style EQ6_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style C6_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style C6_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
7. **The Co. purchased inventory for $ 40,000 on credit from suppliers**
   1. *Equity-Expenses_Dr* = 40K
   2. *Liabilities-Accounts_Payable_Cr* = 40K
   ```mermaid
    graph LR
    subgraph IDENTIFY7["1 IDENTIFY"]
        ID7["The Co. purchased inventory for<br/>$40,000 on credit from suppliers"]
    end

    subgraph ANALYZE7["2 ANALYZE"]
        H1["Assets = Liabilities + Equity"]
        H3["0 = Accts Payable +40,000 + Expenses +40,000"]
        H1 --- H3
    end

    subgraph RECORD7["3 RECORD"]
        X1["(7) Expenses-Inventory &nbsp;&nbsp;&nbsp; 501 &nbsp; 40,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        X2["&nbsp;&nbsp;&nbsp; Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 40,000"]
        X1 --- X2
    end

    subgraph POST7["4 POST"]
        subgraph EXP7["Expenses-Inventory &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 501"]
            direction LR
            EXP7_DR["Dr: (7) 40,000"] ~~~ EXP7_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph AP7["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP7_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ AP7_CR["Cr: (7) 40,000"]
        end
    end

    IDENTIFY7 --> ANALYZE7
    ANALYZE7 --> RECORD7
    RECORD7 -- "post debit to Expenses" --> EXP7
    RECORD7 -- "post credit to Accts Payable" --> AP7

    style IDENTIFY7 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE7 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD7 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST7 fill:#e3f2fd,stroke:#1565c0,color:#333
    style EXP7 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style AP7 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID7 fill:#fce4ec,stroke:#c62828,color:#333
    style EXP7_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style EXP7_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style AP7_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style AP7_CR fill:#90caf9,stroke:#1565c0,color:#333
   ```
8. **The Co. Sold the inventory purchased in previous transaction for $50,000 in cash**
   1. *Equity-Revenues_Cr* = 10K
   2. *Assets-Cash_Dr* = 50K
   3. *Liabilities-Accounts_Payable_Dr* = 40K
   4. *Assets-Cash_Cr* = 40K
   ```mermaid
    graph LR
    subgraph IDENTIFY8["1 IDENTIFY"]
        ID8["Co. sold inventory from TX#7<br/>for $50,000 cash — Cost was $40,000"]
    end

    subgraph ANALYZE8["2 ANALYZE"]
        I1["Assets = Liabilities + Equity"]
        I3["Cash +50K -40K = Accts Payable -40K + Revenue +10K"]
        I4["Net: Cash +10K = AP -40K + Revenue +10K"]
        I1 --- I3 --- I4
    end

    subgraph RECORD8["3 RECORD — Compound Entry"]
        Y1["(8a) Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp; 50,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        Y2["&nbsp;&nbsp;&nbsp;&nbsp; Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10,000"]
        Y3["(8b) Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp; 201 &nbsp; 40,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        Y4["&nbsp;&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 40,000"]
        Y1 --- Y2 --- Y3 --- Y4
    end

    subgraph POST8["4 POST"]
        subgraph CASH8["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C8_DR["Dr: (8a) 50,000"] ~~~ C8_CR["Cr: (8b) 40,000"]
        end
        subgraph REV8["Revenue &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 401"]
            direction LR
            REV8_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ REV8_CR["Cr: (8a) 10,000"]
        end
        subgraph AP8["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP8_DR["Dr: (8b) 40,000"] ~~~ AP8_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
    end

    IDENTIFY8 --> ANALYZE8
    ANALYZE8 --> RECORD8
    RECORD8 -- "post Dr/Cr to Cash" --> CASH8
    RECORD8 -- "post credit to Revenue" --> REV8
    RECORD8 -- "post debit to Accts Payable" --> AP8

    style IDENTIFY8 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE8 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD8 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST8 fill:#e3f2fd,stroke:#1565c0,color:#333
    style CASH8 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style REV8 fill:#bbdefb,stroke:#1565c0,color:#333
    style AP8 fill:#d7ccc8,stroke:#795548,color:#333
    style ID8 fill:#fce4ec,stroke:#c62828,color:#333
    style C8_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style C8_CR fill:#ef9a9a,stroke:#c62828,color:#333
    style REV8_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style REV8_CR fill:#90caf9,stroke:#1565c0,color:#333
    style AP8_DR fill:#d7ccc8,stroke:#795548,color:#333
    style AP8_CR fill:#d7ccc8,stroke:#795548,color:#999
   ```
9.  **The Co. purchased equipment for $2000 on credit**
    1.  *Assets-Equipments_Dr* = 2K
    2.  *Liabilities-Accounts_Receiable_Cr* = 2K
    ```mermaid
    graph LR
    subgraph IDENTIFY9["1 IDENTIFY"]
        ID9["The Co. purchased equipment<br/>for $2,000 on credit"]
    end

    subgraph ANALYZE9["2 ANALYZE"]
        J1["Assets = Liabilities + Equity"]
        J3["Equipment +2,000 = Accts Payable +2,000 + 0"]
        J1 --- J3
    end

    subgraph RECORD9["3 RECORD"]
        Z1["(9) Equipment &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 103 &nbsp; 2,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        Z2["&nbsp;&nbsp;&nbsp; Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2,000"]
        Z1 --- Z2
    end

    subgraph POST9["4 POST"]
        subgraph EQUIP9["Equipment &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 103"]
            direction LR
            EQ9_DR["Dr: (9) 2,000"] ~~~ EQ9_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph AP9["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP9_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ AP9_CR["Cr: (9) 2,000"]
        end
    end

    IDENTIFY9 --> ANALYZE9
    ANALYZE9 --> RECORD9
    RECORD9 -- "post debit to Equipment" --> EQUIP9
    RECORD9 -- "post credit to Accts Payable" --> AP9

    style IDENTIFY9 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE9 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD9 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST9 fill:#e3f2fd,stroke:#1565c0,color:#333
    style EQUIP9 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style AP9 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID9 fill:#fce4ec,stroke:#c62828,color:#333
    style EQ9_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style EQ9_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style AP9_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style AP9_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
10. **The Co. received and paid the advertising bill for the month for $10,000 in cash**
    1.  *Assets-Cash_Cr* = 10K
    2.  *Equity-Expenses_Utilities_Dr* = 10K
    ```mermaid
    graph LR
    subgraph IDENTIFY10["1 IDENTIFY"]
        ID10["The Co. received and paid the<br/>advertising bill for $10,000 in cash"]
    end

    subgraph ANALYZE10["2 ANALYZE"]
        K1["Assets = Liabilities + Equity"]
        K3["Cash -10,000 = 0 + Expenses +10,000"]
        K1 --- K3
    end

    subgraph RECORD10["3 RECORD"]
        AA1["(10) Expenses-Advertising &nbsp; 501 &nbsp; 10,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        AA2["&nbsp;&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10,000"]
        AA1 --- AA2
    end

    subgraph POST10["4 POST"]
        subgraph EXP10["Expenses-Advertising &nbsp;&nbsp;&nbsp;&nbsp; 501"]
            direction LR
            EXP10_DR["Dr: (10) 10,000"] ~~~ EXP10_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CASH10["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C10_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ C10_CR["Cr: (10) 10,000"]
        end
    end

    IDENTIFY10 --> ANALYZE10
    ANALYZE10 --> RECORD10
    RECORD10 -- "post debit to Expenses" --> EXP10
    RECORD10 -- "post credit to Cash" --> CASH10

    style IDENTIFY10 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE10 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD10 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST10 fill:#e3f2fd,stroke:#1565c0,color:#333
    style EXP10 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CASH10 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID10 fill:#fce4ec,stroke:#c62828,color:#333
    style EXP10_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style EXP10_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style C10_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style C10_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
11. **The Co. received the utilities bill for $5000**
    1.  *Equity-Expenses_Utilities_Dr* = 5K
    2.  *Liabilities-Accounts_Payable_Cr* = 5K
    ```mermaid
    graph LR
    subgraph IDENTIFY11["1 IDENTIFY"]
        ID11["The Co. received the utilities<br/>bill for $5,000 — not yet paid"]
    end

    subgraph ANALYZE11["2 ANALYZE"]
        L1["Assets = Liabilities + Equity"]
        L3["0 = Accts Payable +5,000 + Expenses +5,000"]
        L1 --- L3
    end

    subgraph RECORD11["3 RECORD"]
        AB1["(11) Expenses-Utilities &nbsp;&nbsp;&nbsp;&nbsp; 501 &nbsp; 5,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        AB2["&nbsp;&nbsp;&nbsp;&nbsp; Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp; 201 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000"]
        AB1 --- AB2
    end

    subgraph POST11["4 POST"]
        subgraph EXP11["Expenses-Utilities &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 501"]
            direction LR
            EXP11_DR["Dr: (11) 5,000"] ~~~ EXP11_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph AP11["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP11_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ AP11_CR["Cr: (11) 5,000"]
        end
    end

    IDENTIFY11 --> ANALYZE11
    ANALYZE11 --> RECORD11
    RECORD11 -- "post debit to Expenses" --> EXP11
    RECORD11 -- "post credit to Accts Payable" --> AP11

    style IDENTIFY11 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE11 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD11 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST11 fill:#e3f2fd,stroke:#1565c0,color:#333
    style EXP11 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style AP11 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID11 fill:#fce4ec,stroke:#c62828,color:#333
    style EXP11_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style EXP11_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style AP11_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style AP11_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
12. **The Co. paid the above utilities bill**
    1.  *Liabilities-Accounts_Payable_Dr* = 5K
    2.  *Assets-Cash_Cr* = 5K
    ```mermaid
    graph LR
    subgraph IDENTIFY12["1 IDENTIFY"]
        ID12["The Co. paid the utilities bill<br/>from TX#11 for $5,000 in cash"]
    end

    subgraph ANALYZE12["2 ANALYZE"]
        M1["Assets = Liabilities + Equity"]
        M3["Cash -5,000 = Accts Payable -5,000 + 0"]
        M1 --- M3
    end

    subgraph RECORD12["3 RECORD"]
        AC1["(12) Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp; 201 &nbsp; 5,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        AC2["&nbsp;&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000"]
        AC1 --- AC2
    end

    subgraph POST12["4 POST"]
        subgraph AP12["Accounts Payable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 201"]
            direction LR
            AP12_DR["Dr: (12) 5,000"] ~~~ AP12_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CASH12["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C12_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ C12_CR["Cr: (12) 5,000"]
        end
    end

    IDENTIFY12 --> ANALYZE12
    ANALYZE12 --> RECORD12
    RECORD12 -- "post debit to Accts Payable" --> AP12
    RECORD12 -- "post credit to Cash" --> CASH12

    style IDENTIFY12 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE12 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD12 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST12 fill:#e3f2fd,stroke:#1565c0,color:#333
    style AP12 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CASH12 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID12 fill:#fce4ec,stroke:#c62828,color:#333
    style AP12_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style AP12_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style C12_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style C12_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
13. **The owner withdrew $5000 in cash from the company for his personal use**
    1.  *Assets-Cash_Cr* = 5K
    2.  *Equity-Withdrawals_Dr* = 5K
    ```mermaid
    graph LR
    subgraph IDENTIFY13["1 IDENTIFY"]
        ID13["The owner withdrew $5,000 cash<br/>from the company for personal use"]
    end

    subgraph ANALYZE13["2 ANALYZE"]
        N1["Assets = Liabilities + Equity"]
        N3["Cash -5,000 = 0 + Withdrawals -5,000"]
        N1 --- N3
    end

    subgraph RECORD13["3 RECORD"]
        AD1["(13) Owner Withdrawals &nbsp;&nbsp; 302 &nbsp; 5,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        AD2["&nbsp;&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000"]
        AD1 --- AD2
    end

    subgraph POST13["4 POST"]
        subgraph WD13["Owner Withdrawals &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 302"]
            direction LR
            WD13_DR["Dr: (13) 5,000"] ~~~ WD13_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CASH13["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C13_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ C13_CR["Cr: (13) 5,000"]
        end
    end

    IDENTIFY13 --> ANALYZE13
    ANALYZE13 --> RECORD13
    RECORD13 -- "post debit to Withdrawals" --> WD13
    RECORD13 -- "post credit to Cash" --> CASH13

    style IDENTIFY13 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE13 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD13 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST13 fill:#e3f2fd,stroke:#1565c0,color:#333
    style WD13 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CASH13 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID13 fill:#fce4ec,stroke:#c62828,color:#333
    style WD13_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style WD13_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style C13_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style C13_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
14. **The Co. purchased a one-year insurance policy for $60000 cash**
    1.  *Assets-Cash_Cr* = 60K
    2.  *Assets-Prepaid_Insurance_Dr* = 60K
    ```mermaid
    graph LR
    subgraph IDENTIFY14["1 IDENTIFY"]
        ID14["The Co. purchased a one-year<br/>insurance policy for $60,000 cash"]
    end

    subgraph ANALYZE14["2 ANALYZE"]
        O1["Assets = Liabilities + Equity"]
        O3["Prepaid Insurance +60,000 &amp; Cash -60,000 = 0 + 0"]
        O1 --- O3
    end

    subgraph RECORD14["3 RECORD"]
        AE1["(14) Prepaid Insurance &nbsp;&nbsp;&nbsp; 104 &nbsp; 60,000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        AE2["&nbsp;&nbsp;&nbsp;&nbsp; Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 60,000"]
        AE1 --- AE2
    end

    subgraph POST14["4 POST"]
        subgraph PI14["Prepaid Insurance &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 104"]
            direction LR
            PI14_DR["Dr: (14) 60,000"] ~~~ PI14_CR["Cr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        end
        subgraph CASH14["Cash &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101"]
            direction LR
            C14_DR["Dr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"] ~~~ C14_CR["Cr: (14) 60,000"]
        end
    end

    IDENTIFY14 --> ANALYZE14
    ANALYZE14 --> RECORD14
    RECORD14 -- "post debit to Prepaid Insurance" --> PI14
    RECORD14 -- "post credit to Cash" --> CASH14

    style IDENTIFY14 fill:#fce4ec,stroke:#c62828,color:#333
    style ANALYZE14 fill:#e0f2f1,stroke:#00695c,color:#333
    style RECORD14 fill:#fff8e1,stroke:#f57f17,color:#333
    style POST14 fill:#e3f2fd,stroke:#1565c0,color:#333
    style PI14 fill:#c8e6c9,stroke:#2e7d32,color:#333
    style CASH14 fill:#bbdefb,stroke:#1565c0,color:#333
    style ID14 fill:#fce4ec,stroke:#c62828,color:#333
    style PI14_DR fill:#a5d6a7,stroke:#2e7d32,color:#333
    style PI14_CR fill:#c8e6c9,stroke:#2e7d32,color:#999
    style C14_DR fill:#bbdefb,stroke:#1565c0,color:#999
    style C14_CR fill:#90caf9,stroke:#1565c0,color:#333
    ```
15. **The Co. received $10,000 cash deposits from clients for services to be provided in the coming period**