"""Deterministic hypothetical teaching model; NOT observed 1983 market data.
All coefficients and budgets were selected for illustration, not estimated.
"""
from math import isfinite

MODEL_VERSION = '1.0'
DEFAULTS = dict(confidence=65, sell_pressure=50, bank_capacity=55, intervention='early')


def validate_inputs(data):
    if not isinstance(data, dict):
        raise ValueError('יש לשלוח אובייקט JSON עם ארבעה פרמטרים.')
    if set(data) != set(DEFAULTS):
        raise ValueError('חובה לספק confidence, sell_pressure, bank_capacity, intervention בלבד.')
    clean = {}
    for key in ('confidence','sell_pressure','bank_capacity'):
        value = data[key]
        if isinstance(value,bool) or not isinstance(value,int) or value < 0 or value > 100:
            raise ValueError(f'{key}: יש לשלוח מספר שלם בין 0 ל־100.')
        clean[key] = value
    if data['intervention'] not in ('none','delayed','early'):
        raise ValueError('intervention: הערכים המותרים הם none, delayed, early.')
    clean['intervention'] = data['intervention']
    return clean


def simulate(data):
    p = validate_inputs(data)
    index, bank_remaining, state_remaining = 100., p['bank_capacity']*3.2, 75.
    used_bank = 0.
    used_public = 0.
    points = []
    for t in range(1,13):
        demand = max(0., min(100., 4 + .18*p['sell_pressure'] + .12*(100-p['confidence']) + .10*(100-index)))
        bank = min(demand, 12., bank_remaining)
        bank_remaining -= bank
        public = 0.
        eligible = p['intervention']=='early' or (p['intervention']=='delayed' and t>=6)
        if eligible:
            public = min(max(0., demand-bank), 8., state_remaining)
            state_remaining -= public
        unmet = max(0., demand-bank-public)
        index = max(0., min(100., index-.28*unmet))
        used_bank += bank
        used_public += public
        points.append({
            'period':t,'stability_index':round(index,3),'sell_demand':round(demand,3),
            'bank_support_used':round(bank,3),'public_support_used':round(public,3),
            'unmet_demand':round(unmet,3),'bank_remaining':round(bank_remaining,3),
            'public_remaining':round(state_remaining,3)
        })
    summary = ('בהנחות המודל, התערבות ציבורית יכולה לספוג חלק מהלחץ שלא נספג — '
               'אך גם המשאבים הציבוריים מוגבלים.' if used_public else
               'בהנחות המודל, ללא התערבות ציבורית הלחץ שנותר משפיע על מדד היציבות.')
    return dict(model_version=MODEL_VERSION,historical=False,inputs=p,periods=points,
        summary=dict(last_stability_index=points[-1]['stability_index'],
                     bank_used=round(used_bank,3),public_used=round(used_public,3),
                     description_he=summary))
