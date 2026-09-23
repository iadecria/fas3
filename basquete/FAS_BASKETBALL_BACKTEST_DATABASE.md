# FAS BASKETBALL — HISTÓRICO, BACKTEST E AUDITORIA DIÁRIA (V1.0)

Arquivo central de registro, auditoria e conferência contínua do **Basketball Analysis System (FAS Basketball V1.0)**.
Este arquivo preserva snapshots imutáveis, decisões pré-jogo, liquidações pós-jogo (CONFERE) e auditoria de erros (MISS AUDIT) para backtests futuros e comparação Multi-IA / Shadow.

---

## 📌 METODOLOGIA E CONTRATO DE AUDITORIA

- **Versão:** 1.0 (Laboratório Independente do FAS Football)
- **Schema:** `fas-basketball-import-v1`
- **Integridade Temporal:** Pre-match rigoroso. Proibido usar resultado posterior para reconstruir tese pre-match.
- **Competition Quality Gate:** `TIER_A` (WNBA, NBA), `TIER_B` (FIBA Intercontinental, EuroLeague, NBB, ACB), `TIER_C` (Ligas menores/Torneios curtos).
- **Auditoria de Miss:** Categorias permitidas: `STATISTICAL_VARIANCE`, `BAD_SELECTION`, `MISSING_CONTEXT`, `LINEUP_CHANGE`, `DATA_QUALITY`.
- **Status de Liquidação:** `HIT`, `MISS`, `VOID`, `PENDING`.

---

## 📅 REGISTRO POR DATA

---

### [2026-09-21] — RODADA DIÁRIA (CONFERE LIQUIDADO)

- **Data da Partida:** 2026-09-21
- **Competição:** WNBA 2026 (Temporada Regular)
- **Status de Liquidação:** **LIQUIDADO / AUDITADO**

#### 1. Dallas Wings @ Phoenix Mercury
* **Mercado Registrado:** Under 178,5 Pontos (Game Total Under)
* **Resultado Oficial:** Phoenix Mercury 87 × 86 Dallas Wings
* **Pontuação Combinada:** 87 + 86 = **173 Pontos**
* **Status:** ✅ **HIT**
* **Auditoria:** A tese pre-match de retenção de ritmo nos minutos finais de um jogo equilibrado sustentou a pontuação 5,5 pontos abaixo do teto de segurança. Cesta da vitória nos segundos finais por Kahleah Copper.

#### 2. Atlanta Dream @ New York Liberty
* **Mercado Registrado:** New York Liberty +6,0 (Spread Protegido)
* **Resultado Oficial:** New York Liberty 84 × 95 Atlanta Dream
* **Margem Efetiva:** New York 84 + 6,0 = 90,0 < 95 (Atlanta cobriu por 11 pontos)
* **Status:** ❌ **MISS**
* **Miss Audit:** `STATISTICAL_VARIANCE / MISSING_CONTEXT`
  * O Atlanta Dream teve uma corrida ofensiva no 2º tempo com aproveitamento atípico em arremessos de quadra, superando a margem de proteção do Liberty.

---

### [2026-09-22] — RODADA DIÁRIA (WNBA & FIBA)

- **Snapshot ID:** `FAS_BASKETBALL_GEMINI_2026-09-22_V2`
- **Cutoff:** 2026-09-22T13:30:00-03:00
- **Contexto da Data:** Penúltima rodada da temporada regular da WNBA (5 jogos noturnos decisivos para seeding). Início da FIBA Intercontinental Cup em Pequim (jogos da madrugada/manhã já encerrados pré-cutoff).
- **Status de Liquidação:** **PARCIALMENTE LIQUIDADO** (Jogos da Costa Oeste das 23:00 em apuração final de súmula)

#### 1. Auditoria de Competições Internacionais (FIBA Intercontinental Cup)
* *Rytas Vilnius 107 × 89 RSSB Tigers* — Encerrado antes do cutoff (04:30 BRT).
* *Boca Juniors 88 × 78 Beijing Royal Fighters* — Encerrado antes do cutoff (08:30 BRT).
* *Decisão:* Conforme seção # 2 e # 3 do manual, jogos encerrados pré-cutoff não recebem pick retroativo para blindar integridade estatística.

#### 2. Grade de Fixtures WNBA e Liquidação

1. **Connecticut Sun 69 @ 79 Washington Mystics**
   - *Resultado Oficial:* 79 × 69 (Total: 148 pontos | Margem: Washington +10)
   - **SAFE:** Washington Mystics -9.5 ➔ ✅ **HIT** (Washington venceu por 10 pontos: 79 - 69 = 10 > 9.5)
   - **SAFE+:** Menos de 164.5 Pontos ➔ ✅ **HIT** (Total 148 pontos <= 164.5)

2. **Minnesota Lynx 77 @ 96 Indiana Fever**
   - *Resultado Oficial:* 96 × 77 (Total: 173 pontos | Margem: Indiana +19)
   - **SAFE:** Mais de 181.5 Pontos ➔ ❌ **MISS** (Total 173 pontos)
     - *Miss Audit:* `LINEUP_CHANGE / STATISTICAL_VARIANCE` (Olivia Miles foi desfalque de última hora no Lynx por lesão na panturrilha; ataque do Lynx caiu para apenas 77 pontos, enquanto Caitlin Clark anotou 27 pts e liderou o Fever).
   - **SAFE+:** Minnesota Lynx +4.5 Spread ➔ ❌ **MISS** (Fever venceu por 19 pontos)
     - *Miss Audit:* `LINEUP_CHANGE`
   - **PRA CIMA:** Mais de 186.5 Pontos ➔ ❌ **MISS** (Total 173 pontos)
     - *Miss Audit:* `LINEUP_CHANGE`

3. **Toronto Tempo 85 @ 97 Chicago Sky**
   - *Resultado Oficial:* 97 × 85
   - **SAFE+:** Chicago Sky Vence - Moneyline ➔ ✅ **HIT** (Chicago Sky venceu por 97x85)

4. **Golden State Valkyries @ Portland Fire** (23:00 BRT)
   - *Tese:* Valkyries com 6 vitórias seguidas e melhor defesa da liga contra Portland eliminado (4 derrotas seguidas).
   - **SAFE:** Golden State Valkyries -8.5 (FAS 91 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** Golden State Vence 1º Tempo (FAS 86 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Menos de 158.5 Pontos (FAS 81 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING` (Aguardando homologação oficial da súmula da Costa Oeste)

5. **Los Angeles Sparks @ Las Vegas Aces** (23:00 BRT)
   - *Tese:* Sparks sem garrafão (Cameron Brink e Dearica Hamby fora); Aces com A'ja Wilson focadas na seed 3.
   - **SAFE:** Las Vegas Aces -9.5 (FAS 91 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** Las Vegas Aces 1º Tempo -6.5 (FAS 86 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Las Vegas Aces -15.5 Spread (FAS 80 | DQ HIGH | Risco MEDIUM_HIGH)
   - **Status:** `PENDING` (Vitória dos Aces confirmada, aguardando box score pontual completo de margem)

#### 3. Auditoria das Múltiplas / Bilhetes Combinados (Backtest de Bilhetes)

*   🎫 **MÚLTIPLA SAFE (WNBA):**
    *   Sun @ Mystics: Mystics -9.5 ➔ ✅ HIT (79x69)
    *   Lynx @ Fever: Over 181.5 ➔ ❌ MISS (173 pts)
    *   Valkyries @ Fire: Valkyries -8.5 ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces -9.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla SAFE:** ❌ **RED** (derrubada pelo desfalque de Olivia Miles e queda de pontuação do Lynx)

*   🎫 **MÚLTIPLA SAFE+ (WNBA):**
    *   Sun @ Mystics: Under 164.5 ➔ ✅ HIT (148 pts)
    *   Lynx @ Fever: Lynx +4.5 Spread ➔ ❌ MISS
    *   Tempo @ Sky: Sky ML ➔ ✅ HIT (97x85)
    *   Valkyries @ Fire: Valkyries 1ºT ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces 1ºT -6.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla SAFE+:** ❌ **RED** (1 erro já registrado no Lynx +4.5)

*   🎫 **MÚLTIPLA PRA CIMA (ATTACK):**
    *   Lynx @ Fever: Over 186.5 ➔ ❌ MISS
    *   Valkyries @ Fire: Under 158.5 ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces -15.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla PRA CIMA:** ❌ **RED**

*   🎫 **MÚLTIPLA APOSENTAR O NETO (Scanner / Alavancagem):**
    *   Bilhete longo da rodada WNBA.
    *   **Resultado:** ❌ **RED**

---

## 📊 PAINEL ACUMULADO DE BACKTEST (BASQUETE)

### A. Performance por Seleções Individuais (Singles)
| Categoria | Total Registrado | HIT | MISS | VOID | Win Rate (%) |
# FAS BASKETBALL — HISTÓRICO, BACKTEST E AUDITORIA DIÁRIA (V1.0)

Arquivo central de registro, auditoria e conferência contínua do **Basketball Analysis System (FAS Basketball V1.0)**.
Este arquivo preserva snapshots imutáveis, decisões pré-jogo, liquidações pós-jogo (CONFERE) e auditoria de erros (MISS AUDIT) para backtests futuros e comparação Multi-IA / Shadow.

---

## 📌 METODOLOGIA E CONTRATO DE AUDITORIA

- **Versão:** 1.0 (Laboratório Independente do FAS Football)
- **Schema:** `fas-basketball-import-v1`
- **Integridade Temporal:** Pre-match rigoroso. Proibido usar resultado posterior para reconstruir tese pre-match.
- **Competition Quality Gate:** `TIER_A` (WNBA, NBA), `TIER_B` (FIBA Intercontinental, EuroLeague, NBB, ACB), `TIER_C` (Ligas menores/Torneios curtos).
- **Auditoria de Miss:** Categorias permitidas: `STATISTICAL_VARIANCE`, `BAD_SELECTION`, `MISSING_CONTEXT`, `LINEUP_CHANGE`, `DATA_QUALITY`.
- **Status de Liquidação:** `HIT`, `MISS`, `VOID`, `PENDING`.

---

## 📅 REGISTRO POR DATA

---

### [2026-09-21] — RODADA DIÁRIA (CONFERE LIQUIDADO)

- **Data da Partida:** 2026-09-21
- **Competição:** WNBA 2026 (Temporada Regular)
- **Status de Liquidação:** **LIQUIDADO / AUDITADO**

#### 1. Dallas Wings @ Phoenix Mercury
* **Mercado Registrado:** Under 178,5 Pontos (Game Total Under)
* **Resultado Oficial:** Phoenix Mercury 87 × 86 Dallas Wings
* **Pontuação Combinada:** 87 + 86 = **173 Pontos**
* **Status:** ✅ **HIT**
* **Auditoria:** A tese pre-match de retenção de ritmo nos minutos finais de um jogo equilibrado sustentou a pontuação 5,5 pontos abaixo do teto de segurança. Cesta da vitória nos segundos finais por Kahleah Copper.

#### 2. Atlanta Dream @ New York Liberty
* **Mercado Registrado:** New York Liberty +6,0 (Spread Protegido)
* **Resultado Oficial:** New York Liberty 84 × 95 Atlanta Dream
* **Margem Efetiva:** New York 84 + 6,0 = 90,0 < 95 (Atlanta cobriu por 11 pontos)
* **Status:** ❌ **MISS**
* **Miss Audit:** `STATISTICAL_VARIANCE / MISSING_CONTEXT`
  * O Atlanta Dream teve uma corrida ofensiva no 2º tempo com aproveitamento atípico em arremessos de quadra, superando a margem de proteção do Liberty.

---

### [2026-09-22] — RODADA DIÁRIA (WNBA & FIBA)

- **Snapshot ID:** `FAS_BASKETBALL_GEMINI_2026-09-22_V2`
- **Cutoff:** 2026-09-22T13:30:00-03:00
- **Contexto da Data:** Penúltima rodada da temporada regular da WNBA (5 jogos noturnos decisivos para seeding). Início da FIBA Intercontinental Cup em Pequim (jogos da madrugada/manhã já encerrados pré-cutoff).
- **Status de Liquidação:** **PARCIALMENTE LIQUIDADO** (Jogos da Costa Oeste das 23:00 em apuração final de súmula)

#### 1. Auditoria de Competições Internacionais (FIBA Intercontinental Cup)
* *Rytas Vilnius 107 × 89 RSSB Tigers* — Encerrado antes do cutoff (04:30 BRT).
* *Boca Juniors 88 × 78 Beijing Royal Fighters* — Encerrado antes do cutoff (08:30 BRT).
* *Decisão:* Conforme seção # 2 e # 3 do manual, jogos encerrados pré-cutoff não recebem pick retroativo para blindar integridade estatística.

#### 2. Grade de Fixtures WNBA e Liquidação

1. **Connecticut Sun 69 @ 79 Washington Mystics**
   - *Resultado Oficial:* 79 × 69 (Total: 148 pontos | Margem: Washington +10)
   - **SAFE:** Washington Mystics -9.5 ➔ ✅ **HIT** (Washington venceu por 10 pontos: 79 - 69 = 10 > 9.5)
   - **SAFE+:** Menos de 164.5 Pontos ➔ ✅ **HIT** (Total 148 pontos <= 164.5)

2. **Minnesota Lynx 77 @ 96 Indiana Fever**
   - *Resultado Oficial:* 96 × 77 (Total: 173 pontos | Margem: Indiana +19)
   - **SAFE:** Mais de 181.5 Pontos ➔ ❌ **MISS** (Total 173 pontos)
     - *Miss Audit:* `LINEUP_CHANGE / STATISTICAL_VARIANCE` (Olivia Miles foi desfalque de última hora no Lynx por lesão na panturrilha; ataque do Lynx caiu para apenas 77 pontos, enquanto Caitlin Clark anotou 27 pts e liderou o Fever).
   - **SAFE+:** Minnesota Lynx +4.5 Spread ➔ ❌ **MISS** (Fever venceu por 19 pontos)
     - *Miss Audit:* `LINEUP_CHANGE`
   - **PRA CIMA:** Mais de 186.5 Pontos ➔ ❌ **MISS** (Total 173 pontos)
     - *Miss Audit:* `LINEUP_CHANGE`

3. **Toronto Tempo 85 @ 97 Chicago Sky**
   - *Resultado Oficial:* 97 × 85
   - **SAFE+:** Chicago Sky Vence - Moneyline ➔ ✅ **HIT** (Chicago Sky venceu por 97x85)

4. **Golden State Valkyries @ Portland Fire** (23:00 BRT)
   - *Tese:* Valkyries com 6 vitórias seguidas e melhor defesa da liga contra Portland eliminado (4 derrotas seguidas).
   - **SAFE:** Golden State Valkyries -8.5 (FAS 91 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** Golden State Vence 1º Tempo (FAS 86 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Menos de 158.5 Pontos (FAS 81 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING` (Aguardando homologação oficial da súmula da Costa Oeste)

5. **Los Angeles Sparks @ Las Vegas Aces** (23:00 BRT)
   - *Tese:* Sparks sem garrafão (Cameron Brink e Dearica Hamby fora); Aces com A'ja Wilson focadas na seed 3.
   - **SAFE:** Las Vegas Aces -9.5 (FAS 91 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** Las Vegas Aces 1º Tempo -6.5 (FAS 86 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Las Vegas Aces -15.5 Spread (FAS 80 | DQ HIGH | Risco MEDIUM_HIGH)
   - **Status:** `PENDING` (Vitória dos Aces confirmada, aguardando box score pontual completo de margem)

#### 3. Auditoria das Múltiplas / Bilhetes Combinados (Backtest de Bilhetes)

*   🎫 **MÚLTIPLA SAFE (WNBA):**
    *   Sun @ Mystics: Mystics -9.5 ➔ ✅ HIT (79x69)
    *   Lynx @ Fever: Over 181.5 ➔ ❌ MISS (173 pts)
    *   Valkyries @ Fire: Valkyries -8.5 ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces -9.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla SAFE:** ❌ **RED** (derrubada pelo desfalque de Olivia Miles e queda de pontuação do Lynx)

*   🎫 **MÚLTIPLA SAFE+ (WNBA):**
    *   Sun @ Mystics: Under 164.5 ➔ ✅ HIT (148 pts)
    *   Lynx @ Fever: Lynx +4.5 Spread ➔ ❌ MISS
    *   Tempo @ Sky: Sky ML ➔ ✅ HIT (97x85)
    *   Valkyries @ Fire: Valkyries 1ºT ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces 1ºT -6.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla SAFE+:** ❌ **RED** (1 erro já registrado no Lynx +4.5)

*   🎫 **MÚLTIPLA PRA CIMA (ATTACK):**
    *   Lynx @ Fever: Over 186.5 ➔ ❌ MISS
    *   Valkyries @ Fire: Under 158.5 ➔ ⏳ PENDING
    *   Sparks @ Aces: Aces -15.5 ➔ ⏳ PENDING
    *   **Resultado da Múltipla PRA CIMA:** ❌ **RED**

*   🎫 **MÚLTIPLA APOSENTAR O NETO (Scanner / Alavancagem):**
    *   Bilhete longo da rodada WNBA.
    *   **Resultado:** ❌ **RED**

---

## 📊 PAINEL ACUMULADO DE BACKTEST (BASQUETE)

### A. Performance por Seleções Individuais (Singles)
| Categoria | Total Registrado | HIT | MISS | VOID | Win Rate (%) |
|---|---|---|---|---|---|
| **SAFE** | 5 | 2 | 2 | 0 | **50.0%** *(2 pendentes)* |
| **SAFE+** | 5 | 2 | 1 | 0 | **66.7%** *(2 pendentes)* |
| **PRA CIMA** | 3 | 0 | 1 | 0 | **0.0%** *(2 pendentes)* |
| **Total Liquidado** | 8 | 4 | 4 | 0 | **50.0%** |

### B. Performance por Múltiplas / Bilhetes Combinados (Parlays)
| Bilhete / Múltipla | Total Disputado | GREEN (HIT) | RED (MISS) | PENDENTE | Taxa de Acerto (%) |
|---|---|---|---|---|---|
| **Bilhete SAFE** | 1 | 0 | 1 | 0 | **0.0%** |
| **Bilhete SAFE+** | 1 | 0 | 1 | 0 | **0.0%** |
| **Bilhete PRA CIMA (ATTACK)** | 1 | 0 | 1 | 0 | **0.0%** |
| **Bilhete APOSENTAR O NETO** | 1 | 0 | 1 | 0 | **0.0%** |

---

### [2026-09-23] — RODADA DIÁRIA (BASQUETE)

- **Snapshot ID:** `FAS_BASKETBALL_GEMINI_2026-09-23_V1`
- **Data do Registro:** 2026-09-23
- **Horário de Registro:** 01:10:00 BRT
- **Cutoff:** 2026-09-23T01:10:00-03:00
- **Contexto da Data:** Reta final da temporada regular da WNBA (2 confrontos cruciais para fechamento da tabela) e 2ª rodada da fase de grupos da FIBA Intercontinental Cup em Pequim.
- **Status de Liquidação:** `PENDING` (Jogos a serem disputados entre 08:30 BRT e 23:00 BRT)

#### 1. Discovery e Cobertura
- Encontrados: 4
- Elegíveis: 3
- Analisados: 3
- Descartados: 1 (Shanghai Sharks vs RSSB Tigers — TIER_C / Disparidade técnica sem linhas comerciais auditadas)

#### 2. Grade de Fixtures e Teses Pre-Match
1. **Beijing Royal Fighters vs NBA G League United** (FIBA Intercontinental Cup - Grupo B - 08:30 BRT)
   - *Tese:* Equipe da G-League americana possui superioridade atlética e profundidade de rotação contra o time chinês anfitrião.
   - **SAFE:** NBA G League United Vence (Moneyline) (FAS 91 | TIER_B | DQ HIGH | Risco LOW)
   - **SAFE+:** NBA G League United -6.5 Spread (FAS 85 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Mais de 168.5 Pontos (FAS 81 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

2. **Atlanta Dream @ New York Liberty** (WNBA - 18:00 BRT / 17:00 ET)
   - *Tese:* Reencontro direto após a zebra do dia 21. Liberty em casa buscando ajuste defensivo com Stewart e Ionescu; aplicação do novo protocolo: evitar Over cego e focar em resposta tática do Liberty com margem de segurança.
   - **SAFE:** New York Liberty +4.5 Spread Protegido (FAS 92 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** New York Liberty Vence (Moneyline) (FAS 86 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Menos de 169.5 Pontos (Ajuste de intensidade defensiva pós-derrota) (FAS 83 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

3. **Dallas Wings @ Seattle Storm** (WNBA - 23:00 BRT / 10:00 PM ET)
   - *Tese:* Storm em casa disputando posicionamento de mando para os playoffs; Wings eliminadas e com rotação encurtada. Defesa do Storm é top 3 em roubos e transição.
   - **SAFE:** Seattle Storm -5.5 Spread (FAS 90 | TIER_A | DQ HIGH | Risco LOW)
   - **SAFE+:** Seattle Storm Vence 1º Tempo (FAS 85 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Dallas Wings Team Total Under 79.5 (FAS 82 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

#### 3. Bilhetes Combinados / Múltiplas do Dia (Basquete)

*   🎫 **MÚLTIPLA 1 — SAFE (3 seleções):**
    *   Beijing vs G League: G League United Vence (ML)
    *   Atlanta @ New York: New York Liberty +4.5 Spread
    *   Dallas @ Seattle: Seattle Storm -5.5 Spread
    *   **Status:** `PENDING`

*   🎫 **MÚLTIPLA 2 — SAFE+ (3 seleções):**
    *   Beijing vs G League: G League United -6.5 Spread
    *   Atlanta @ New York: New York Liberty Vence (ML)
    *   Dallas @ Seattle: Seattle Storm Vence 1º Tempo
    *   **Status:** `PENDING`

*   🎫 **MÚLTIPLA 3 — PRA CIMA (Tripla de Ataque):**
    *   Beijing vs G League: Mais de 168.5 Pontos
    *   Atlanta @ New York: Menos de 169.5 Pontos
    *   Dallas @ Seattle: Dallas Wings Team Total Under 79.5
    *   **Status:** `PENDING`

*   🎫 **MÚLTIPLA 4 — APOSENTAR O NETO (Basquete Scanner / Cotação Alta):**
    *   G League United -6.5 + Liberty ML + Seattle 1º Tempo + Dallas Under 79.5 pts.
    *   **Status:** `PENDING`

#### 4. ⏰ Protocolo de Lembrete T-60min
*   **Primeiro Jogo da Rodada:** Beijing Royal Fighters vs NBA G League United (08:30 BRT)
*   **Horário de Check-in Pré-Jogo:** **07:30 BRT (T-60 minutos)**
*   **Para a WNBA (Primeiro jogo às 18:00 BRT):** Lembrete às **17:00 BRT**
*   **Checklist:** Checar Official Injury Report e shootaround da WNBA / escalação da FIBA. Governar: MANTER / ALTERAR / CANCELAR.
