import streamlit as st

def length_converter(value, from_unit, to_unit):
    # Conversion factors to meters
    length_units = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    # Convert to meters first, then to target unit
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    # Conversion factors to kilograms
    weight_units = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495
    }
    
    # Convert to kilograms first, then to target unit
    kilograms = value * weight_units[from_unit]
    return kilograms / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    # Handle temperature conversions separately due to different formulas
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9/5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    return value

def main():
    st.title("Unit Converter")
    
    # Create three tabs for different conversions
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"]
    )
    
    # Input value
    value = st.number_input("Enter Value", value=0.0)
    
    if conversion_type == "Length":
        units = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        if st.button("Convert"):
            try:
                result = length_converter(value, from_unit, to_unit)
                st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except:
                st.error("Conversion error occurred!")
    
    elif conversion_type == "Weight":
        units = ['kg', 'g', 'mg', 'lb', 'oz']
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        if st.button("Convert"):
            try:
                result = weight_converter(value, from_unit, to_unit)
                st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except:
                st.error("Conversion error occurred!")
    
    elif conversion_type == "Temperature":
        units = ['C', 'F', 'K']
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        if st.button("Convert"):
            try:
                result = temperature_converter(value, from_unit, to_unit)
                st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            except:
                st.error("Conversion error occurred!")

if __name__ == "__main__":
    main()
 