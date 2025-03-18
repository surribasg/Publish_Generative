import streamlit as st
import requests
import os
from dotenv import load_dotenv
from crewai import Crew
from app.agents import analyst_agent, strategist_agent, consultant_agent
from app.tasks import analyst_task, strategist_task, consultant_task

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# App title
st.title("Market Intelligence with CrewAI")

# List of popular stocks
stocks = ["IBM", "AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NFLX"]

# Dropdown menu to select a stock
symbol = st.selectbox("Select a stock:", stocks)

# Button to fetch stock data
if st.button("Get Data"):
    # Build the URL to fetch the latest stock quote
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the API response is successful
    if response.status_code == 200:
        data = response.json()
        quote = data.get("Global Quote", {})
        
        if quote:
            # Extract relevant information
            current_price = quote.get("05. price", "N/A")
            change = quote.get("09. change", "N/A")
            change_percentage = quote.get("10. change percent", "N/A")

            # Display stock information in Streamlit
            st.subheader("Selected Stock Information:")
            st.write(f"Symbol: {symbol}")
            st.write(f"Last Price: {current_price} USD")
            st.write(f"Change: {change} ({change_percentage})")
            
            # Integrate CrewAI for analysis
            st.subheader("Analysis with CrewAI")

            # Create the agent team with tasks
            crew = Crew(
                agents=[analyst_agent, strategist_agent, consultant_agent], 
                tasks=[analyst_task, strategist_task, consultant_task]
            )
            
            try:
                # Execute the CrewAI analysis
                result = crew.kickoff(inputs={"current_price": current_price, "change": change, "change_percentage": change_percentage})
                
                # Display results in a structured manner
                st.subheader("Market Analysis:")
                st.markdown(analyst_task.output if analyst_task.output else "Analysis not available")

                st.subheader("Marketing Strategy:")
                st.markdown(strategist_task.output if strategist_task.output else "Strategy not available")

                st.subheader("Financial Assessment:")
                st.markdown(consultant_task.output if consultant_task.output else "Assessment not available")
            
            except Exception as e:
                st.error(f"Error executing CrewAI analysis: {str(e)}")
        
        else:
            st.error("No data found for the selected stock symbol.")
    else:
        st.error(f"Request error. Response code: {response.status_code}")

