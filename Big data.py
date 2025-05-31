import dask.dataframe as dd
import matplotlib.pyplot as plt

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
