Here's a complete and well-structured `README.md` file for your GitHub repository:  

---

# **Date Converter Program**  

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
A Python-based **Date Converter Program** that converts between **Gregorian, Solar Hijri (Persian), and Islamic** calendars. It also displays the current date and time in all three calendar systems.  

## **Features**  
✅ Display the current date in **Gregorian, Solar Hijri (Persian), and Islamic** calendars.  
✅ Convert **Solar Hijri (Persian) to Gregorian**.  
✅ Convert **Gregorian to Solar Hijri (Persian)**.  
✅ Displays **weekday names and month names** for better readability.  
✅ Uses **Colorama** for a colorful and user-friendly interface.  

## **Technologies Used**  
- **Python** (Core Language)  
- **Jalali Date (`jdatetime`)** – To handle Persian (Solar Hijri) dates.  
- **Convertdate (`convertdate`)** – To convert between different calendar systems.  
- **Colorama** – For colored terminal output.  
## **Requirement 
```bash
pkg install openssl
```
## **Installation**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/pejmanmorovat/date_converter.git
   cd date_converter
   ```

2. **Install required dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, install packages manually:  
   ```bash
   pip install jdatetime convertdate colorama
   ```

3. **Run the program**  
   ```bash
   python condate.py
   ```

## **Usage**  
After running the script, you will see a menu with four options:  

1️⃣ **Show Current Calendars** – Displays today's date in **Gregorian, Solar Hijri, and Islamic** formats.  
2️⃣ **Convert Solar Hijri to Gregorian** – Convert a Persian (Solar Hijri) date to **Gregorian**.  
3️⃣ **Convert Gregorian to Solar Hijri** – Convert a Gregorian date to **Persian (Solar Hijri)**.  
4️⃣ **Exit** – Close the program.  

### **Example Usage**  
#### **Convert Solar Hijri to Gregorian**  
```
Enter Solar Hijri year: 1403
Enter Solar Hijri month: 11
Enter Solar Hijri day: 18
Gregorian Date: 2025-02-07
```

#### **Convert Gregorian to Solar Hijri**  
```
Enter Gregorian year: 2025
Enter Gregorian month: 2
Enter Gregorian day: 7
Solar Hijri Date: 1403-11-18
```

## **Code Structure**  
- **`date_converter.py`** – Main script handling date conversions and user interaction.  
- **`requirements.txt`** – Dependencies required to run the program.  
- **`README.md`** – Documentation for the project.  

## **Contribution**  
Contributions are welcome! Feel free to **fork** the repository and submit a **pull request** with improvements.  

## **License**  
This project is **open-source** and available under the **MIT License**.  

## **Author**  
👤 **Pejman Morovat**  
📧 pejmanmorovat@yahoo.com
