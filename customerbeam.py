import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class CustomerTracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Timestamp', 'Event', 'UserID', 'Demographics'])
        
    def track_event(self, timestamp, event, user_id, age=None, region=None):
        new_row = {'Timestamp': timestamp, 'Event': event, 'UserID': user_id, 'Age': age, 'Region': region}
        self.data = self.data.append(new_row, ignore_index=True)
    
    def calculate_customer_churn_rate(self):
        total_customers = len(self.data['UserID'].unique())
        churned_customers = self.data[self.data['Event'] == 'Churn'].groupby('UserID').size().count()
        churn_rate = (churned_customers / total_customers) * 100
        return churn_rate

    def calculate_customer_lifetime_value(self):
        # Placeholder for calculating CLV
        return 0

    def calculate_net_promoter_score(self):
        # Placeholder for calculating NPS
        return 0

    def calculate_customer_satisfaction_score(self):
        # Placeholder for calculating CSAT
        return 0

    def calculate_average_revenue_per_user(self):
        total_revenue = self.data[self.data['Event'] == 'Purchase']['Revenue'].sum()
        total_users = len(self.data['UserID'].unique())
        arpu = total_revenue / total_users if total_users > 0 else 0
        return arpu

    def calculate_customer_retention_rate(self):
        total_customers_start = len(self.data[self.data['Event'] == 'First Visit']['UserID'].unique())
        total_customers_end = len(self.data[self.data['Event'] == 'Last Visit']['UserID'].unique())
        retention_rate = (total_customers_end / total_customers_start) * 100
        return retention_rate

    def calculate_conversion_rate(self):
        total_visitors = len(self.data[self.data['Event'] == 'Visit']['UserID'].unique())
        total_purchases = len(self.data[self.data['Event'] == 'Purchase']['UserID'].unique())
        conversion_rate = (total_purchases / total_visitors) * 100 if total_visitors > 0 else 0
        return conversion_rate

    def calculate_average_order_value(self):
        total_revenue = self.data[self.data['Event'] == 'Purchase']['Revenue'].sum()
        total_purchases = len(self.data[self.data['Event'] == 'Purchase'])
        aov = total_revenue / total_purchases if total_purchases > 0 else 0
        return aov

    def calculate_first_contact_resolution_rate(self):
        total_inquiries = len(self.data[self.data['Event'] == 'Inquiry'])
        resolved_first_contact = len(self.data[(self.data['Event'] == 'Inquiry') & (self.data['Resolution'] == 'First Contact')])
        fcr_rate = (resolved_first_contact / total_inquiries) * 100 if total_inquiries > 0 else 0
        return fcr_rate

    def calculate_time_to_resolution(self):
        resolved_inquiries = self.data[(self.data['Event'] == 'Inquiry') & (self.data['Resolution'] == 'Resolved')]
        time_to_resolution = resolved_inquiries['Resolution Time'].mean()
        return time_to_resolution

    def calculate_customer_effort_score(self):
        # Placeholder for calculating CES
        return 0

    def calculate_repeat_purchase_rate(self):
        total_customers = len(self.data[self.data['Event'] == 'Purchase']['UserID'].unique())
        repeat_customers = len(self.data[(self.data['Event'] == 'Purchase') & (self.data['Repeat'] == True)]['UserID'].unique())
        repeat_purchase_rate = (repeat_customers / total_customers) * 100 if total_customers > 0 else 0
        return repeat_purchase_rate

    def calculate_abandonment_rate(self):
        total_checkouts_started = len(self.data[self.data['Event'] == 'Checkout']['UserID'].unique())
        total_checkouts_completed = len(self.data[(self.data['Event'] == 'Checkout') & (self.data['Status'] == 'Completed')]['UserID'].unique())
        abandonment_rate = ((total_checkouts_started - total_checkouts_completed) / total_checkouts_started) * 100 if total_checkouts_started > 0 else 0
        return abandonment_rate
        
    def visualize_data(self):
        # Visualize data using Pandas
        print("Customer Interaction Data:")
        print(self.data)
        
        # Visualize demographics
        print("\nDemographics:")
        demographics_summary = self.data['Demographics'].value_counts()
        print(demographics_summary)
        
        # Plot histograms
        plt.figure(figsize=(10, 5))
        self.data['Event'].value_counts().plot(kind='bar', color='skyblue')
        plt.title('Event Distribution')
        plt.xlabel('Event')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()
        
        # Create event-user matrix
        event_user_matrix = self.data.pivot_table(index='Event', columns='UserID', aggfunc='size', fill_value=0)
        
        # Plot event-user matrix
        plt.figure(figsize=(10, 5))
        plt.imshow(event_user_matrix, cmap='viridis', aspect='auto')
        plt.title('Event-User Matrix')
        plt.xlabel('User ID')
        plt.ylabel('Event')
        plt.colorbar(label='Frequency')
        plt.show()
        
        # Calculate and display metrics
        churn_rate = self.calculate_customer_churn_rate()
        clv = self.calculate_customer_lifetime_value()
        nps = self.calculate_net_promoter_score()
        csat = self.calculate_customer_satisfaction_score()
        arpu = self.calculate_average_revenue_per_user()
        retention_rate = self.calculate_customer_retention_rate()
        conversion_rate = self.calculate_conversion_rate()
        aov = self.calculate_average_order_value()
        fcr_rate = self.calculate_first_contact_resolution_rate()
        time_to_resolution = self.calculate_time_to_resolution()
        ces = self.calculate_customer_effort_score()
        repeat_purchase_rate = self.calculate_repeat_purchase_rate()
        abandonment_rate = self.calculate_abandonment_rate()
        
        print("\nMetrics:")
        print(f"Churn Rate: {churn_rate}")
        print(f"Customer Lifetime Value (CLV): {clv}")
        print(f"Net Promoter Score (NPS): {nps}")
        print(f"Customer Satisfaction Score (CSAT): {csat}")
        print(f"Average Revenue Per User (ARPU): {arpu}")
        print(f"Customer Retention Rate: {retention_rate}")
        print(f"Conversion Rate: {conversion_rate}")
        print(f"Average Order Value (AOV): {aov}")
        print(f"First Contact Resolution Rate: {fcr_rate}")
        print(f"Time to Resolution: {time_to_resolution}")
        print(f"Customer Effort Score (CES): {ces}")
        print(f"Repeat Purchase Rate: {repeat_purchase_rate}")
        print(f"Abandonment Rate: {abandonment_rate}")
        
    def calculate_customer_churn_rate(self):
        total_customers = len(self.data['UserID'].unique())
        churned_customers = self.data[self.data['Event'] == 'Churn'].groupby('UserID').size().count()
        churn_rate = (churned_customers / total_customers) * 100
        return churn_rate
        
    def calculate_customer_lifetime_value(self):
        # Placeholder for calculating CLV
        return 0
        
    def calculate_net_promoter_score(self):
        # Placeholder for calculating NPS
        return 0
        
    def calculate_customer_satisfaction_score(self):
        # Placeholder for calculating CSAT
        return 0
        
    def calculate_average_revenue_per_user(self):
        # Placeholder for calculating ARPU
        return 0
        
    def calculate_customer_retention_rate(self):
        # Placeholder for calculating retention rate
        return 0
        
    def calculate_conversion_rate(self):
        # Placeholder for calculating conversion rate
        return 0
        
    def calculate_average_order_value(self):
        # Placeholder for calculating AOV
        return 0
        
    def calculate_first_contact_resolution_rate(self):
        # Placeholder for calculating FCR rate
        return 0
        
    def calculate_time_to_resolution(self):
        # Placeholder for calculating time to resolution
        return 0
        
    def calculate_customer_effort_score(self):
        # Placeholder for calculating CES
        return 0
        
    def calculate_repeat_purchase_rate(self):
        # Placeholder for calculating repeat purchase rate
        return 0
        
    def calculate_abandonment_rate(self):
        # Placeholder for calculating abandonment rate
        return 0

class CustomerTrackerUI:
    def __init__(self, tracker):
        self.tracker = tracker
        self.root = tk.Tk()
        self.root.title("Customer Tracker")
        
        self.label = ttk.Label(self.root, text="Customer Tracker")
        self.label.pack()
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        
        # Input fields
        self.timestamp_label = ttk.Label(self.frame, text="Timestamp:")
        self.timestamp_label.grid(row=0, column=0)
        self.timestamp_entry = ttk.Entry(self.frame)
        self.timestamp_entry.grid(row=0, column=1)
        
        self.event_label = ttk.Label(self.frame, text="Event:")
        self.event_label.grid(row=1, column=0)
        self.event_entry = ttk.Entry(self.frame)
        self.event_entry.grid(row=1, column=1)
        
        self.user_id_label = ttk.Label(self.frame, text="User ID:")
        self.user_id_label.grid(row=2, column=0)
        self.user_id_entry = ttk.Entry(self.frame)
        self.user_id_entry.grid(row=2, column=1)
        
        self.age_label = ttk.Label(self.frame, text="Age Range:")
        self.age_label.grid(row=3, column=0)
        self.age_var = tk.StringVar()
        self.age_combobox = ttk.Combobox(self.frame, textvariable=self.age_var, values=["Under 18", "18-26", "27-35", "40-99"])
        self.age_combobox.grid(row=3, column=1)
        
        self.region_label = ttk.Label(self.frame, text="Region:")
        self.region_label.grid(row=4, column=0)
        self.region_var = tk.StringVar()
        self.region_combobox = ttk.Combobox(self.frame, textvariable=self.region_var, values=["Region A", "Region B", "Region C"])
        self.region_combobox.grid(row=4, column=1)
        
        # Buttons
        self.track_event_button = ttk.Button(self.frame, text="Track Event", command=self.track_event)
        self.track_event_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.visualize_data_button = ttk.Button(self.frame, text="Visualize Data", command=self.visualize_data)
        self.visualize_data_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Data display
        self.data_display = tk.Text(self.root, height=20, width=60)
        self.data_display.pack()
        
        self.root.mainloop()
        
    def track_event(self):
        timestamp = self.timestamp_entry.get() or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        event = self.event_entry.get()
        user_id = self.user_id_entry.get()
        age = self.age_var.get()
        region = self.region_var.get()
        self.tracker.track_event(timestamp, event, user_id, age=age, region=region)
