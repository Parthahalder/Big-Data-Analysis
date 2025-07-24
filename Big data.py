import dask.dataframe as dd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset (use your file path)
df = dd.read_csv("Yellow taxi cleaned data.csv", dtype={'tolls_amount': 'float64'})

# Show the first few rows (lazily evaluated)
print(df.head())

# Basic info
print("\nColumns:\n", df.columns)

# Compute basic statistics
print("\nTrip Distance Stats:")
print(df['trip_distance'].describe().compute())

# Average fare amount by payment type
print("\nAverage fare amount by payment type:")
print(df.groupby('payment_type')['fare_amount'].mean().compute())

# Filter out trips greater than 20 miles
long_trips = df[df['trip_distance'] > 20]
print(f"\nLong Trips Count: {long_trips.shape[0].compute()}")
df['Pick up date'] = dd.to_datetime(df['Pick up date'])
daily_trips = df.groupby(df['Pick up date']).count()
print("\nTotal Trips Per Day:\n", daily_trips)
corr = df['trip_distance'].corr(df['fare_amount']).compute()
print(f'Correlation between trip distance and fare amount: {corr:.2f}')
sample = df[['trip_distance', 'fare_amount']].sample(frac=0.01).compute()
plt.scatter(sample['trip_distance'], sample['fare_amount'], alpha=0.3)
plt.xlabel('Trip Distance')
plt.ylabel('Fare Amount')
plt.title('Trip Distance vs Fare Amount')
plt.show()
df['pickup_hour'] = df['Pick up time'].str.split(':').str[0].astype(int)
peak_hours = df.groupby('pickup_hour').size().compute().sort_index()
peak_hours.plot(kind='bar', figsize=(10,5))
plt.xlabel('Pickup Hour')
plt.ylabel('Number of Trips')
plt.title('Number of Trips by Pickup Hour')
plt.show()
top_pickup = df['PULocationID'].value_counts().nlargest(10).compute()
top_dropoff = df['DOLocationID'].value_counts().nlargest(10).compute()
print('Top 10 Pickup Locations:\n', top_pickup)
print('Top 10 Dropoff Locations:\n', top_dropoff)
# Only load the columns needed for tip analysis
total_trips = df.shape[0].compute()
df_tip = df[['tip_amount']]

# Filter and compute safely
trips_with_tips = df_tip[df_tip['tip_amount'] > 0].shape[0].compute()
print(f'Trips with tips: {trips_with_tips}')
percent_tips = (trips_with_tips / total_trips) * 100
avg_tip = df['tip_amount'].mean().compute()
print(f'Percentage of trips with tips: {percent_tips:.2f}%')
print(f'Average tip amount: ${avg_tip:.2f}')
extra_charges = df[['extra', 'mta_tax', 'tolls_amount', 'improvement_surcharge']].mean().compute()
print('Average Extra Charges & Fees:\n', extra_charges)
import matplotlib.pyplot as plt

# Sample a fraction for performance, then compute to pandas
trip_dist_sample = df['trip_distance'].sample(frac=0.1).compute()

plt.figure(figsize=(10,6))
plt.hist(trip_dist_sample, bins=50, color='teal', edgecolor='black')
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Number of Trips')
plt.title('Distribution of Trip Distances')
plt.grid(axis='y', alpha=0.75)
plt.show()
st.title("NYC Yellow Taxi Trip Data Analysis")

# Load the dataset
@st.cache_data
def load_data():
    df = dd.read_csv("Yellow taxi cleaned data.csv", dtype={'tolls_amount': 'float64'})
    df['Pick up date'] = dd.to_datetime(df['Pick up date'])
    df['pickup_hour'] = df['Pick up time'].str.split(':').str[0].astype(int)
    return df

df = load_data()

# Show data sample
if st.checkbox("Show raw data"):
    st.write(df.head())

# Trip Distance Stats
if st.checkbox("Show Trip Distance Stats"):
    st.write(df['trip_distance'].describe().compute())

# Average fare by payment type
if st.checkbox("Average Fare Amount by Payment Type"):
    avg_fare = df.groupby('payment_type')['fare_amount'].mean().compute()
    st.bar_chart(avg_fare)

# Long trips
if st.checkbox("Show Long Trips Count (>20 miles)"):
    long_trips_count = df[df['trip_distance'] > 20].shape[0].compute()
    st.write(f"Trips > 20 miles: {long_trips_count}")

# Trips per day
if st.checkbox("Show Total Trips Per Day"):
    daily_trips = df.groupby(df['Pick up date']).count()['VendorID'].compute()
    st.line_chart(daily_trips)

# Correlation
if st.checkbox("Correlation between Trip Distance and Fare Amount"):
    corr = df['trip_distance'].corr(df['fare_amount']).compute()
    st.write(f"Correlation: {corr:.2f}")

# Scatter Plot
if st.checkbox("Scatter Plot: Trip Distance vs Fare Amount"):
    sample = df[['trip_distance', 'fare_amount']].sample(frac=0.01).compute()
    fig, ax = plt.subplots()
    ax.scatter(sample['trip_distance'], sample['fare_amount'], alpha=0.3)
    ax.set_xlabel("Trip Distance")
    ax.set_ylabel("Fare Amount")
    ax.set_title("Trip Distance vs Fare Amount")
    st.pyplot(fig)

# Pickup hour analysis
if st.checkbox("Trips by Pickup Hour"):
    peak_hours = df.groupby('pickup_hour').size().compute().sort_index()
    st.bar_chart(peak_hours)

# Top Pickup & Dropoff
if st.checkbox("Top 10 Pickup & Dropoff Locations"):
    top_pickup = df['PULocationID'].value_counts().nlargest(10).compute()
    top_dropoff = df['DOLocationID'].value_counts().nlargest(10).compute()
    st.write("Top 10 Pickup Locations:", top_pickup)
    st.write("Top 10 Dropoff Locations:", top_dropoff)

# Tip Analysis
if st.checkbox("Tip Analysis"):
    total_trips = df.shape[0].compute()
    trips_with_tips = df[df['tip_amount'] > 0].shape[0].compute()
    percent_tips = (trips_with_tips / total_trips) * 100
    avg_tip = df['tip_amount'].mean().compute()
    st.write(f"Percentage of Trips with Tips: {percent_tips:.2f}%")
    st.write(f"Average Tip Amount: ${avg_tip:.2f}")

# Extra Charges
if st.checkbox("Average Extra Charges & Fees"):
    extra_charges = df[['extra', 'mta_tax', 'tolls_amount', 'improvement_surcharge']].mean().compute()
    st.write(extra_charges)

# Histogram of Trip Distance
if st.checkbox("Histogram of Trip Distances"):
    trip_dist_sample = df['trip_distance'].sample(frac=0.1).compute()
    fig2, ax2 = plt.subplots()
    ax2.hist(trip_dist_sample, bins=50, color='teal', edgecolor='black')
    ax2.set_xlabel("Trip Distance (miles)")
    ax2.set_ylabel("Number of Trips")
    ax2.set_title("Distribution of Trip Distances")
    st.pyplot(fig2)

#-------------##THANK YOU##------------------#
