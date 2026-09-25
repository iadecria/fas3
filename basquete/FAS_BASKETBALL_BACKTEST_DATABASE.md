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

4. **Golden State Valkyries 82 @ 90 Portland Fire** (OT) (23:00 BRT)
   - *Resultado Oficial:* 90 × 82 (78 × 78 no tempo regulamentar; Portland venceu no OT | Total: 172 pontos | Margem: Portland +8)
   - **SAFE:** Golden State Valkyries -8.5 ➔ ❌ **MISS** (Portland venceu 90x82)
     - *Miss Audit:* STATISTICAL_VARIANCE / UPSET (Valkyries abriu 17x0, mas sofreu apagão defensivo na reta final e caiu no OT diante de Portland descompromissado).
   - **SAFE+:** Golden State Vence 1º Tempo ➔ ✅ **HIT** (Valkyries venceu a primeira metade com folga)
   - **PRA CIMA:** Menos de 158.5 Pontos ➔ ❌ **MISS** (Prorrogação inflou placar para 172 pontos)
     - *Miss Audit:* STATISTICAL_VARIANCE

5. **Los Angeles Sparks 79 @ 89 Las Vegas Aces** (23:00 BRT)
   - *Resultado Oficial:* 89 × 79 (Total: 168 pontos | Margem: Las Vegas +10)
   - **SAFE:** Las Vegas Aces -9.5 ➔ ✅ **HIT** (89 - 79 = 10 > 9.5)
   - **SAFE+:** Las Vegas Aces 1º Tempo -6.5 ➔ ✅ **HIT** (Aces abriram vantagem no 1º tempo)
   - **PRA CIMA:** Las Vegas Aces -15.5 Spread ➔ ❌ **MISS** (Margem final travou em 10 pontos)
     - *Miss Audit:* STATISTICAL_VARIANCE

#### 3. Auditoria das Múltiplas / Bilhetes Combinados (Backtest de Bilhetes 22/09)

*   🎟️ **MÚLTIPLA SAFE (WNBA):**
    *   Sun @ Mystics: Mystics -9.5 ➔ ✅ HIT (79x69)
    *   Lynx @ Fever: Over 181.5 ➔ ❌ MISS (173 pts)
    *   Valkyries @ Fire: Valkyries -8.5 ➔ ❌ MISS (82x90)
    *   Sparks @ Aces: Aces -9.5 ➔ ✅ HIT (89x79)
    *   **Resultado da Múltipla SAFE:** ❌ **RED** (2 acertos, 2 erros)

*   🎟️ **MÚLTIPLA SAFE+ (WNBA):**
    *   Sun @ Mystics: Under 164.5 ➔ ✅ HIT (148 pts)
    *   Lynx @ Fever: Lynx +4.5 Spread ➔ ❌ MISS
    *   Tempo @ Sky: Sky ML ➔ ✅ HIT (97x85)
    *   Valkyries @ Fire: Valkyries 1ºT ➔ ✅ HIT
    *   Sparks @ Aces: Aces 1ºT -6.5 ➔ ✅ HIT
    *   **Resultado da Múltipla SAFE+:** ❌ **RED** (4 acertos, 1 erro - derrubada por Lynx +4.5)

*   🎟️ **MÚLTIPLA PRA CIMA (ATTACK):**
    *   Lynx @ Fever: Over 186.5 ➔ ❌ MISS
    *   Valkyries @ Fire: Under 158.5 ➔ ❌ MISS
    *   Sparks @ Aces: Aces -15.5 ➔ ❌ MISS
    *   **Resultado da Múltipla PRA CIMA:** ❌ **RED**

*   🎟️ **MÚLTIPLA APOSENTAR O NETO (Scanner / Alavancagem):**
    *   **Resultado:** ❌ **RED**

---

## 📊 PAINEL ACUMULADO DE BACKTEST (BASQUETE)

### A. Performance por Seleções Individuais (Singles)
| Categoria | Total Registrado | HIT | MISS | VOID | Win Rate (%) |
|---|---|---|---|---|---|
| **SAFE** | 7 | 3 | 4 | 0 | **42.9%** |
| **SAFE+** | 8 | 5 | 3 | 0 | **62.5%** |
| **PRA CIMA** | 6 | 1 | 5 | 0 | **16.7%** |
| **Total Liquidado** | 21 | 9 | 12 | 0 | **42.9%** |

### B. Performance por Múltiplas / Bilhetes Combinados (Parlays)
| Bilhete / Múltipla | Total Disputado | GREEN (HIT) | RED (MISS) | PENDENTE | Taxa de Acerto (%) |
|---|---|---|---|---|---|
| **Bilhete SAFE** | 2 | 0 | 2 | 0 | **0.0%** (2/4 pernas ontem, 1/3 hoje) |
| **Bilhete SAFE+** | 2 | 0 | 2 | 0 | **0.0%** (4/5 pernas ontem, 1/3 hoje) |
| **Bilhete PRA CIMA (ATTACK)** | 2 | 0 | 2 | 0 | **0.0%** (0/3 pernas ontem, 1/3 hoje) |
| **Bilhete APOSENTAR O NETO** | 2 | 0 | 2 | 0 | **0.0%** |

---

### [2026-09-23] - RODADA DIÁRIA (BASQUETE)

- **Snapshot ID:** FAS_BASKETBALL_GEMINI_2026-09-23_V1
- **Data do Registro:** 2026-09-23
- **Horário de Registro:** 01:10:00 BRT
- **Cutoff:** 2026-09-23T01:10:00-03:00
- **Contexto da Data:** Reta final da temporada regular da WNBA (2 confrontos cruciais para fechamento da tabela) e 2ª rodada da fase de grupos da FIBA Intercontinental Cup em Pequim.
- **Status de Liquidação:** **LIQUIDADO / AUDITADO**

#### 1. Discovery e Cobertura
- Encontrados: 4
- Elegíveis: 3
- Analisados: 3
- Descartados: 1 (Shanghai Sharks vs RSSB Tigers – TIER_C / Disparidade técnica sem linhas comerciais auditadas)

#### 2. Grade de Fixtures, Resultados e Liquidação

1. **Beijing Royal Fighters 89 vs 119 NBA G League United** (FIBA Intercontinental Cup - Grupo B - 08:30 BRT)
   - *Resultado Oficial:* 89 × 119 (Total: 208 pontos | Margem: G League +30)
   - **SAFE:** NBA G League United Vence (Moneyline) ➔ ✅ **HIT** (119x89)
   - **SAFE+:** NBA G League United -6.5 Spread ➔ ✅ **HIT** (G League venceu por 30 pontos)
   - **PRA CIMA:** Mais de 168.5 Pontos ➔ ✅ **HIT** (Total 208 pontos > 168.5)
   - *Observação:* Varredura de 100% de acerto nas 3 seleções.

2. **Atlanta Dream 95 @ 84 New York Liberty** (WNBA - 18:00 BRT / 17:00 ET)
   - *Resultado Oficial:* 95 × 84 (Total: 179 pontos | Margem: Atlanta +11)
   - **SAFE:** New York Liberty +4.5 Spread Protegido ➔ ❌ **MISS** (Liberty perdeu por 11 pontos: 84 - 95 = -11)
     - *Miss Audit:* STATISTICAL_VARIANCE / UPSET (Dream garantiu seed 4 nos playoffs com intensidade defensiva e alto aproveitamento perimetral; Liberty rodou titulares na reta final).
   - **SAFE+:** New York Liberty Vence (Moneyline) ➔ ❌ **MISS** (Placar 84x95)
     - *Miss Audit:* STATISTICAL_VARIANCE
   - **PRA CIMA:** Menos de 169.5 Pontos ➔ ❌ **MISS** (Total 179 pontos > 169.5)
     - *Miss Audit:* STATISTICAL_VARIANCE

3. **Dallas Wings 92 @ 70 Seattle Storm** (WNBA - 23:00 BRT / 10:00 PM ET)
   - *Resultado Oficial:* 92 × 70 (Total: 162 pontos | Margem: Dallas +22)
   - **SAFE:** Seattle Storm -5.5 Spread ➔ ❌ **MISS** (Seattle perdeu em casa por 22 pontos)
     - *Miss Audit:* STATISTICAL_VARIANCE / UPSET (Seattle já com seed travada atuou desmobilizado; Dallas abriu vantagem desde os minutos iniciais).
   - **SAFE+:** Seattle Storm Vence 1º Tempo ➔ ❌ **MISS** (Dallas liderou o primeiro tempo)
     - *Miss Audit:* STATISTICAL_VARIANCE
   - **PRA CIMA:** Dallas Wings Team Total Under 79.5 ➔ ❌ **MISS** (Dallas anotou 92 pontos)
     - *Miss Audit:* STATISTICAL_VARIANCE

#### 3. Auditoria das Múltiplas / Bilhetes Combinados (Backtest de Bilhetes 23/09)

*   🎟️ **MÚLTIPLA 1 - SAFE (3 seleções):**
    *   Beijing vs G League: G League United Vence (ML) ➔ ✅ HIT
    *   Atlanta @ New York: New York Liberty +4.5 Spread ➔ ❌ MISS
    *   Dallas @ Seattle: Seattle Storm -5.5 Spread ➔ ❌ MISS
    *   **Resultado da Múltipla SAFE:** ❌ **RED** (1 acerto, 2 erros)

*   🎟️ **MÚLTIPLA 2 - SAFE+ (3 seleções):**
    *   Beijing vs G League: G League United -6.5 Spread ➔ ✅ HIT
    *   Atlanta @ New York: New York Liberty Vence (ML) ➔ ❌ MISS
    *   Dallas @ Seattle: Seattle Storm Vence 1º Tempo ➔ ❌ MISS
    *   **Resultado da Múltipla SAFE+:** ❌ **RED** (1 acerto, 2 erros)

*   🎟️ **MÚLTIPLA 3 - PRA CIMA (Tripla de Ataque):**
    *   Beijing vs G League: Mais de 168.5 Pontos ➔ ✅ HIT
    *   Atlanta @ New York: Menos de 169.5 Pontos ➔ ❌ MISS
    *   Dallas @ Seattle: Dallas Wings Team Total Under 79.5 ➔ ❌ MISS
    *   **Resultado da Múltipla PRA CIMA:** ❌ **RED** (1 acerto, 2 erros)

*   🎟️ **MÚLTIPLA 4 - APOSENTAR O NETO (Basquete Scanner / Cotação Alta):**
    *   **Resultado:** ❌ **RED**

---

### [2026-09-24] — RODADA DIÁRIA (BASQUETE)

- **Snapshot ID:** `FAS_BASKETBALL_GEMINI_2026-09-24_V1`
- **Data do Registro:** 2026-09-24
- **Horário de Registro:** 00:20:00 BRT
- **Cutoff:** 2026-09-24T00:20:00-03:00
- **Contexto da Data:** Reta decisiva da fase de grupos da FIBA Intercontinental Cup em Pequim e encerramento da temporada regular da WNBA com definição das últimas vagas de playoffs.
- **Status de Liquidação:** **PARCIALMENTE AUDITADO / EM FINALIZAÇÃO**

#### 1. Discovery e Cobertura
- Encontrados: 5
- Elegíveis: 3
- Analisados: 3
- Descartados: 2 (Jogos amistosos europeus de pré-temporada sem liquidez)

#### 2. Grade de Fixtures, Resultados e Liquidação

1. **Boca Juniors 74 × 79 NBA G League United** (FIBA Intercontinental Cup - 08:30 BRT)
   - *Resultado Oficial:* 74 × 79 (Total: 153 pontos | Margem: G League +5)
   - **SAFE:** NBA G League United Vence (Moneyline) ➔ ✅ **HIT** (G League venceu por 79x74)
   - **SAFE+:** NBA G League United -7.5 Spread ➔ ❌ **MISS** (Venceu por 5 pontos; faltou cobrir o handicap)
     - *Miss Audit:* `STATISTICAL_VARIANCE` (Boca desacelerou o ritmo de jogo no 4º quarto com posses longas e evitou a dilatação do placar).
   - **PRA CIMA:** NBA G League United Team Total Over 89.5 Pontos ➔ ❌ **MISS** (G League anotou 79 pontos)
     - *Miss Audit:* `STATISTICAL_VARIANCE`

2. **Indiana Fever 66 @ 86 Minnesota Lynx** (WNBA - 21:00 BRT / 8:00 PM ET)
   - *Resultado Oficial:* 66 × 86 (Total: 152 pontos | Margem: Lynx +20)
   - **SAFE:** Mais de 166.5 Pontos ➔ ❌ **MISS** (Total 152 pontos < 166.5)
     - *Miss Audit:* `STATISTICAL_VARIANCE` (Defesa sufocante do Lynx no Target Center segurou o Fever em apenas 66 pontos).
   - **SAFE+:** Minnesota Lynx Vence (Moneyline) ➔ ✅ **HIT** (Lynx venceu com folga 86x66)
   - **PRA CIMA:** Indiana Fever +5.5 Spread + Mais de 168.5 Pontos ➔ ❌ **MISS**
     - *Miss Audit:* `STATISTICAL_VARIANCE`

3. **Golden State Valkyries @ Los Angeles Sparks** (WNBA - 20:00 BRT / 7:00 PM ET)
   - *Status da Partida:* Concluída na Costa Oeste (Madrugada BRT); súmula e box score oficial em processo de consolidação de estatísticas.
   - **SAFE:** Golden State Valkyries Vence (Moneyline) ➔ `PENDING_CONFIRMATION`
   - **SAFE+:** Golden State Valkyries -4.5 Spread ➔ `PENDING_CONFIRMATION`
   - **PRA CIMA:** Sparks Team Total Under 78.5 ➔ `PENDING_CONFIRMATION`

#### 3. 👴 APOSENTAR O NETO — Principais Linhas (Scanner Completo)

**Boca Juniors vs NBA G League United**
- 🔥🔥🔥 G League United Vence (ML) — 95 ➔ ✅ HIT
- 🔥🔥 G League United -7.5 Spread — 88 ➔ ❌ MISS
- 🔥 G League United Team Total Over 89.5 — 84 ➔ ❌ MISS
- 🔥 Mais de 168.5 Pontos — 82 ➔ ❌ MISS
- 🟢 Boca Juniors Under 82.5 — 79 ➔ ✅ HIT

**Indiana Fever @ Minnesota Lynx**
- 🔥🔥🔥 Mais de 166.5 Pontos — 91 ➔ ❌ MISS
- 🔥🔥 Minnesota Lynx Vence (ML) — 85 ➔ ✅ HIT
- 🔥 Indiana Fever +5.5 Spread — 83 ➔ ❌ MISS
- 🔥 Mais de 168.5 Pontos — 82 ➔ ❌ MISS
- 🟢 Indiana Fever Team Total Over 81.5 — 78 ➔ ❌ MISS

**Golden State Valkyries @ Los Angeles Sparks**
- 🔥🔥🔥 Valkyries Vence (ML) — 93 ➔ `PENDING`
- 🔥🔥 Valkyries -4.5 Spread — 86 ➔ `PENDING`
- 🔥 Sparks Team Total Under 78.5 — 81 ➔ `PENDING`
- 🟢 Menos de 164.5 Pontos — 78 ➔ `PENDING`

#### 4. Bilhetes Combinados / Múltiplas do Dia (Backtest 24/09)

*   🎟️ **MÚLTIPLA 1 — SAFE (Formato Modular com Stop Points):**
    *   🥇 **#1 [ÂNCORA PRIMÁRIA]:** Boca vs G League: G League United Vence (ML) ➔ ✅ **HIT** (79x74)
    *   🥈 **#2 [ÂNCORA SECUNDÁRIA]:** Valkyries @ Sparks: Golden State Valkyries Vence (ML) ➔ `PENDING`
    *   🟢 **STOP POINT 1 ➔ DUPLA ÂNCORA (Top 1 + Top 2):** G League ML (HIT) + Valkyries ML *(Aguardando confirmação oficial da Costa Oeste)*
    *   🥉 **#3 [EXPANSÃO TRIPLA]:** Fever @ Lynx: Mais de 166.5 Pontos ➔ ❌ MISS (152 pts)
    *   🟡 **STOP POINT 2 ➔ TRIPLA EQUILIBRADA:** ❌ **RED** (derrubada pelo Under do Lynx)
    *   **Status:** `PARCIAL`

*   🎟️ **MÚLTIPLA 2 — SAFE+ (Formato Modular):**
    *   🥇 #1 G League United -7.5 Spread ➔ ❌ MISS (venceu por 5)
    *   🥈 #2 Golden State Valkyries -4.5 Spread ➔ `PENDING`
    *   🥉 #3 Minnesota Lynx Vence (ML) ➔ ✅ HIT (86x66)
    *   **Resultado da Múltipla SAFE+:** ❌ **RED** (derrubada pelo spread do G League)

*   🎟️ **MÚLTIPLA 3 — PRA CIMA (Tripla de Valor):**
    *   G League United Team Total Over 89.5 Pontos
    *   Fever @ Lynx: Fever +5.5 + Over 168.5 Pontos
    *   Sparks Team Total Under 78.5 Pontos
    *   **Status:** `PENDING`

*   🎟️ **MÚLTIPLA 4 — APOSENTAR O NETO (Alavancagem Máxima da Rodada):**
    *   G League -7.5 + Valkyries -4.5 + Lynx ML + Fever Over 168.5 + Sparks Under 78.5.
    *   **Status:** `PENDING`

#### 4. ⏰ Protocolo de Lembrete T-60min
*   **Primeiro Jogo FIBA:** Boca vs G League (08:30 BRT) ➔ Lembrete às **07:30 BRT**
*   **Primeiro Jogo WNBA:** Valkyries @ Sparks (20:00 BRT) ➔ Lembrete às **19:00 BRT**
*   **Checklist:** Injury reports oficiais e confirmação de minutos dos titulares.

---

### [2026-09-25] — RODADA DIÁRIA (BASQUETE V2.0 BLINDADO)

- **Snapshot ID:** `FAS_BASKETBALL_GEMINI_2026-09-25_V1`
- **Data do Registro:** 2026-09-25
- **Horário de Registro:** 00:52:00 BRT
- **Cutoff:** 2026-09-25T13:00:00-03:00
- **Contexto da Data:** Abertura da temporada 2026/27 da EuroLeague Basketball (Rodada 1). Dia de descanso na FIBA Intercontinental Cup e entressafra de playoffs da WNBA.
- **Protocolo de Blindagem Ativo:** **SAFE Quality Gates V2.0** (Veto a Spreads Negativos em SAFE, Veto a Linhas Cheias de Over, Foco em Moneyline de Favorito e Handicap Positivo Protegido).
- **Status de Liquidação:** `PENDING`

#### 1. Discovery e Cobertura
- Encontrados: 4
- Elegíveis: 3
- Analisados: 3 (Fenerbahçe x Virtus Bologna, Partizan x Olimpia Milano, Beşiktaş x Valencia Basket)
- Descartados: 1 (Brisbane Bullets x Illawarra Hawks na NBL — jogo das 06:30 BRT matutino de alta volatilidade)

#### 2. Grade de Fixtures e Teses Pre-Match (V2.0)

1. **Fenerbahçe SK vs Virtus Segafredo Bologna** (EuroLeague - Rodada 1 - 14:45 BRT)
   - *Tese:* Fenerbahçe atua na Ülker Sports Arena em Istambul com um elenco estelar (Will Clyburn, Shane Larkin e Sertaç Şanlı). Virtus Bologna com 9 novos atletas e 7 estreantes na EuroLeague. Aplicação da Regra V2.0: proibido spread negativo arriscado (-7.5) na SAFE. Foco na vitória seca absoluta.
   - **SAFE:** Fenerbahçe Vence (Moneyline) (FAS 97 | DQ HIGH | VERY_HIGH | Risco LOW)
   - **SAFE+:** Fenerbahçe Vence o 1º Tempo (1H ML) (FAS 91 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Fenerbahçe -7.5 Spread (FAS 84 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

2. **KK Partizan NIS vs Olimpia Milano** (EuroLeague - Rodada 1 - 15:45 BRT)
   - *Tese:* Caldeirão da Stark Arena em Belgrado com a torcida mais fervorosa da Europa. O Partizan impõe um jogo físico e intensidade de contato brutal que Milano historicamente sofre para conter em estreias fora de casa.
   - **SAFE:** Partizan NIS +4.5 Spread Positivo Protegido (FAS 93 | DQ HIGH | VERY_HIGH | Risco LOW)
   - **SAFE+:** Partizan NIS Vence (Moneyline) (FAS 87 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Partizan NIS Vence o 1º Tempo (FAS 82 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

3. **Beşiktaş J.K. vs Valencia Basket** (EuroLeague - Rodada 1 - 14:00 BRT)
   - *Tese:* Beşiktaş retorna à EuroLeague diante do experiente Valencia Basket da Liga ACB. Jogo inaugural tenso e de ajuste de elenco. Linha de handicap positivo protege o time espanhol contra oscilações de placar.
   - **SAFE:** Valencia Basket +5.5 Spread Positivo Protegido (FAS 91 | DQ HIGH | VERY_HIGH | Risco LOW)
   - **SAFE+:** Valencia Basket Vence (Moneyline) (FAS 84 | DQ HIGH | Risco LOW_MEDIUM)
   - **PRA CIMA:** Menos de 162.5 Pontos (Under de Estreia) (FAS 80 | DQ HIGH | Risco MEDIUM)
   - **Status:** `PENDING`

#### 3. 👴 APOSENTAR O NETO — Principais Linhas (Scanner Completo)

**Fenerbahçe vs Virtus Bologna**
- 🔥🔥🔥 Fenerbahçe Vence (ML) — 97
- 🔥🔥 Fenerbahçe Vence 1º Tempo — 91
- 🔥 Fenerbahçe -7.5 Spread — 84
- 🟢 Mais de 158.5 Pontos — 80
- 🟢 Virtus Bologna Under 76.5 — 82

**KK Partizan vs Olimpia Milano**
- 🔥🔥🔥 Partizan +4.5 Spread — 93
- 🔥🔥 Partizan Vence (ML) — 87
- 🔥 Partizan Vence 1º Tempo — 82
- 🟢 Menos de 164.5 Pontos — 79
- 🟢 Milano Under 80.5 — 81

**Beşiktaş vs Valencia Basket**
- 🔥🔥🔥 Valencia Basket +5.5 Spread — 91
- 🔥🔥 Valencia Basket Vence (ML) — 84
- 🔥 Menos de 162.5 Pontos — 80
- 🟢 Beşiktaş Under 81.5 — 78

#### 4. Bilhetes Combinados / Múltiplas do Dia (Arquitetura Modular Rankeada V2.0)

*   🎟️ **MÚLTIPLA 1 — SAFE (Formato Modular com Stop Points) [BOLETIM OFICIAL REGISTRADO]:**
    *   🥇 **#1 [ÂNCORA PRIMÁRIA]:** Fenerbahçe Vence (Moneyline) (FAS 97) ➔ **Odd Real: @1.10**
    *   🥈 **#2 [ÂNCORA SECUNDÁRIA]:** Partizan NIS +4.5 Spread Positivo (FAS 93) ➔ **Odd Real: @1.28**
    *   🟢 **STOP POINT 1 ➔ DUPLA ÂNCORA (Top 1 + Top 2):** Fenerbahçe ML + Partizan +4.5 *(Odd combinada: **@1.41** | Dupla de Máxima Blindagem)*.
    *   🥉 **#3 [EXPANSÃO TRIPLA]:** Valencia Basket +5.5 Spread Positivo (FAS 91) ➔ **Odd Real: @1.50**
    *   🟡 **STOP POINT 2 ➔ TRIPLA EQUILIBRADA (Top 1 + Top 2 + Top 3):** *(Odd combinada real: **@2.12**)*
    *   **Status:** `PENDING (AGUARDANDO LIQUIDAÇÃO AMANHÃ)`

*   🎟️ **MÚLTIPLA 2 — SAFE+ (Formato Modular):**
    *   🥇 #1 Fenerbahçe Vence 1º Tempo
    *   🥈 #2 Partizan NIS Vence (Moneyline)
    *   🟢 **STOP POINT 1 ➔ Dupla SAFE+**
    *   🥉 #3 Valencia Basket Vence (Moneyline)
    *   🟡 **STOP POINT 2 ➔ Tripla SAFE+**
    *   **Status:** `PENDING`

*   🎟️ **MÚLTIPLA 3 — PRA CIMA (Tripla de Alta Assimetria):**
    *   Fenerbahçe -7.5 Spread + Partizan 1ºT ML + Beşiktaş/Valencia Under 162.5.
    *   **Status:** `PENDING`

#### 5. ⏰ Protocolo de Lembrete T-60min
*   **Primeiro Jogo (EuroLeague):** 14:00 BRT (Beşiktaş x Valencia) ➔ Lembrete às **13:00 BRT**
*   **Segundo Jogo:** 14:45 BRT (Fenerbahçe x Bologna) ➔ Lembrete às **13:45 BRT**
*   **Terceiro Jogo:** 15:45 BRT (Partizan x Milano) ➔ Lembrete às **14:45 BRT**
*   **Checklist:** Injury reports oficiais da EuroLeague Basketball.


