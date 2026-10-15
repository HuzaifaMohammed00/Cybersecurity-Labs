# 🕵️‍♂️ SQL Murder Mystery - Forensic Investigation Write-up

> **Author:** Huzaifa Mohammed  
> **Platform:** [Knight Lab SQL Murder Mystery](https://mystery.knightlab.com/)  
> **Status:** Completed & Verified  
> **Category:** Database Forensics / SQL Querying / Incident Investigation  

---

## 📌 Overview
This repository contains my forensic investigation report and step-by-step SQL queries used to solve the **SQL Murder Mystery** challenge. Instead of relying on passive reading, this hands-on lab required navigating relational database schemas, tracing foreign keys, utilizing wildcards, and filtering multi-variable evidence to catch both the hired hitman and the ultimate mastermind.

---

## 🧠 Key Skills & Concepts Practiced
* **Relational Schema Analysis:** Mapping relationships across 7 interconnected tables (`person`, `interview`, `drivers_license`, `get_fit_now_member`, `get_fit_now_check_in`, `facebook_event_checkin`, `crime_scene_report`).
* **Pattern Matching:** Leveraging `LIKE` and `%` wildcards for partial string matching.
* **Advanced Filtering:** Using `IN (...)`, `BETWEEN ... AND ...`, and sorting with `ORDER BY ... DESC LIMIT 1`.
* **Investigative Mindset:** Avoiding false positives by expanding search scopes rather than anchoring to the first matching record.

---

## 🔍 Investigation Workflow & Queries

### 1. Crime Scene Analysis
```sql
-- Extracting the initial crime scene report
SELECT * 
FROM crime_scene_report 
WHERE city = 'SQL City' 
  AND type = 'murder' 
  AND date = 20180115;
```
* **Findings:** Two witnesses identified (one on Northwestern Dr, one named Annabel on Franklin Ave).

### 2. Witness Testimony Retrieval
```sql
-- Finding Witness 1 (Last house on Northwestern Dr)
SELECT * 
FROM person 
WHERE address_street_name = 'Northwestern Dr' 
ORDER BY address_number DESC 
LIMIT 1;

-- Finding Witness 2 (Annabel on Franklin Ave)
SELECT * 
FROM person 
WHERE address_street_name = 'Franklin Ave' 
  AND name LIKE '%Annabel%';

-- Extracting interview transcripts
SELECT * 
FROM interview 
WHERE person_id IN (14887, 16371);
```

### 3. Catching the Hitman (Jeremy Bowers)
```sql
-- Filtering gym gold members starting with 48Z
SELECT * 
FROM get_fit_now_member 
WHERE membership_status = 'gold' 
  AND id LIKE '48Z%';

-- Linking suspects and verifying license plate fragment H42W
SELECT * 
FROM person 
WHERE id IN (28819, 67318);

SELECT * 
FROM drivers_license 
WHERE plate_number LIKE '%H42W%';
```

### 4. Uncovering the Mastermind (Miranda Priestly)
```sql
-- Reviewing hitman's confession
SELECT * 
FROM interview 
WHERE person_id = 67318;

-- Searching for physical description & vehicle criteria (using BETWEEN to avoid false narrowing)
SELECT * 
FROM drivers_license 
WHERE gender = 'female' 
  AND hair_color = 'red' 
  AND height BETWEEN 65 AND 67 
  AND car_make = 'Tesla' 
  AND car_model = 'Model S';

-- Mapping license IDs to individuals
SELECT * 
FROM person 
WHERE license_id IN (918773, 202298, 291182);

-- Checking event check-ins for 3 appearances in Dec 2017
SELECT * 
FROM facebook_event_checkin 
WHERE person_id IN (99716, 78881, 90700) 
  AND event_name = 'SQL Symphony Concert' 
  AND date LIKE '201712%';
```

---

## 💡 Key Forensic Takeaway
> *“Never fall in love with your first suspect.”* 
> Initially restricting a search parameter (`height = 65`) pointed to a single individual (`Red Korb`). Expanding the scope properly (`BETWEEN 65 AND 67`) revealed the true pool of suspects, proving that correlational event logs (`facebook_event_checkin`) are vital to eliminating false positives in digital investigations.