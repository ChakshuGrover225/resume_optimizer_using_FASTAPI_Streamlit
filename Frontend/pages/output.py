import streamlit as st

st.set_page_config(page_title="Output")


# Ensure response exists
if "api_response" not in st.session_state:
    st.error("No data found. Please submit the form first.")
else:
    api_response = st.session_state.api_response
    print(f"API Response: {api_response}")

    # Extract values by mapping Backend/resume_scoring_parser.py Output

    resume_length = api_response.get("Resume", "")               
    job_desc_length = api_response.get("Job Description", "")
    score_value = api_response.get("resume_score", 0)
    resume_summary = api_response.get("resume_summary", "")
    resume_suggestions = api_response.get("resume_suggestion", "")
    recommended_job_title = api_response.get("recommended_job_titles", [] )

    # Display results

    # ----- exp
    import streamlit as st
    import plotly.graph_objects as go

    def odometer_gauge(score_value):
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score_value,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Resume Score", 'font': {'size': 30}},
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

        fig.update_layout(paper_bgcolor = "rgba(0,0,0,0)", font = {'color': "White", 'family': "Arial"})
        return fig

    # Streamlit UI
    st.title("Results Dashboard")

    

    # Display the Gauge
    st.plotly_chart(odometer_gauge(score_value*100), use_container_width=True)

    # -------------------------------
    st.button("Download LaTeX Compatible Resume (not added yet) ")

    st.text_area("Resume Summary", value=str(resume_length)[:100], height=100)
    st.text_area("Job Description Summary", value=str(job_desc_length)[:100], height=100)


    st.markdown("## Summary")
    st.write(resume_summary)

    st.markdown("## Suggestions")
    st.write(resume_suggestions)

    st.markdown("## Job Titles")
    for job in recommended_job_title:
        st.markdown(f"- {job}")

    #st.markdown("## complete json object")
    #st.write(api_response)


