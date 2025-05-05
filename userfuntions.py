import re
import pandas as pd
import numpy as np


def extract_keywords_job (title):
    
    job_keywords = [
        ["Data", "scientist"],
        ["Data", "analyst"],  
        ["Data", "engineer"],
        ["Machine", "learning"], 
        ["Business", "intelligence"],
        ["Daten", "bank"],
        ["Business", "analyst"],
        ["Daten", "analys"]
        ]
    
    res = None
    for words in job_keywords:
        if words[0].lower() in title.lower() and words[1].lower() in title.lower():
            res = " ".join(words)     

    if res == "Daten analys":
        res = "Data analyst" 

    if res == "Daten bank":
        res = "Data engineer"

    if res == "Machine learning":
        res = "Machine learning engineer"

    return res
    



def extract_seniority (title):

    title_lower = title.lower()
    if any(keyword in title_lower for keyword in ["junior"]):
        return "Junior"
    
    elif any(keyword in title_lower for keyword in ["senior", "experienced", "expert", "professional", "sr.", "referent"]):
        return "Senior"
    
    elif any(keyword in title_lower for keyword in ["lead", "chief", "head", "principal", "gruppenkoordinator", "team lead", "teamleit"]):
        return "Lead"
    
    elif any(keyword in title_lower for keyword in ["intern", "trainee", "practic", "student", "praktik", "student", "ausbildung", "abschlussarbeit"]):
        return "Intern"
    
    else :
        return "None(Mid)"
    



def count_locations(locations):
    location_dict = {}
    for location in locations:
        if pd.isna(location):  # Пропускаем NaN значения
            continue
        list_location = [loc.strip().lower() for loc in location.split(",")]
        for loc in list_location:
            if loc in location_dict:
                location_dict[loc] += 1
            else:
                location_dict[loc] = 1
    return dict(sorted(location_dict.items(), key=lambda x: x[1], reverse=True))




def extract_location_remote (location):
    location = location.lower()
    if "remote" in location or "home" in location:
        return 1
    else:
        return 0