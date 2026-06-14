# SCG-Scale Procurement Document AI & SKU-Matching RAG Pipeline

This repository hosts a comprehensive, end-to-end solution for processing, digitizing, and matching complex procurement documents at scale, specifically optimized for SCG-scale industrial operations.

## Project Overview

The project is structured into five strategic phases, moving from synthetic data generation to a fully integrated human-in-the-loop AI system.

### Phase 1: Document Degradation Simulator (Current Implementation)

The foundational phase involves a sophisticated image processing pipeline designed to simulate realistic degradation and aging effects on digital documents. This is critical for training robust OCR models that can handle real-world, imperfect scans and photocopies.

Technical details of the simulator:
- **Noise Injection:** Adds Gaussian and Salt and Pepper noise to simulate sensor grain and dust.
- **Blurring:** Applies subtle Gaussian blur to mimic lens defocus or scanner motion.
- **Contrast and Brightness Adjustment:** Simulates the loss of dynamic range common in photocopies.
- **Rotation and Shear:** Introduces slight misalignments (deskewing) typical of manual scanning.
- **Thresholding:** Mimics the binary look of older fax or xerox machines.

### Phase 2: Intelligent Document Router

Implementation of a classification layer to identify document types (e.g., invoices, purchase orders, shipping manifests) and route them to specialized extraction sub-pipelines.

### Phase 3: Tabular OCR & Thai Language Parsing

Advanced extraction of structured data from complex tables, with specific focus on Thai language support and specialized procurement terminology.

### Phase 4: Hybrid SKU-Matching RAG Pipeline

A Retrieval-Augmented Generation (RAG) system that performs hybrid search (semantic and keyword) to accurately match extracted document line items to a master SKU database.

### Phase 5: Human-in-the-Loop (HITL) Dashboard

A validation interface for human reviewers to verify low-confidence extractions, ensuring 100% data accuracy for financial and procurement workflows.

---
*Created for Shalom (Fame)*
