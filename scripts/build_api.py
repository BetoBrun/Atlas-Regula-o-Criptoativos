from pathlib import Path
import json
from datetime import datetime

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / 'data' / 'manual-overrides.json'
API = BASE / 'api'
COUNTRY_DIR = API / 'country'
COUNTRY_DIR.mkdir(parents=True, exist_ok=True)

WEIGHTS = {
    'legal_certainty': 20,
    'proportionality': 15,
    'exchanges': 10,
    'stablecoins': 10,
    'tokenization': 10,
    'taxation': 10,
    'mining_infrastructure': 10,
    'innovation_openness': 10,
    'anti_centralization': 5,
}


def compute_score(criteria: dict) -> int:
    return int(round(sum(criteria.get(k, 0) for k in WEIGHTS)))


def classify(score: int) -> str:
    if score >= 80:
        return 'very_favorable'
    if score >= 65:
        return 'favorable'
    if score >= 50:
        return 'mixed'
    if score >= 35:
        return 'restrictive'
    return 'very_restrictive'


def main() -> None:
    payload = json.loads(DATA.read_text(encoding='utf-8'))
    countries = payload['countries']
    for c in countries:
        c['score'] = compute_score(c['criteria'])
        c['classification'] = classify(c['score'])

    countries_sorted = sorted(countries, key=lambda x: x['score'], reverse=True)
    rankings = {
        'top_favorable': countries_sorted[:10],
        'top_restrictive': list(reversed(countries_sorted[-10:])),
    }
    updates = sorted(
        [{'country': c['country'], 'iso3': c['iso3'], 'last_update': c['last_update'], 'trend': c['trend'], 'score': c['score']} for c in countries],
        key=lambda x: x['last_update'], reverse=True
    )
    metadata = {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'country_count': len(countries),
        'methodology_version': '1.1.0-bilingual'
    }
    (API / 'countries.json').write_text(json.dumps(countries, ensure_ascii=False, indent=2), encoding='utf-8')
    (API / 'rankings.json').write_text(json.dumps(rankings, ensure_ascii=False, indent=2), encoding='utf-8')
    (API / 'updates.json').write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding='utf-8')
    (API / 'metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    for c in countries:
        (COUNTRY_DIR / f"{c['iso3']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
