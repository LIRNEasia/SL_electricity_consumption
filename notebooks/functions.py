import pandas as pd

def calculate_price(avg):

    for idx, row in avg.iterrows():

        if row['consumption'] <= 30:
            price = row['consumption'] * 4
        elif row['consumption'] <= 60:
            extra = row['consumption'] - 30
            price = (30 * 4) + (extra * 6)
        elif row['consumption'] <= 90:
            extra = row['consumption'] - 60
            price = (60 * 11) + (extra * 14)
        elif row['consumption'] <= 120:
            extra = row['consumption'] - 90
            price = (60 * 11) + (30 * 14) + (extra * 20)
        elif row['consumption'] <= 180:
            extra = row['consumption'] - 120
            price = (60 * 11) + (30 * 14) + (60 * 20) + (extra * 33)
        else:
            extra = row['consumption'] - 180
            price = (60 * 11) + (30 * 14) + (60 * 20) + (60 * 33) + (extra * 52)


        avg.loc[idx, 'price'] = price + 1200
    
    return avg



def calculate_appliance_score(app):
    """
    Calculate the appliance score based on the appliance weights.
    The weights are defined in the appliance_weights dictionary.
    """
    # Load the appliance data

    appliance_weights = {
        # Essential Appliances (Weight = 1)
        "Refrigerator": 1,
        "Microwave": 1,
        "Rice cooker": 1,
        "Electric Iron including electric steam iron": 1,
        "Mobile phone - Basic phones": 1,
        "Mobile phone - Smart phones": 1,
        "Mobile phone - Feature phones": 1,
        "Fixed phones": 1,
        "Emergency Light / re-chargeable torches": 1,

        # Convenience Appliances (Weight = 2)
        "Electric pressure cooker": 2, 
        "Electric Bell" : 2,
        "Separate Freezer": 2,
        "Mini Bar": 2,
        "Electric cook tops (induction cookers, Infra-red cookers, hot plates)": 2,
        "Electric Blender": 2,
        "Electric grinder": 2,
        "Electric mixer / beater": 2,
        "Electric food processor": 2,
        "Electric Kettle": 2,
        "Toaster / Sandwich toaster": 2,
        "Electric coconut scraper": 2,
        "Washing Machine": 2,
        "Electric Vacuum Cleaner": 2,
        "TV": 2,
        "TV antenna": 2,
        "Fax machines": 2,
        "Radio": 2,
        "Computers": 2,
        "Laptops": 2,
        "Routers": 2,
        "Printer": 2,
        "Hair dryer": 2,
        "Hair iron / hair curlers": 2,
        "Electric shavers": 2,
        "Electric Sewing machine": 2,

        # Entertainment/Leisure Appliances (Weight = 3)
        "Air fryer": 3,
        "Coffee maker": 3,
        "Bluetooth Speakers": 3,
        "DVD / VCD": 3,
        "Gaming console/PlayStation": 3,
        "Sound systems (Subwoofer)/Stereo": 3,
        "Camera (that needs to be charged using electricity)": 3,
        "Home theater system": 3,
        "Electric musical Instruments (ex.: electric organ, electric guitar etc.)": 3,
        "Mobile phone – Smart phones": 3,
        "Mobile phone – Feature phones": 3,
        "Power banks": 3,
        "Oxygen filter for fish tank": 3,
        "Toys with re-chargeable batteries": 3,

        # High-Tech/Luxury Appliances (Weight = 4)
        "Dialog TV / Peo TV / Satellite TV box": 4,
        "Electric Oven": 4,
        "Electrical exhaust fan fitted above the oven or the hot plate": 4,
        "Electric water heater to heat water for drinking purposes": 4,
        "Electric grill": 4,
        "Electric water gun (used to wash cars etc.)": 4,
        "Electric Water filter / water dispenser": 4,
        "Dish washer": 4,
        "Clothes dryer": 4,
        "Electric floor polisher": 4,
        "Electric Lawn mower": 4,
        "Photo Copiers": 4,
        "Electric Exercise Machines": 4,
        "Roller door": 4,
        "CCTV camera systems": 4,
        "Electric Alarm System": 4,
        "Other Electric Security Systems": 4,
        "Electric vehicles (four wheelers) - cars,  vans, SUVs)": 4,
        "Electric vehicles (two wheelers) - Electric bicycles, scooters": 4,
        "Electric vehicles (three wheelers)": 4,
        "Electric Water pump": 4,
        "Geyser / Hot water systems for bathrooms which operate from electricity": 4,
        "Hot tub": 4,
        "Electric Fountain / decorative waterfall": 4,
        "Electric heater (to control room temperature)": 4,
        "Scanner": 4,
        "Waffle maker": 4,
        "Humidifier": 4,
        "Other1": 4,
        "Other 2": 4,
        "Other 3": 4,
        "Tab": 4
    }

    app['Appliance_Weight'] = app['appliance_type'].map(appliance_weights)
    customer_scores = app.groupby('household_ID')['Appliance_Weight'].sum().reset_index()
    return customer_scores