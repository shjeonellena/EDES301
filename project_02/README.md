# Etch-A-Sketch PCB Design

This directory contains all design and manufacturing files for **Project 02**, which focuses on creating a custom printed circuit board (PCB) for the Etch-A-Sketch project. The board was designed to interface with a **PocketBeagle** and supports the electronics required for the implemented system.

All files necessary for **PCB fabrication, assembly, and documentation** are included in this repository.

---

## Repository Structure

### `/docs`
This folder contains supporting documentation for Project 02, including:
- The **Project 02 proposal**, outlining the design concept and system goals
- A **mechanical block diagram** describing the overall system architecture
- A **PDF of the finalized schematics**
- Images of the **layers** of the PCB layout for reference and review

---

### `/EAGLE`
This folder contains the full EAGLE design files used to create the PCB:
- **`.lbr`** – Custom and modified component libraries
- **`.sch`** – Schematic files defining the electrical design
- **`.brd`** – Board layout files defining component placement and routing

#### `/EAGLE/CAM Output`
The subfolder contains manufacturing outputs generated using **EAGLE’s default CAM settings**, including:
- **Gerber files** for PCB fabrication
- **Drill files** for vias and through-holes
- **Assembly files** for component placement and reference

These files can be directly submitted to a PCB manufacturer for production.

---

## Notes
- The PCB was designed with standard fabrication constraints in mind
- All silkscreen, copper, and drill layers have been verified prior to Gerber generation
- No additional processing is required before manufacturing

---

## Author
Ellena Jeon
Etch-A-Sketch Project – Project 02
