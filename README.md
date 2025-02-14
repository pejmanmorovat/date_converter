# Date Converter Program

A Python-based date converter program that allows users to convert between the **Gregorian**, **Persian (Solar Hijri)**, and **Islamic** calendars. The program provides an interactive console interface with color-coded outputs to enhance user experience.

### Author:
Pejman Morovat

---

## Features:

- **Current Calendar Display**: Shows the current date in Gregorian, Persian (Solar Hijri), and Islamic formats.
- **Conversion Functions**:
  - Convert **Solar Hijri** to **Gregorian** date.
  - Convert **Gregorian** to **Solar Hijri** date.
  - Convert **Gregorian** to **Islamic** date.

---

## Requirements:

Before running the program, you’ll need to install the following Python libraries:

- **jdatetime**: For converting between Gregorian and Persian dates.
- **convertdate**: For converting between Gregorian and Islamic dates.
- **colorama**: For colored terminal output.

You can install these libraries using `pip`:

```bash
pip install jdatetime convertdate colorama
```
## Usage:

Clone the repository:
```bash
git clone https://github.com/pejmanmorovat/date_converter.git
cd date_converter
```
Run the script:
```bash
python date_converter.py
```
---

## How to Use:

1. **Run the Program**: Execute the Python script in your terminal.
   
2. **Choose an Option**: 
    - Option 1: Display current dates in Gregorian, Persian, and Islamic calendars.
    - Option 2: Convert a **Solar Hijri** date to **Gregorian**.
    - Option 3: Convert a **Gregorian** date to **Solar Hijri**.
    - Option 4: Convert a **Gregorian** date to **Islamic**.
    - Option 5: Exit the program.

3. **Input Dates**: Depending on your choice, input the relevant date details for conversion.

---

## Example Run:

```bash
╔════════════════════════════╗
║    Date Converter Program  ║
║    Author: Pejman Morovat  ║
╚════════════════════════════╝

╔════════════════════════════╗
║      DATE CONVERTER        ║
╚════════════════════════════╝

1. Show Current Calendars
2. Convert Solar Hijri to Gregorian
3. Convert Gregorian to Solar Hijri
4. Convert Gregorian to Islamic
5. Exit

Enter your choice (1-5): 1

╔════════════════════════════╗
║      CURRENT CALENDARS     ║
╚════════════════════════════╝

Today: Wednesday
Persian Date: 1403/11/19
Month: Bahman

Gregorian Date: 2025/02/07
Month: February

Islamic Date: 1446/07/27

Time: 13:15:32
```

---

## License:

This project is open-source and licensed under the MIT License.

## Date Converter

A Python-based date converter supporting Gregorian, Solar Hijri (Persian), and Islamic dates.

### Features
- CLI Version: `date_converter_cli.py`
- GUI Version: `date_converter_gui.py`

### Requirements
```bash
pip install -r requirements.txt
```
