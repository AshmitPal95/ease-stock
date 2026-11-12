# ease-stock
> A lightweight, easy to use, desktop-based Inventory Management System (IMS) designed for speed, simplicity and operational efficiency 

## Overview:
ease-stock was initially developed as a school project but quickly scaled into a real-world solution to handle stock tracking for my family business. It has a minimalist design  with a  fast, simple and clean Tkinter-based Graphical User Interface(GUI) interface that solves genuine business bottlenecks which prioritizes quick data entry and access as well as smooth and reliable operation.

##  Specifications:
*   **Language:** Python 3.13
*   **Database:** MySQL
*   
## Technologies used:**
* **MySQL**
* **Database Abstraction Layer(DAL)**
* **Tkinter**
* **Modal Windows**
* **Automatic Logging**
* **bcrypt Hashing**
* **Regular Expression (Regex)**
 
## Key Features:
*   **Streamlined UI:** A clean, easy-to-use menu system  built with Tkinter for rapid and easy operations with a minimal learning curve.
*   **Core Stock Management:** Fast, efficient and reliable CRUD operations (Create, Read, Update, Delete) for  addition, modification, and withdrawal of inventory items.
*   **Automatic Logging:** History of all the actions performed every 14 days are stored in .csv file which can be opened with Excel
*   **Double-layer Authentication:** Users have to enter the user password as well as the database password in order to access the system.
*   **Secure Password Storage:** User Passwords are securely stored with the help of bcrypt hashing.
*   **Stock Valuation:** Automatically calculates the total worth of each category, vendor and godown based on rate, unit weight and number of units
## Before you setup:
* **Please ensure that MySQL has been installed on the system on which ease-stock will be used**
* **Default Password:** easestock@1234
  
## Roadmap:
*  Development of this software is actively ongoing. In order to optimize performance and improve the quality of the code:
*  **1)** Add keyboard shortcuts for greater ease of operation and faster navigation
*  **2)** Remove unused imports from all modules to maintain clean and efficient code.

## Acknowledgments
*   **Mentorship & QA:** Special thanks to my father for introducing me to industry-standard practices, providing meticulous architectural supervision, and conducting rigorous Quality Assurance (QA) testing on the software.
*   **Development Tools:** Microsoft Copilot and Google Gemini were utilized as productivity tools for syntax debugging and localized code optimization.
