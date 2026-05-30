"""
AERIS - Complete Dataset Generator
Generates realistic aviation personnel and fleet data with compliance flags
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict

np.random.seed(42)

def generate_flight_deck_crew(num_pilots: int = 500) -> pd.DataFrame:
    """Generate flight deck crew with EASA/FAA/GACA compliance"""
    
    ranks = ['Captain', 'Senior First Officer', 'First Officer', 'Second Officer']
    rank_weights = [0.25, 0.20, 0.40, 0.15]
    
    aircraft_ratings = ['A320', 'A350', 'A380', 'B777', 'B777ER', 'B787']
    
    data = {
        'pilot_id': [f'PL{str(i).zfill(4)}' for i in range(1, num_pilots + 1)],
        'rank': np.random.choice(ranks, num_pilots, p=rank_weights),
        'aircraft_rating': np.random.choice(aircraft_ratings, num_pilots),
        'base': np.random.choice(['RUH', 'JED', 'DMM', 'MED'], num_pilots, p=[0.55, 0.25, 0.12, 0.08]),
        'total_hours': np.random.randint(500, 15000, num_pilots),
        'hours_30d': np.random.randint(20, 100, num_pilots),
        'hours_7d': np.random.randint(5, 35, num_pilots),
        'hours_24h': np.random.randint(0, 14, num_pilots),
        'nights_7d': np.random.randint(0, 20, num_pilots),
        'medical_valid': [datetime.now() + timedelta(days=np.random.randint(1, 365)) for _ in range(num_pilots)],
        'license_valid': [datetime.now() + timedelta(days=np.random.randint(1, 730)) for _ in range(num_pilots)],
        'status': np.random.choice(['Active', 'Leave', 'Training'], num_pilots, p=[0.85, 0.10, 0.05])
    }
    
    df = pd.DataFrame(data)
    df['easa_compliant'] = (df['hours_24h'] <= 13) & (df['hours_30d'] <= 100)
    df['faa_compliant'] = (df['hours_24h'] <= 9) & (df['hours_30d'] <= 100)
    df['gaca_compliant'] = (df['hours_24h'] <= 13) & (df['hours_7d'] <= 60)
    df['fatigue_score'] = (df['hours_7d'] / 60 * 0.6) + (df['nights_7d'] / 20 * 0.4)
    
    return df

def generate_cabin_crew(num_crew: int = 1200) -> pd.DataFrame:
    ranks = ['Purser', 'Senior Cabin Crew', 'Cabin Crew', 'Trainee']
    rank_weights = [0.12, 0.25, 0.53, 0.10]
    
    data = {
        'cc_id': [f'CC{str(i).zfill(5)}' for i in range(1, num_crew + 1)],
        'rank': np.random.choice(ranks, num_crew, p=rank_weights),
        'base': np.random.choice(['RUH', 'JED', 'DMM', 'MED'], num_crew, p=[0.50, 0.25, 0.15, 0.10]),
        'total_hours': np.random.randint(200, 8000, num_crew),
        'hours_30d': np.random.randint(30, 100, num_crew),
        'hours_7d': np.random.randint(10, 35, num_crew),
        'training_valid': [datetime.now() + timedelta(days=np.random.randint(1, 365)) for _ in range(num_crew)],
        'languages': np.random.randint(1, 5, num_crew),
        'status': np.random.choice(['Active', 'Leave', 'Training'], num_crew, p=[0.88, 0.07, 0.05])
    }
    
    df = pd.DataFrame(data)
    df['compliance_ready'] = df['training_valid'] > datetime.now()
    df['fatigue_score'] = df['hours_7d'] / 35
    return df

def generate_engineering_staff(num_engineers: int = 300) -> pd.DataFrame:
    certs = ['A', 'B1', 'B2', 'C']
    cert_weights = [0.30, 0.35, 0.20, 0.15]
    
    data = {
        'eng_id': [f'ENG{str(i).zfill(4)}' for i in range(1, num_engineers + 1)],
        'certification': np.random.choice(certs, num_engineers, p=cert_weights),
        'specialization': np.random.choice(['Airframe', 'Powerplant', 'Avionics', 'Line'], num_engineers),
        'aircraft_rated': np.random.choice(['A320', 'A350', 'B787', 'Multiple'], num_engineers),
        'experience_years': np.random.uniform(2, 25, num_engineers),
        'license_valid': [datetime.now() + timedelta(days=np.random.randint(30, 730)) for _ in range(num_engineers)],
        'status': np.random.choice(['Active', 'Training'], num_engineers, p=[0.92, 0.08])
    }
    
    df = pd.DataFrame(data)
    df['part145_compliant'] = df['license_valid'] > datetime.now()
    return df

def generate_fleet() -> pd.DataFrame:
    aircraft_specs = {
        'A320': {'count': 20, 'captains': 2, 'cabin': 4},
        'A350': {'count': 15, 'captains': 2, 'cabin': 8},
        'A380': {'count': 5, 'captains': 2, 'cabin': 18},
        'B777': {'count': 12, 'captains': 2, 'cabin': 8},
        'B777ER': {'count': 8, 'captains': 2, 'cabin': 8},
        'B787': {'count': 18, 'captains': 2, 'cabin': 7}
    }
    
    fleet = []
    for ac_type, spec in aircraft_specs.items():
        for i in range(spec['count']):
            fleet.append({
                'aircraft_id': f"{ac_type}-{str(i+1).zfill(3)}",
                'type': ac_type,
                'status': np.random.choice(['Operational', 'Maintenance', 'Check'], p=[0.85, 0.10, 0.05]),
                'base': np.random.choice(['RUH', 'JED', 'DMM']),
                'captains_required': spec['captains'],
                'cabin_required': spec['cabin']
            })
    return pd.DataFrame(fleet)

def generate_ground_staff(num_staff: int = 800) -> pd.DataFrame:
    roles = ['Ramp', 'Baggage', 'Pushback', 'Fuel', 'Load Control', 'Dispatch']
    
    data = {
        'ground_id': [f'GR{str(i).zfill(5)}' for i in range(1, num_staff + 1)],
        'role': np.random.choice(roles, num_staff),
        'base': np.random.choice(['RUH', 'JED', 'DMM', 'MED'], num_staff, p=[0.45, 0.25, 0.15, 0.15]),
        'hours_week': np.random.randint(20, 55, num_staff),
        'certified': np.random.choice([True, False], num_staff, p=[0.85, 0.15]),
        'status': np.random.choice(['Active', 'Leave'], num_staff, p=[0.92, 0.08])
    }
    
    df = pd.DataFrame(data)
    df['fatigue_risk'] = df['hours_week'] / 48
    return df

def generate_all_datasets() -> Dict[str, pd.DataFrame]:
    return {
        'flight_crew': generate_flight_deck_crew(500),
        'cabin_crew': generate_cabin_crew(1200),
        'engineering': generate_engineering_staff(300),
        'fleet': generate_fleet(),
        'ground_staff': generate_ground_staff(800)
    }
