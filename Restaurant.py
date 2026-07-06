import streamlit as st
import pandas as pd

# Set page configurations
st.set_page_config(
    page_title="Mumbai Restaurant Finder",
    page_icon="🍔",
    layout="centered"
)

# 1. Host our curated data set 
restaurant_data = [
    {
        "Restaurant": "Trishna",
        "Location": "Fort / Kala Ghoda",
        "Signature Dish": "King Crab in Butter-Pepper-Garlic (Seafood)",
        "Services": "Dine-in, AC Seating, Brisk Table Service, Bar available",
        "Timings": "12:00 PM - 3:30 PM, 6:30 PM - 12:00 AM"
    },
    {
        "Restaurant": "The Bombay Canteen",
        "Location": "Lower Parel (Kamala Mills)",
        "Signature Dish": "Eggs Kejriwal / Goan Pork Vindaloo (Modern Indian)",
        "Services": "Modern Indoor Dining, Craft Cocktail Bar, Valet Parking, Reservations Recommended",
        "Timings": "12:00 PM - 1:00 AM"
    },
    {
        "Restaurant": "Ashok Vada Pav",
        "Location": "Dadar West",
        "Signature Dish": "Classic Vada Pav with Chura & Spicy Chutney (Street Food)",
        "Services": "Street Food Stall, Quick Takeaway, Outdoor Standing, Budget Friendly",
        "Timings": "11:00 AM - 9:30 PM (Closed Sundays)"
    },
    {
        "Restaurant": "Sardar Pav Bhaji",
        "Location": "Tardeo",
        "Signature Dish": "Heavy Amul Butter Pav Bhaji (Street Mughlai/Veg)",
        "Services": "Casual Dining, Fast-paced Service, Family Seating, Pure Vegetarian",
        "Timings": "12:00 PM - 2:00 AM"
    },
    {
        "Restaurant": "Shree Thaker Bhojanalay",
        "Location": "Kalbadevi / Bhuleshwar",
        "Signature Dish": "Unlimited Heritage Gujarati Thali (Traditional)",
        "Services": "Traditional Fine Sit-down Thali, Unlimited Refills, Pure Veg, Historic Legacy",
        "Timings": "11:30 AM - 3:30 PM, 7:00 PM - 10:30 PM"
    },
    {
        "Restaurant": "Wasabi by Morimoto",
        "Location": "Colaba (Taj Mahal Palace Hotel)",
        "Signature Dish": "Black Cod Miso / Toro Tartare (Japanese Fine Dining)",
        "Services": "Ultra-Luxury Fine Dining, Omakase Live Counter, Private Rooms, Valet Parking",
        "Timings": "12:30 PM - 2:45 PM, 7:00 PM - 11:45 PM"
    }
]

df = pd.DataFrame(restaurant_data)

# 2. UI Layout Setup
st.title("🗺️ Ultimate Mumbai Restaurant Explorer")
st.write("Find the city's highest-rated culinary milestones filtered cleanly by your cravings.")
st.divider()

# Sidebar Interactive Filters
st.sidebar.header("🔍 Filter Options")

# Filter option 1: Search based on what dish/cuisine they want
all_dishes = df["Signature Dish"].tolist()
selected_dish = st.sidebar.selectbox("What are you craving?", ["Show All Dishes"] + all_dishes)

# Filter option 2: Search by specific location pocket
all_locations = sorted(df["Location"].unique())
selected_location = st.sidebar.selectbox("Select Neighborhood", ["All Locations"] + all_locations)

# Apply filter processing logic
filtered_df = df.copy()

if selected_dish != "Show All Dishes":
    filtered_df = filtered_df[filtered_df["Signature Dish"] == selected_dish]

if selected_location != "All Locations":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]


# 3. Presenting the results elegantly
if filtered_df.empty:
    st.warning("No exact matches found for that specific combination. Try broadening your filter options!")
else:
    for index, row in filtered_df.iterrows():
        with st.container():
            st.subheader(f"📍 {row['Restaurant']}")
            
            # Use columns to make reading fast and scannable
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**🗺️ Neighborhood:** {row['Location']}")
                st.markdown(f"**⭐ Must-Order Dish:** `{row['Signature Dish']}`")
            with col2:
                st.markdown(f"**⏰ Timings:** {row['Timings']}")
                st.markdown(f"**🛠️ Services:** *{row['Services']}*")
            
            st.divider()

# Metric view helper just to summarize what's on screen
st.sidebar.markdown(f"**Total Spots Found:** `{len(filtered_df)}`")
