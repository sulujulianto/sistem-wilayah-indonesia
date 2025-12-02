# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

## [0.1.0-api] - 2025-12-01

### Added
- 🚀 FastAPI service with `/health`, `/v1/stats`, `/v1/provinces`, and `/v1/search` endpoints plus unified error responses
- 🗂️ JSON data file (`app/data/wilayah.json`) with loader fallback in `sistem_wilayah_indonesia.py`
- 🧪 Service layer, Pydantic schemas, and pytest suite (FastAPI TestClient)
- 🛠️ CI workflow (ruff, mypy, pytest), Dockerfile, and backend project scaffolding

### Changed
- 📄 README diperbarui untuk quickstart API, Docker, dan catatan versi (tag CLI `v1.0.0-cli`)
- 📦 Dependencies disederhanakan: runtime FastAPI + dev tools (ruff, mypy, pytest)

---

## [2.0.0-cli] - 2025-08-19

### Added
- 🎉 Complete rewrite with comprehensive kabupaten/kota data
- 📊 Complete data for all 38 provinces in Indonesia
- 🗂️ 416 kabupaten and 98 kota data
- 🔍 Advanced search functionality for provinces, kabupaten, and kota
- 📈 Statistics feature showing complete administrative data
- 💾 Export functionality to JSON and TXT formats
- 🎨 Enhanced CLI interface with emoji and better formatting
- 📚 Comprehensive documentation and README
- 🔧 Professional project structure with all supporting files

### Changed
- ✨ Fuzzy search capability for flexible input
- 🔄 Object-oriented programming approach
- 📝 Type hints for better code maintainability
- ⚡ Improved error handling and user feedback
- 🎯 Better user experience with intuitive commands

### Technical Improvements
- 🏗️ Class-based architecture with `SistemWilayahIndonesia`
- 🔍 Separate methods for different search types
- 📁 Proper file organization and project structure
- 🧪 Better code documentation and comments

---

## [1.0.0-cli] - 2024-01-16

### Added
- 🏛️ Basic province and capital city lookup
- 🎲 Random province information feature
- 💻 Simple command-line interface
- 📋 Basic province listing functionality

### Features
- 🔍 Province search by name
- 🎯 Capital city information
- 📜 List all provinces
- 🎪 Random province trivia

### Data Coverage
- 🗺️ 38 provinces with capital cities
- 🏢 Basic administrative information

---

## Data Update History

### August 2025
- ✅ Updated all provincial data to 2024 standards
- ✅ Added new provinces: Papua Tengah, Papua Pegunungan, Papua Selatan, Papua Barat Daya
- ✅ Verified kabupaten/kota data with latest government regulations
- ✅ Cross-referenced with BPS and Wikipedia sources

### Data Accuracy Notes
- 📊 Total Provinces: 38 (including newest Papua provinces)
- 🏛️ Total Kabupaten: 416
- 🏙️ Total Kota: 98
- 📍 Total Administrative Level 2: 514

---

## Acknowledgments

### Data Sources
- 🏛️ Kementerian Dalam Negeri Republik Indonesia
- 📊 Badan Pusat Statistik Indonesia
- 🌐 Wikipedia Contributors

### Technology Stack
- 🐍 Python 3.7+
- 📝 Built-in libraries: `json`, `random`, `typing`, `datetime`
- 🎨 CLI with emoji support

### Special Thanks
- 🙏 Indonesian Government for providing open administrative data
- 👥 Open source community for tools and inspiration
- 📖 Wikipedia editors for maintaining accurate regional data
- 🇮🇩 Indonesia for being an amazing archipelago to document
