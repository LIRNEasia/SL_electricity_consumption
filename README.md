# Residential Electricity Consumption: Dataset combining Multi-round Longitudinal Surveys and Energy Provider Data

## Overview

This dataset contains household electricity consumption data, and survey responses collected from households in multiple Sri Lankan cities, combining 20 months of smart-meter and non-smart-meter electricity consumption records with three rounds of longitudinal surveys conducted with 4000 households. The dataset captures household living conditions, appliance usage, and behavioral changes over time, offering an intersection of granular energy consumption and consumer-driven factors.

The dataset is divided into two main parts:

1. **Consumption Data**: Includes smart meter readings and non-smart meter (monthly) consumption data.
2. **Survey Data**: Collected over three waves (three longitudinal surveys), providing details including household demographic, appliance usage details and there changes over time.

Each section includes a **data dictionary** that describes variable names and meanings. Additionally Survey Data includes **data profilers** for each individual data file.

---

## 1. Consumption Data
### 1.1 Non-Smart Meter Data
- **Description**: Monthly electricity consumption readings for 4,063 households over 20 months.
- **File Path**: `consumption_data/non_smart_meter/`
- **File Name**: `monthly_consumption.csv`
- **Columns**:
  - `household_Id`: Unique household identifier
  - `month`: Year-Month format (YYYY-MM)
  - `consumption`: Total consumed units in kilowatts (KW)
  
### 1.2 Smart Meter Data
#### 1.2.1 15-Minute Interval Data
- **Description**: Smart meter readings collected every 15 minutes.
- **File Path**: `consumption_data/smart_meter/15min_interval/`
- **Files and Data Points**:
  - `smart_15min_1.csv`: 9,435,755 datapoints, collected during 2023-10-01 to 2024-03-01.
  - `smart_15min_2.csv`: 16,425,676 datapoints, collected during 2024-03-02 to 2024-08-01 
  - `smart_15min_3.csv`: 19,751,849 datapoints, collected during 2024-08-02 to 2024-12-23

- **Sample Columns**:
  - `household_Id`: Unique household identifier
  - `date`: Date of the reading
  - `time`: Time of the reading
  - `importkwh(kwh)`: : Total Cumulative consumed energy units in kilowatts (kW)
  - `exportkwh(kwh)`: : Total Cumulative generated energy units in kilowatts (kW)

#### 1.2.2 6-Hour Interval Data
- **Description**: Smart meter readings collected every 6 hours.
- **File Path**: `consumption_data/smart_meter/6hour_interval/`
- **Files and Data Points**:
  - `smart_6hour_1.csv`: 1,115,230 datapoints, collected during 2023-01-01 to 2023-06-01
  - `smart_6hour_2.csv`: 1,319,347 datapoints, collected during 2023-06-02 to 2023-11-01
  - `smart_6hour_3.csv`: 1,047,075 datapoints, collected during 2023-11-02 to 2024-04-01
  - `smart_6hour_4.csv`: 680,674 datapoints, collected during 2024-04-02 to 2024-09-01
  - `smart_6hour_5.csv`: 279,467 datapoints, collected during 2024-09-02 to 2024-12-31
- **Sample Columns**:
  - `household_Id`: Unique household identifier
  - `date`: Date of the reading
  - `time`: Time of the reading
  - `TOTAL_IMPORT (kWh)`: : Total Cumulative consumed energy units in kilowatts (kW)
  - `TOTAL_EXPORT (kWh)`: : Total Cumulative generated energy units in kilowatts (kW)

*(See `consumption_data/documentation/data_dictionary.csv` for full details.)*

---

## 2. Survey Data

### 2.1 Wave 1
- **File Path**: `survey_data/wave_1/`
- **Tables**:
  - `w1_ac_roster.csv`
  - `w1_appliances.csv`
  - `w1_demographics.csv`
  - `w1_electricity_generation_water_heating_cooking.csv`
  - `w1_fan_roster.csv`
  - `w1_household_information_and_history.csv`
  - `w1_light_roster.csv`
  - `w1_room_roster.csv`

### 2.2 Wave 2
- **File Path**: `survey_data/wave_2/`
- **Tables**:
  - `w2_ac_roster.csv`
  - `w2_new_household_members.csv`
  - `w2_changed_appliances.csv`
  - `w2_members_who_were_in_w1.csv`
  - `w2_electricity_generation.csv`
  - `w2_room_roster.csv`
  - `w2_changed_rooms.csv`
  - `w2_appliance_usage.csv`
  - `w2_household_information.csv`
  - `w2_light_roster.csv`
  - `w2_fan_roster.csv`
  - `w2_behaviour.csv`

### 2.3 Wave 3
- **File Path**: `survey_data/wave_3/`
- **Tables**:
  - `w3_appliance_usage.csv`
  - `w3_behaviour_data.csv`
  - `w3_fan_roster.csv`
  - `w3_electricity_billing_info.csv`
  - `w3_light_roster.csv`
  - `w3_ac_roster.csv`
  - `w3_members_who_were_in_w2.csv`
  - `w3_new_household_members.csv`
  - `w3_changed_rooms.csv`
  - `w3_demolished_rooms.csv`
  - `w3_room_roster.csv`
  - `w3_awareness_of_time_of_use.csv`
  - `w3_household_information.csv`
  - `w3_electricity_generation.csv`
  - `w3_changed_appliances.csv`

### 2.4 Survey Dates
- **File Path**: `survey_data/`
- **File Name**: `surveyed_dates.csv`
- **Description**: Contains timestamps of when surveys were conducted for each household.

*(See `survey_data/documentation/data_dictionaries` and `survey_data/documentation/table_structures` for details.)*

---

## Documentation
Each dataset component has an accompanying data dictionary and table structure file stored in the `documentation/` folder:
- `data_dictionary.csv`: Definitions of column names and data types.
- `table_structure.csv`: Relationships between tables and descriptions.
