## System Architecture

```mermaid
flowchart TD

A[Security Logs] --> B[Python SOC Agent]
B --> C[LLM Threat Analysis]
C --> D[Structured JSON Alert]
D --> E[Automated Response Engine]
E --> F[Block IP]
E --> G[Isolate Host]
```
