import pandas as pd

# Data for the Quality Education Budget
quality_education_data = {
    "Description": [
        "Teacher Salaries (3 teachers @ ₹25,000 each)",
        "Learning Materials (₹2,000 for 50 students)",
        "Classroom Setup (Rent for community hall)",
        "Miscellaneous Expenses (Electricity, maintenance)"
    ],
    "Cost": [
        "₹25,000/teacher",
        "₹1,00,000",
        "₹10,000",
        "₹5,000"
    ],
    "Frequency": [
        "Monthly",
        "Annual",
        "Monthly",
        "Monthly"
    ],
    "Total Cost": [
        "₹9,00,000",
        "₹1,00,000",
        "₹1,20,000",
        "₹60,000"
    ]
}

# Data for the Community Kitchens Budget
community_kitchens_data = {
    "Description": [
        "Meal Cost (₹20 per meal for 100 meals)"
    ],
    "Cost": [
        "₹20"
    ],
    "Frequency": [
        "Daily"
    ],
    "Total Cost": [
        "₹60,000"
    ]
}

# Data for the Community-Led WASH Program Budget
wash_program_data = {
    "Description": [
        "Water Tank Cleaning (₹5,000 per tank)",
        "Water Purification Systems (Small-scale units)",
        "Household Water Filters",
        "Awareness Campaign (Printed materials & workshops)"
    ],
    "Cost": [
        "₹5,000",
        "₹30,000–₹50,000",
        "₹1,000",
        "₹10,000"
    ],
    "Frequency": [
        "Quarterly",
        "One-time",
        "One-time",
        "Annual"
    ],
    "Total Cost": [
        "₹20,000",
        "Varies by community size",
        "Varies by household",
        "₹15,000"
    ]
}

# Create DataFrames
df_quality_education = pd.DataFrame(quality_education_data)
df_community_kitchens = pd.DataFrame(community_kitchens_data)
df_wash_program = pd.DataFrame(wash_program_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = r'C:\Users\singh\Downloads\community_initiatives_budget.xlsx'  # Use raw string
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_quality_education.to_excel(writer, sheet_name='Quality Education Budget', index=False)
    df_community_kitchens.to_excel(writer, sheet_name='Community Kitchens Budget', index=False)
    df_wash_program.to_excel(writer, sheet_name='Community-Led WASH Budget', index=False)

# Save the Excel file
print(f'Excel file saved at: {excel_file_path}')
