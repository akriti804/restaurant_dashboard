import streamlit as st
import pandas as pd

# Load Data
data = pd.read_csv("products.csv")

# Title + Logo
st.title("🍴 Restaurant Menu Price Dashboard")
st.write("Compare dishes, track pricing trends & stay ahead of competition.")

# Show Full Menu
st.subheader("📋 Menu Pricing")
st.dataframe(data)

# Price Chart
st.subheader("📈 Price Distribution")
st.bar_chart(data.set_index("product_name")["price"])

# Insights
st.subheader("💡 Insights")
st.write(f"🔹 Average Price: ₹{data['price'].mean():.2f}")
st.write(f"🔹 Most Expensive Dish: {data.loc[data['price'].idxmax(), 'product_name']} (₹{data['price'].max()})")
st.write(f"🔹 Cheapest Dish: {data.loc[data['price'].idxmin(), 'product_name']} (₹{data['price'].min()})")

# Subscription Box
st.subheader("📬 Subscribe for Daily Updates")
email = st.text_input("Enter your email:")
if st.button("Subscribe"):
    if email:
        with open("subscribers.txt", "a") as f:
            f.write(email + "\n")
        st.success("Thank you! You are now subscribed.")
    else:
        st.error("Please enter your email")
