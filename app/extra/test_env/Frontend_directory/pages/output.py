import streamlit as st

st.set_page_config(page_title="Output")

st.title("API Output")

# Ensure response exists
if "api_response" not in st.session_state:
    st.error("No data found. Please submit the form first.")
else:
    api_response = st.session_state.api_response
    print(f"API Response: {api_response}")
    # Extract values
    resume_length = api_response.get("resume_length", "")
    job_desc_length = api_response.get("job_desc_length", "")
    score_value = api_response.get("score_value", 0)

    # Display results

    # ----- exp
    import streamlit as st
    import plotly.graph_objects as go

    def odometer_gauge(score_value):
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score_value,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Performance Score", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#1f77b4"}, # The color of the "needle" or fill
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': '#ffcccb'}, # Red for low
                    {'range': [50, 80], 'color': '#ffffcc'}, # Yellow for mid
                    {'range': [80, 100], 'color': '#ccffcc'} # Green for high
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': score_value
                }
            }
        ))

        fig.update_layout(paper_bgcolor = "rgba(0,0,0,0)", font = {'color': "darkblue", 'family': "Arial"})
        return fig

    # Streamlit UI
    st.title("Results Dashboard")

    

    # Display the Gauge
    st.plotly_chart(odometer_gauge(score_value*100), use_container_width=True)

    # -------------------------------




    st.text_area("Resume Length", value=str(resume_length), height=100)
    st.text_area("Job Description Length", value=str(job_desc_length), height=100)
