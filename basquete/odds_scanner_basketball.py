"""
FAS Basketball - Odds Scanner & Ticket Multiplier
Consulta cotações reais de Basquete (WNBA, NBA, EuroLeague, FIBA) e monta os bilhetes para a Pinnacle e Bet365.
"""

import json
import urllib.request
import sys
import os
from typing import Dict, List, Any

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "2949bd401486c8c955216b3fb58c68c4"
BASE_URL = "https://api.the-odds-api.com/v4"

def get_basketball_sports() -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/sports/?apiKey={API_KEY}"
    req = urllib.request.Request(url, headers={"User-Agent": "FAS-Basketball/1.0"})
    with urllib.request.urlopen(req) as resp:
        sports = json.loads(resp.read().decode("utf-8"))
        return [s for s in sports if s.get("group") == "Basketball" and s.get("active")]

def get_basketball_odds(sport_key: str, regions: str = "eu,us", markets: str = "h2h,spreads,totals") -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/sports/{sport_key}/odds/?apiKey={API_KEY}&regions={regions}&markets={markets}"
    req = urllib.request.Request(url, headers={"User-Agent": "FAS-Basketball/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def print_basketball_pinnacle_slip(tickets: List[Dict[str, Any]]):
    print("\n" + "="*55)
    print("🏀 GUIA DE EXECUÇÃO: BOLETIM OFICIAL BASQUETE PINNACLE")
    print("="*55)
    for idx, t in enumerate(tickets, 1):
        print(f"\n🎫 {t['title']} — Multiplicador: @{t['multiplier']:.2f}")
        print(f"💰 Retorno com R$ 50: R$ {50 * t['multiplier']:.2f} | Com R$ 100: R$ {100 * t['multiplier']:.2f}")
        print("📌 Passo a passo no site:")
        for s in t['legs']:
            print(f"   ▫️ Jogo: {s['match']}")
            print(f"      ➔ Categoria: [{s['market_group']}]")
            print(f"      ➔ Linha: {s['selection']} (Odd Pinnacle: @{s['odd']})")
        print(f"   👉 No boletim da Pinnacle, selecione a aba 'ACUMULADA' / 'PARLAY' e confirme!")

if __name__ == "__main__":
    print("--- SCANNER BASQUETE THE ODDS API ---")
    active_b = get_basketball_sports()
    print(f"Ligas de Basquete Ativas: {len(active_b)}")
    for s in active_b:
        print(f"- {s.get('key')}: {s.get('title')}")
