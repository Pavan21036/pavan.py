import streamlit as st

# Function to calculate efficiency and CU_L
def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    # Calculate Ish
    Ish = V / Rsh
    
    # Calculate Ia
    Ia = K * IL - Ish
    
    # Calculate CU_L (Core and Losses)
    CU_L = (Ish**2) * Rsh + (Ia**2) * Ra  # Corrected the formula (squared Ish and Ia)
    
    # Calculate Efficiency (Eff)
    Eff = (K * V * IL - CL - CU_L) / (K * V * IL) * 100
    
    return Eff, CU_L


def main():
    st.title("Generator Efficiency Calculator")
    
    # Inputs from the user
    V = st.number_input("Enter the Voltage (V)", min_value=0.0, step=0.1)
    CL = st.number_input("Enter the Core Losses (CL) in Watts", min_value=0.0, step=0.1)
    IL = st.number_input("Enter the Full Load Current (IL) in Amps", min_value=0.0, step=0.1)
    K = st.number_input("Enter the Loading on Generator (K)", min_value=0.0, step=0.1)
    Rsh = st.number_input("Enter the Shunt Field Resistance (Rsh) in Ohms", min_value=0.0, step=0.1)
    Ra = st.number_input("Enter the Armature Resistance (Ra) in Ohms", min_value=0.0, step=0.1)
    
    # Calculate Efficiency and CU_L
    if st.button("Calculate Efficiency"):
        if V > 0 and CL >= 0 and IL >= 0 and K >= 0 and Rsh > 0 and Ra >= 0:
            Eff, CU_L = Gen_Eff(V, CL, IL, K, Rsh, Ra)
            st.write(f"Efficiency: {Eff:.2f}%")
            st.write(f"Core and Losses (CU_L): {CU_L:.2f} Watts")
        else:
            st.error("Please provide valid inputs.")
    
if __name__ == "__main__":  # Corrected the typo here
    main()
