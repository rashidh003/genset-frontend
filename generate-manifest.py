#!/usr/bin/env python3
"""
Run this script whenever you add or remove images from public/images/<folder>:
  python3 generate-manifest.py
It regenerates public/images/manifest.json which the products page reads automatically.
"""
import os, json

BASE = os.path.join(os.path.dirname(__file__), 'public', 'images')

CATEGORIES = [
    {"label": "Controllers",  "folder": "cotroller",    "filter": "controllers"},
    {"label": "AVR",          "folder": "avr",          "filter": "avr"},
    {"label": "Filters",      "folder": "FILTERS",      "filter": "filters"},
    {"label": "Battery",      "folder": "battery",      "filter": "battery"},
    {"label": "Coolant",      "folder": "coolant",      "filter": "coolant"},
    {"label": "Engine Spares","folder": "engine spares","filter": "engine-spares"},
    {"label": "Fleetguard",   "folder": "fleetguart",   "filter": "fleetguard"},
    {"label": "Fuel Gauge",   "folder": "fuel guage",   "filter": "fuel-gauge"},
    {"label": "Oil",          "folder": "oil",          "filter": "oil"},
    {"label": "Pistons",      "folder": "pistons",      "filter": "pistons"},
    {"label": "Solenoid",     "folder": "solenoid",     "filter": "solenoid"},
    {"label": "Valves",       "folder": "valves",       "filter": "valves"},
]

manifest = {"categories": []}
total = 0
for cat in CATEGORIES:
    folder_path = os.path.join(BASE, cat["folder"])
    if not os.path.isdir(folder_path):
        print(f"  SKIP (folder missing): {cat['folder']}")
        continue
    images = sorted([
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')
    ])
    manifest["categories"].append({
        "label":  cat["label"],
        "folder": cat["folder"],
        "filter": cat["filter"],
        "images": images,
    })
    total += len(images)
    print(f"  {cat['label']:15s}: {len(images)} images")

out = os.path.join(BASE, 'manifest.json')
with open(out, 'w') as f:
    json.dump(manifest, f, indent=2)
print(f"\nDone — {total} total images → {out}")
