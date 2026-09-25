"""
FAS 3 - Odds Scanner & Ticket Multiplier
Calcula as melhores odds por casa de apostas para os jogos do FAS.
"""

import json
import urllib.request
import sys
from typing import Dict, List, Any

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "2949bd401486c8c955216b3fb58c68c4"
BASE_URL = "https://api.the-odds-api.com/v4"

def get_nations_league_odds() -> List[Dict[str, Any]]:
    # Traz mercados de h2h e totals
    url = f"{BASE_URL}/sports/soccer_uefa_nations_league/odds/?apiKey={API_KEY}&regions=eu,uk&markets=h2h,totals"
    req = urllib.request.Request(url, headers={"User-Agent": "FAS3-OddsClient/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_serie_b_odds() -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/sports/soccer_brazil_serie_b/odds/?apiKey={API_KEY}&regions=eu,uk&markets=h2h,totals"
    req = urllib.request.Request(url, headers={"User-Agent": "FAS3-OddsClient/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def calculate_double_chance_odd(home_odd: float, draw_odd: float) -> float:
    """Calcula a odd justa/comercial de Dupla Chance 1X a partir de Home e Draw"""
    if not home_odd or not draw_odd:
        return 0.0
    prob = (1.0 / home_odd) + (1.0 / draw_odd)
    return round(1.0 / prob, 2)

def analyze_match_odds(match: Dict[str, Any]):
    home = match.get("home_team")
    away = match.get("away_team")
    time_str = match.get("commence_time")
    
    print(f"\n==========================================")
    print(f"⚽ {home} x {away} ({time_str})")
    print(f"==========================================")
    
    bookmakers = match.get("bookmakers", [])
    
    # Mapear odds de 1X2 e Totals por casa
    results_by_bookie = {}
    
    for b in bookmakers:
        b_name = b.get("title")
        markets = {m.get("key"): m for m in b.get("markets", [])}
        
        h2h = markets.get("h2h", {}).get("outcomes", [])
        totals = markets.get("totals", {}).get("outcomes", [])
        
        home_odd = next((o.get("price") for o in h2h if o.get("name") == home), None)
        away_odd = next((o.get("price") for o in h2h if o.get("name") == away), None)
        draw_odd = next((o.get("price") for o in h2h if o.get("name") == "Draw"), None)
        
        # 1X
        dc_1x = calculate_double_chance_odd(home_odd, draw_odd) if (home_odd and draw_odd) else None
        
        # Over 1.5 e Over 2.5
        o15_odd = next((o.get("price") for o in totals if o.get("name") == "Over" and o.get("point") == 1.5), None)
        o25_odd = next((o.get("price") for o in totals if o.get("name") == "Over" and o.get("point") == 2.5), None)
        u35_odd = next((o.get("price") for o in totals if o.get("name") == "Under" and o.get("point") == 3.5), None)
        
        results_by_bookie[b_name] = {
            "Home": home_odd,
            "Draw": draw_odd,
            "Away": away_odd,
            "1X": dc_1x,
            "Over 1.5": o15_odd,
            "Over 2.5": o25_odd,
            "Under 3.5": u35_odd,
        }
    
    # Exibir principais casas
    priority_casas = ["Pinnacle", "Betfair", "Betsson", "1xBet", "Marathon Bet", "Suprabets", "William Hill"]
    for casa in priority_casas:
        if casa in results_by_bookie:
            info = results_by_bookie[casa]
            line_str = f"  🏦 {casa:<14} | "
            if info["Home"]: line_str += f"Casa: @{info['Home']} | "
            if info["Draw"]: line_str += f"Empate: @{info['Draw']} | "
            if info["Away"]: line_str += f"Fora: @{info['Away']} | "
            if info["1X"]: line_str += f"1X: @{info['1X']} | "
            if info["Over 1.5"]: line_str += f"O1.5: @{info['Over 1.5']} | "
            if info["Over 2.5"]: line_str += f"O2.5: @{info['Over 2.5']} | "
            print(line_str)

def print_pinnacle_slip(tickets: List[Dict[str, Any]]):
    print("\n" + "="*55)
    print("📋 GUIA DE EXECUÇÃO: BOLETIM OFICIAL PINNACLE (pinnacle.bet.br)")
    print("="*55)
    for idx, t in enumerate(tickets, 1):
        print(f"\n🎫 {t['title']} — Multiplicador: @{t['multiplier']:.2f}")
        print(f"💰 Retorno com R$ 50: R$ {50 * t['multiplier']:.2f} | Com R$ 100: R$ {100 * t['multiplier']:.2f}")
        print("📌 Passo a passo no site:")
        for s in t['legs']:
            print(f"   ▫️ Jogo: {s['match']}")
            print(f"      ➔ Categoria: [{s['market_group']}]")
            print(f"      ➔ Linha: {s['selection']} (Odd Pinnacle: @{s['odd']})")
        print(f"   👉 No boletim à direita, clique na aba 'ACUMULADA' / 'PARLAY' e confirme!")

def print_soros_slip():
    import os
    state_file = os.path.join(os.path.dirname(__file__), "soros_state.json")
    if not os.path.exists(state_file):
        return
    with open(state_file, "r", encoding="utf-8") as f:
        state = json.load(f)
        
    day = state.get("currentDay", 1)
    stake = state.get("currentStake", 10.0)
    target_days = state.get("targetDays", 30)
    
    # Seleção do Soros: Âncora de Máxima Proteção da Rodada (Dupla Âncora SAFE)
    # França Over 1.5 (@1.21) ou França ML (@1.39) + Itália AH +0.5 (@1.39)
    # Para Soros, usamos a proteção de elite do FAS
    mult = 1.39 * 1.39  # @1.93 na Pinnacle
    ret = stake * mult
    
    print("\n" + "="*55)
    print(f"🔥 DESAFIO SOROS FAS 30 DIAS — DIA {day} DE {target_days}")
    print("="*55)
    print(f"💵 Entrada de Hoje: R$ {stake:.2f} (Tudo o que temos da jornada)")
    print(f"🎯 Cotação da Dupla Âncora: @{mult:.2f} (Pinnacle)")
    print(f"💰 Retorno Estimado se Bater: R$ {ret:.2f}")
    print(f"🚀 Próximo Passo: Se GREEN, os R$ {ret:.2f} serão a entrada do DIA {day + 1}!")
    print("\n📌 Seleções Obrigatórias do Soros:")
    print("   1️⃣ Turquia x França ➔ França Vence (Odd @1.39)")
    print("   2️⃣ Itália x Bélgica ➔ Handicap Asiático: Itália (+0.5) (Odd @1.39)")
    print("   👉 Na Pinnacle: Adicione os dois, vá na aba ACUMULADA e coloque R$ 10,00!")
    print("="*55)

if __name__ == "__main__":
    matches = get_nations_league_odds()
    target_fixtures = ["Turkey", "Italy", "Sweden", "Poland", "Hungary", "Georgia"]
    
    for m in matches:
        if any(t in m.get("home_team", "") or t in m.get("away_team", "") for t in target_fixtures):
            analyze_match_odds(m)
            
    print("\n\n================ BRASILEIRÃO SÉRIE B ================")
    try:
        serie_b = get_serie_b_odds()
        for m in serie_b:
            analyze_match_odds(m)
    except Exception as e:
        print(f"Erro Série B: {e}")

    # Boletim Especial Pinnacle para a Rodada de 25/09
    pinnacle_tickets = [
        {
            "title": "BILHETE 1: DUPLA ÂNCORA (SAFE - Menor Risco)",
            "multiplier": 1.39 * 1.39,  # França ML @1.39 x Itália AH +0.5 @1.39 = ~1.93
            "legs": [
                {
                    "match": "Turquia x França (UEFA Nations League - 15:45 BRT)",
                    "market_group": "Resultado da Partida / Linha de Dinheiro (1X2)",
                    "selection": "França Vence (Fora / 2)",
                    "odd": 1.39
                },
                {
                    "match": "Itália x Bélgica (UEFA Nations League - 15:45 BRT)",
                    "market_group": "Handicap / Handicap Asiático",
                    "selection": "Itália (+0.5) [Equivalente exato a 1X / Dupla Chance]",
                    "odd": 1.39
                }
            ]
        },
        {
            "title": "BILHETE 2: TRIPLA DE OURO (Equilibrada)",
            "multiplier": 1.39 * 1.39 * 1.48,  # ~2.86
            "legs": [
                {
                    "match": "Turquia x França (15:45 BRT)",
                    "market_group": "Resultado da Partida (1X2)",
                    "selection": "França Vence",
                    "odd": 1.39
                },
                {
                    "match": "Itália x Bélgica (15:45 BRT)",
                    "market_group": "Handicap Asiático",
                    "selection": "Itália (+0.5) [Equivalente exato a 1X]",
                    "odd": 1.39
                },
                {
                    "match": "Suécia x Romênia (15:45 BRT)",
                    "market_group": "Resultado da Partida (1X2)",
                    "selection": "Suécia Vence",
                    "odd": 1.48
                }
            ]
        }
    ]
    print_pinnacle_slip(pinnacle_tickets)
    print_soros_slip()


