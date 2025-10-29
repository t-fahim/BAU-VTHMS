# 🏥 BAU Veterinary Teaching Hospital Management System (BAU-VTHMS)  
**Final Software Engineering Report**

---

## 1. Abstract

The BAU-VTHMS project was developed to solve operational and academic challenges at the Bangladesh Agricultural University Veterinary Teaching Hospital. The existing paper-based system created inefficiencies, errors, and limited access to valuable patient data. This project successfully delivered a digital solution focused on patient registration, medical recordkeeping, and basic inventory management using Python, Tkinter, and PostgreSQL under the MVC architecture. The MVP is functional and lays a solid foundation for future expansion.

---

## 2. Introduction

Veterinary hospitals, particularly in teaching institutions like BAU, require efficient systems to manage both clinical operations and educational functions. However, manual systems often cause bottlenecks in patient registration, record retrieval, and data analysis. The BAU-VTHMS was designed to address these issues by providing a centralized digital platform that supports veterinarians, students, and administrative staff.

The system ensures:
- Structured data collection
- Reliable patient histories
- Faster patient processing
- Improved academic and research capabilities

---

## 3. Activity Diagram

The following activity diagram illustrates the patient case management workflow:

![Activity Diagram](https://github.com/tamimcodes/BAU-VTHMS/blob/main/Documentation/2209024_activity_diagram.png)

---

## 4. Model-View-Controller (MVC) Architecture

The system is structured using the **MVC design pattern** to ensure maintainability and separation of concerns:

### ✅ Architecture Roles:
- **Model:** Handles data logic and PostgreSQL database operations  
- **View:** User interface built using Python's Tkinter library  
- **Controller:** Connects user inputs to appropriate backend logic and updates the interface

![MVC Architecture](https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg)

---

## 5. Results & Testing

### ✅ Features Implemented:
- Owner & Patient Registration
- EMR (Electronic Medical Record) form for veterinarians
- Case Record Printing and Reporting
- Inventory entry and tracking
- Basic statistical reports

### ✅ Testing Outcomes:
| Metric                 | Goal                         | Achieved Status              |
|------------------------|------------------------------|------------------------------|
| Prescription Usage     | ≥ 95%                        | Not fully measured (UAT positive) |
| Check-in Efficiency    | 20% reduction                | Estimated >20% reduction     |
| Data Accuracy          | 95% inventory accuracy       | To be fully evaluated post-deployment |
| User Satisfaction      | ≥ 4.0 / 5                    | 4.2 / 5 (UAT average score)  |
| Critical Bugs          | < 5/month                    | 0 reported during UAT        |

---

## 6. Screenshots

- **Dashboard View**
  ![Dashboard View](https://github.com/t-fahim/BAU-VTHMS/blob/main/Documentation/dashbord.png)


---

## 7. New Contributions

### ✅ Innovations Introduced:
- **Workflow Digitization:** A previously fully manual case-handling process has been converted into a semi-automated workflow.
- **Case Record Integration:** All stages from registration to diagnosis and treatment are captured and linked via a unified case number.
- **Reporting Capability:** Initial reports now offer visibility into daily activity and stock levels.
- **UAT Feedback Loop:** Collected and integrated user feedback during MVP development.

---

## 8. Conclusion & Future Work

The BAU-VTHMS has demonstrated that transitioning to a digital veterinary hospital management system is feasible and beneficial. It not only increases operational efficiency but also enhances the academic value of the hospital by organizing clinical records for study and research.

### 🔮 Future Recommendations:
- Add appointment and billing modules
- Implement a mobile version for on-the-go record access
- Introduce real-time data analytics
- Integrate with external lab tools for automation
- Conduct full staff training for deployment at scale

---

**Submitted by:**  
Md.Tamim Ahmed Fahim
B.Sc. in Bioinformatics & Software Engineering 
Bangladesh Agricultural University  
Date: August 6, 2025
