#   BIG-DATA-ANALYSIS

COMPANY : CODTECH IT SOLUTIONS

NAME : PARTHA PRATIM HALDER

INTERN ID : CT04DF1208

DOMAIN : DATA ANALYTICS

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

DESCRIPTION OF THE TASK PERFORMED ---
This project involves the analysis of a large-scale NYC taxi dataset containing ride-related information such as pickup and drop-off times, trip distances, fare amounts, tips, payment types, and location IDs. Due to the size of the data, Dask was used instead of traditional libraries like pandas, allowing scalable and parallel processing.

Initial steps focused on data cleaning. Date and time columns were combined and converted into datetime objects, but inconsistent formats caused parsing errors, which were resolved by allowing flexible format inference. Numerical fields were validated, and rows with invalid or zero values in key columns like fare amount and trip distance were removed. Categorical fields such as payment type were mapped to meaningful labels for better interpretation.

Analysis was performed to identify tipping behavior, payment preferences, and ride patterns. A count of trips with non-zero tip amounts showed that a considerable number of rides did not include a tip, particularly for short distances. Distribution of payment types revealed that the majority of transactions were made via credit card, followed by cash. Trip distance analysis indicated that most journeys were under 3 miles, though some outliers represented longer rides, likely to airports or outskirts.

Temporal trends were examined by extracting hours from the pickup times. Fare averages were computed per hour, showing that early mornings and evenings had higher activity and sometimes higher average fares, indicating rush hour patterns.

Visualizations were used to support the findings. A scatter plot of trip distance versus tip amount illustrated that while longer trips tend to receive more tips, substantial tips can also occur on short rides. A bar chart displayed payment type distribution, emphasizing the dominance of card-based payments. A line chart of average fare by pickup hour highlighted the variation in pricing and demand throughout the day.

An error during tip amount analysis was traced back to datetime parsing issues rather than the tip data itself. Resolving the date format inconsistency ensured accurate filtering and computation across the dataset.

This analysis demonstrates how large, real-world transportation data can be handled effectively using Dask and how valuable patterns related to user behavior, fare trends, and trip characteristics can be extracted through structured data processing and visualization.







