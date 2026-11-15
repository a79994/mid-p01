#!/usr/bin/env bash
# ==============================================================================
# UNIVERSIDADE DO ALGARVE - MSc in Informatics Engineering (2026/2027)
# Course: Data Modelling and Integration (DMI) - Project P1
# Student: David Rodrigues (Subtopic: China — 58 Entities)
# Script: setup_and_reset.sh
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=================================================================="
echo " [DAVID RODRIGUES - CHINA] Resetting & Building All 58 Entities"
echo "=================================================================="

python3 "$PROJECT_DIR/src/build_david_china_db.py"
python3 "$PROJECT_DIR/queries/run_david_queries.py"

echo "=================================================================="
echo " [SUCCESS] All 38 Relational 3NF SQL Tables + 20 XSD-Validated"
echo " XML Containers + Queries Ready!"
echo "=================================================================="
