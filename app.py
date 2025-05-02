import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import base64

# --- Page config and global styling ---
st.set_page_config(page_title="Pouring Perspectives", layout="wide")
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem !important;
    }
</style>
""", unsafe_allow_html=True)
# --- Background image for intro ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

intro_bg = get_base64_image("data/mass_radiu.jpg")
st.markdown(f"""
    <style>
    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to   {{ opacity: 1; }}
    }}
    @keyframes typing {{
      from {{ width: 0; }}
      to   {{ width: 100%; }}
    }}
    @keyframes blinkCaret {{
      from, to {{ border-color: transparent; }}
      50% {{ border-color: #fff; }}
    }}
    body {{ background-color: #f5f1e7; font-family: 'Inter', sans-serif; }}
    .stApp > header, .stApp > footer {{ visibility: hidden; height: 0; }}
    .intro-container {{
        position: relative;
        z-index: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: center;
        padding: 2rem 1rem;
    }}
    .intro-container::before {{
        content: "";
        background-image: url("data:image/jpeg;base64,{intro_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }}
    .intro-container h1 {{
        font-size: 5rem;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
        opacity: 0;
        animation: fadeIn 2s ease-in-out forwards;
    }}
    .intro-container p:nth-of-type(1) {{
        font-size: 1.6rem;
        max-width: 600px;
        line-height: 1.5;
        color: #fff;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        opacity: 0;
        animation: fadeIn 1.5s ease-in-out 1s forwards;
    }}
    .intro-container p:nth-of-type(2) {{
        font-size: 1.8rem;
        max-width: 600px;
        line-height: 1.5;
        color: #fff;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        opacity: 0;
        animation: fadeIn 1.5s ease-in-out 1s forwards;
    }}
    .intro-container p:nth-of-type(3) {{
        font-size: 1.8rem;
        max-width: 600px;
        line-height: 1.5;
        color: #fff;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        overflow: hidden;
        border-right: .15em solid #fff;
        white-space: nowrap;
        width: 0;
        animation: typing 3s steps(40,end) 3s forwards, blinkCaret .75s step-end infinite 6s;
    }}
    div[role="tablist"] {{
        display: flex !important;
        justify-content: flex-end !important;
        padding-right: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Load data ---
df_coffee_cons = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
df_coffee_prod = pd.read_csv("data/coffee-producing-countries-2025.csv")
df_milk      = pd.read_csv("data/milk-consumption-by-country-2025.csv")
df_pop       = pd.read_csv("data/2018worldpop.csv")
df_gap       = pd.read_csv("data/gapminder_alcohol.csv")
df_pop.rename(columns={"Country": "country"}, inplace=True)

# --- Tabs ---
tabs = st.tabs([
    "Introduction",
    "Design Principles",
    "Color & Accessibility",
    "Visual Encoding",
    "Multivariate Viz",
    "Interactivity & Narrative",
    "Data Prep & Grammar",
    "Conclusion"
])

# --- Introduction (Main Page) ---
with tabs[0]:
    st.markdown("""
    <div class="intro-container">
      <h1>Brewing Perspectives</h1>
      <p>Guide to clear, truthful data visualization.</p>
      <p>Explore Good, Bad, and Ugly examples in each tab.</p>
      <p>P.S. Don't make this plot</p>
    </div>
    """, unsafe_allow_html=True)

# --- Design Principles & Perceptual Accuracy ---
with tabs[1]:
    st.header("Design Principles & Perceptual Accuracy")
    st.markdown("""
    **Why focus on data-ink ratio?**  
    Edward Tufte, in *The Visual Display of Quantitative Information*, argues that minimizing non-data ink sharpens our view of the numbers. This section shows how reducing chartjunk leads to clearer, more honest visualizations.
    """)

    # Good
    st.subheader("✅ Good: High Data-Ink Ratio")
    c1, c2 = st.columns([2,1])
    c1.markdown("**Description:** This bar chart highlights per-capita coffee consumption using a clean, high data-ink ratio design.")
    df = df_coffee_cons.sort_values(
        "CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", 
        ascending=False
    ).head(10)
    fig = px.bar(
        df,
        x="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
        y="country",
        orientation="h",
        color_discrete_sequence=["white"]
    )
    fig.update_traces(marker_line_width=0)
    fig.update_layout(
        xaxis_title="Coffee Consumption per Capita (2022) kg",
        yaxis_title="Country",
        showlegend=False,
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    # Invert bar order: largest on top
    fig.update_yaxes(autorange="reversed")
    fig.update_traces(hovertemplate='%{x} kg <extra></extra>')
    fig.update_layout(title="High Data-Ink Ratio: Coffee Consumption per Capita (kg)")
    c1.plotly_chart(fig, use_container_width=True)
    c2.markdown("""
**Why this works:**  
By maximizing the data-ink ratio and stripping away non-essential decoration, this bar chart directs the viewer’s attention to the true data—per‑capita coffee consumption—allowing precise, fast comparisons.

**Author’s Perspective:**  
Edward Tufte, in *The Visual Display of Quantitative Information*, argues that eliminating chartjunk “sharpens our view of the numbers,” which this design exemplifies. Conversely, Alberto Cairo might note that minimalism can sometimes under-communicate context; in more narrative-driven visuals, brief annotations or contextual cues could be necessary to fully guide the audience.

**Key Takeaways:**
- Use minimal non-data ink to enhance clarity.
- Choose visual encodings that leverage human perceptual strengths.
- Annotate sparingly to provide context without clutter.
    """)
    if c2.checkbox("Show code: Good example", key="good_code"):
        c2.code('''# Good Example Code
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
df = df.sort_values(
    "CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
    ascending=False
).head(10)

fig = px.bar(
    df,
    x="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
    y="country",
    orientation="h",
    color_discrete_sequence=["white"]
)
fig.update_traces(marker_line_width=0)
fig.update_layout(
    xaxis_title="Coffee Consumption per Capita (2022) kg",
    yaxis_title="Country",
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor="rgba(0,0,0,0)"
)
fig.update_yaxes(autorange="reversed")
fig.update_traces(hovertemplate='%{x} kg <extra></extra>')
fig.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: Chartjunk Overload")
    c1, c2 = st.columns([2,1])
    c1.markdown("**Description:** This chart demonstrates 'chartjunk' with excessive gridlines and borders that distract from the data.")
    fig2, ax2 = plt.subplots()
    ax2.barh(
        df["country"], 
        df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"], 
        color='skyblue'
    )
    ax2.grid(True, linestyle='--', linewidth=0.8, alpha=0.5)
    ax2.set_title("Chartjunk Overload: Coffee Consumption per Capita (kg)")
    ax2.invert_yaxis()
    fig2.tight_layout()
    ax2.set_xlabel("Coffee Consumption per Capita (kg)")
    ax2.set_ylabel("Country")
    c1.pyplot(fig2)
    c2.markdown("""
    **Too many gridlines & thick borders**  
    distract from the data.  
    - Remove non-informative elements.  
    - Keep visuals lean.
    """)
    if c2.checkbox("Show code: Bad example", key="bad_code"):
        c2.code('''# Bad Example Code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
df = df.sort_values("CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(df["country"], df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"], color='skyblue')
ax.grid(True, linestyle='--', linewidth=0.8, alpha=0.5)
ax.invert_yaxis()
plt.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: Misleading 3D Effect")
    c1, c2 = st.columns([2,1])
    c1.markdown("**Description:** This pseudo-3D bar chart distorts data perception, showing why 3D effects are misleading.")
    fig3, ax3 = plt.subplots()
    ax3.barh(
        df["country"],
        df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"]*1.1,
        height=0.5, color='lightgray'
    )
    ax3.barh(
        df["country"],
        df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"],
        height=0.5, color='darkgray'
    )
    ax3.set_title("Misleading 3D Effect: Coffee Consumption per Capita (kg)")
    ax3.invert_yaxis()
    fig3.tight_layout()
    ax3.set_xlabel("Coffee Consumption per Capita (kg)")
    ax3.set_ylabel("Country")
    c1.pyplot(fig3)
    c2.markdown("""
**Why this is misleading:**  
Stacking bars with pseudo-3D effects exaggerates differences and distorts perception. The “shadow” bars in light gray inflate the true values, making comparisons less accurate.

**Author’s Perspective:**  
Both Tufte and Cairo warn against misleading visual embellishments. 3D effects, even if only simulated, can bias interpretation and reduce trust.

**Key Takeaways:**
- Avoid pseudo-3D effects—they distort perception.
- Never stack bars unless data is cumulative.
- Clarity and honesty come before style.
    """)
    if c2.checkbox("Show code: Ugly example", key="ugly_code"):
        c2.code('''# Ugly Example Code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
df = df.sort_values("CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(df["country"], df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"]*1.1, height=0.5, color='lightgray')
ax.barh(df["country"], df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"], height=0.5, color='darkgray')
ax.invert_yaxis()
plt.show()''', language="python")



# --- Color & Accessibility ---
with tabs[2]:
    st.header("Color & Accessibility")
    st.markdown("""
    **Why focus on color & accessibility?**  
    Our choice of palette can make or break readability. Perceptually uniform scales like Viridis/Cividis improve interpretation for all users, including those with color vision deficiencies—aligning with Tufte’s principle that form follows function.
    """)

    # Good
    st.subheader("✅ Good: Accessible Palette")
    c1, c2 = st.columns([2,1])
    df_map = df_coffee_prod.sort_values(
        "CoffeeProducing_CoffeeProduction_tonnes_2022", ascending=False
    ).head(15)
    figc1 = px.choropleth(
        df_map,
        locations="country",
        locationmode="country names",
        color="CoffeeProducing_CoffeeProduction_tonnes_2022",
        color_continuous_scale="Viridis"
    )
    figc1.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figc1.update_layout(title="Accessible Palette: Coffee Production by Country")
    c1.plotly_chart(figc1, use_container_width=True)
    c2.markdown("""
**Why this works:**  
Perceptually uniform colormaps like Viridis ensure that equal steps in data are perceived as equal steps in color, avoiding artificial emphasis.

**Author’s Perspective:**  
ICA17 emphasizes accessibility; choosing palettes that work for color-deficient viewers aligns with Tufte’s minimalism—color should serve data, not decorate.

**Key Takeaways:**
- Use monotonic, colorblind-friendly scales.
- Test visuals in grayscale to ensure readability.
- Avoid rainbow palettes that imply false variation.
    """)
    if c2.checkbox("Show code: Good example (Color)", key="color_good_code"):
        c2.code('''# Good Example Code: Accessible Palette
import pandas as pd
import plotly.express as px

df_map = pd.read_csv("data/coffee-producing-countries-2025.csv").sort_values(
    "CoffeeProducing_CoffeeProduction_tonnes_2022", ascending=False
).head(15)

figc1 = px.choropleth(
    df_map,
    locations="country",
    locationmode="country names",
    color="CoffeeProducing_CoffeeProduction_tonnes_2022",
    color_continuous_scale="Viridis"
)
figc1.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: Rainbow Palette")
    c1, c2 = st.columns([2,1])
    figc2 = px.choropleth(
        df_map,
        locations="country",
        locationmode="country names",
        color="CoffeeProducing_CoffeeProduction_tonnes_2022",
        color_continuous_scale="Rainbow"
    )
    figc2.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figc2.update_layout(title="Rainbow Palette: Coffee Production by Country")
    c1.plotly_chart(figc2, use_container_width=True)
    c2.markdown("""
    **Rainbow palettes**  
    - Introduce false steps.  
    - Hard for color-deficient viewers.
    """)
    if c2.checkbox("Show code: Bad example (Color)", key="color_bad_code"):
        c2.code('''# Bad Example Code: Rainbow Palette
import pandas as pd
import plotly.express as px

df_map = pd.read_csv("data/coffee-producing-countries-2025.csv").sort_values(
    "CoffeeProducing_CoffeeProduction_tonnes_2022", ascending=False
).head(15)

figc2 = px.choropleth(
    df_map,
    locations="country",
    locationmode="country names",
    color="CoffeeProducing_CoffeeProduction_tonnes_2022",
    color_continuous_scale="Rainbow"
)
figc2.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: Overloaded Pie")
    c1, c2 = st.columns([2,1])
    figc3 = px.pie(
        df_map,
        values="CoffeeProducing_CoffeeProduction_tonnes_2022",
        names="country"
    )
    figc3.update_traces(textinfo='none')
    figc3.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figc3.update_layout(title="Overloaded Pie: Coffee Production by Country")
    c1.plotly_chart(figc3, use_container_width=True)
    c2.markdown("""
    **Too many discrete colors** overwhelm the eye.  
    - Group minor slices.  
    - Prefer ranked bars.
    """)
    if c2.checkbox("Show code: Ugly example (Color)", key="color_ugly_code"):
        c2.code('''# Ugly Example Code: Overloaded Pie
import pandas as pd
import plotly.express as px

df_map = pd.read_csv("data/coffee-producing-countries-2025.csv").sort_values(
    "CoffeeProducing_CoffeeProduction_tonnes_2022", ascending=False
).head(15)

figc3 = px.pie(
    df_map,
    values="CoffeeProducing_CoffeeProduction_tonnes_2022",
    names="country"
)
figc3.show()''', language="python")

# --- Visual Encoding ---
with tabs[3]:
    st.header("Visual Encoding")
    st.markdown("""
    **Why focus on visual encoding?**  
    The way we map data to visual elements dictates accuracy. Cleveland & McGill’s hierarchy shows position and length yield the most precise judgments, underscoring Tufte’s call for truthful, efficient design.
    """)

    # Good
    st.subheader("✅ Good: Position & Length")
    c1, c2 = st.columns([2,1])
    df_bar = df_coffee_cons.sort_values(
        "CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", ascending=False
    ).head(10)
    figv1 = px.bar(
        df_bar,
        x="country",
        y="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"
    )
    figv1.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figv1.update_layout(
        xaxis_title="Country",
        yaxis_title="Coffee Consumption per Capita (kg)"
    )
    figv1.update_traces(hovertemplate='%{y}<extra></extra>')
    figv1.update_layout(title="Position & Length: Coffee Consumption per Capita by Country")
    c1.plotly_chart(figv1, use_container_width=True)
    c2.markdown("""
**Why this works:**  
Encoding values as aligned bar lengths leverages our innate ability to compare positions, yielding highly accurate judgments.

**Author’s Perspective:**  
Cleveland & McGill’s research ranks position highest in perceptual accuracy; Tufte reinforces that aligned axes minimize mental calculation.

**Key Takeaways:**
- Use bar or dot plots for ranking tasks.
- Keep a common baseline for easy comparison.
- Reserve color for qualitative grouping, not primary value encoding.
    """)
    if c2.checkbox("Show code: Good example (Encoding)", key="enc_good_code"):
        c2.code('''# Good Example Code: Bar encoding
import pandas as pd
import plotly.express as px

df_bar = pd.read_csv("data/coffee-consumption-by-country-2025.csv").sort_values(
    "CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", ascending=False
).head(10)

figv1 = px.bar(
    df_bar,
    x="country",
    y="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"
)
figv1.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: Pie for Ranking")
    c1, c2 = st.columns([2,1])
    figv2 = px.pie(
        df_bar,
        values="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
        names="country"
    )
    figv2.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figv2.update_layout(title="Pie Chart: Coffee Consumption per Capita by Country")
    c1.plotly_chart(figv2, use_container_width=True)
    c2.markdown("""
    **Angles/areas are imprecise**  
    - Hard to order 8% vs 10%.  
    - Bars are better for ranking.
    """)
    if c2.checkbox("Show code: Bad example (Encoding)", key="enc_bad_code"):
        c2.code('''# Bad Example Code: Pie encoding
import pandas as pd
import plotly.express as px

df_bar = pd.read_csv("data/coffee-consumption-by-country-2025.csv").sort_values(
    "CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022", ascending=False
).head(10)

figv2 = px.pie(
    df_bar, values="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
    names="country"
)
figv2.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: Mis-scaled Symbols")
    c1, c2 = st.columns([2,1])
    df_sym = pd.DataFrame({"A":[10], "B":[20]})
    figv3 = px.scatter(
        df_sym,
        x="A",
        y="B",
        size="B",
        size_max=60
    )
    figv3.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figv3.update_layout(title="Mis-scaled Symbols: Encoding Pitfall")
    c1.plotly_chart(figv3, use_container_width=True)
    c2.markdown("""
    **Symbol area must scale linearly**  
    - Mis-sized icons exaggerate differences.  
    - Verify mapping of size to data.
    """)
    if c2.checkbox("Show code: Ugly example (Encoding)", key="enc_ugly_code"):
        c2.code('''# Ugly Example Code: Mis-scaled symbols
import pandas as pd
import plotly.express as px

df_sym = pd.DataFrame({"A":[10], "B":[20]})
figv3 = px.scatter(
    df_sym, x="A", y="B", size="B", size_max=60
)
figv3.show()''', language="python")

# --- Multivariate Visualization ---
with tabs[4]:
    st.header("Multivariate Visualization")
    st.markdown("""
    **Why multivariate visualization?**  
    Real-world data is complex. Techniques like bubble charts or scatter matrices let us explore multiple dimensions simultaneously—though Cairo cautions that clarity must not be sacrificed for richness.
    """)

    # Good
    st.subheader("✅ Good: Bubble Chart")
    c1, c2 = st.columns([2,1])
    figm1 = px.scatter(
        df_gap.dropna(subset=["alcconsumption","incomeperperson","suicideper100th","urbanrate"]),
        x="incomeperperson",
        y="alcconsumption",
        size="suicideper100th",
        color="urbanrate",
        hover_name="country",
        size_max=40,
        log_x=True,
        color_continuous_scale="Viridis"
    )
    figm1.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figm1.update_layout(
        xaxis_title="Income per Person (USD)",
        yaxis_title="Alcohol Consumption per Capita (L)"
    )
    figm1.update_layout(title="Bubble Chart: Alcohol vs Income vs Urbanization vs Suicide")
    c1.plotly_chart(figm1, use_container_width=True)
    c2.markdown("""
**Why this works:**  
Bubble charts encode multiple dimensions—position, size, color—in one view, revealing complex relationships at a glance.

**Author’s Perspective:**  
Alberto Cairo warns that multivariate visuals must balance richness with clarity; careful scaling and tooltips prevent overload.

**Key Takeaways:**
- Limit variables per plot to avoid clutter.
- Cap bubble sizes to prevent occlusion.
- Use color scales that support perceptual consistency.
    """)
    if c2.checkbox("Show code: Good example (Multivariate)", key="multi_good_code"):
        c2.code('''# Good Example Code: Bubble chart
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/gapminder_alcohol.csv").dropna(
    subset=["alcconsumption","incomeperperson","suicideper100th","urbanrate"]
)

figm1 = px.scatter(
    df, x="incomeperperson", y="alcconsumption",
    size="suicideper100th", color="urbanrate",
    hover_name="country", log_x=True,
    size_max=40, color_continuous_scale="Viridis"
)
figm1.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: Overcrowded Scatter")
    c1, c2 = st.columns([2,1])
    figm2 = px.scatter(
        df_gap,
        x="incomeperperson",
        y="alcconsumption",
        title="No filtering → overplotting"
    )
    figm2.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figm2.update_layout(
        xaxis_title="Income per Person (USD)",
        yaxis_title="Alcohol Consumption per Capita (L)"
    )
    figm2.update_layout(title="Overcrowded Scatter: Income vs Alcohol")
    c1.plotly_chart(figm2, use_container_width=True)
    c2.markdown("""
    **Overplotting hides patterns**  
    - Filter or sample data.  
    - Use transparency or jitter.
    """)
    if c2.checkbox("Show code: Bad example (Multivariate)", key="multi_bad_code"):
        c2.code('''# Bad Example Code: Overcrowded scatter
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/gapminder_alcohol.csv")
figm2 = px.scatter(df, x="incomeperperson", y="alcconsumption")
figm2.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: 3D Scatter (fixed)")
    c1, c2 = st.columns([2,1])

    # drop rows with any NaN in these four columns
    df3d = df_gap.dropna(subset=[
        "incomeperperson",
        "alcconsumption",
        "suicideper100th",
        "urbanrate"
    ])

    figm3 = px.scatter_3d(
        df3d,
        x="incomeperperson",
        y="alcconsumption",
        z="suicideper100th",
        color="urbanrate",
        size="urbanrate",
        size_max=20,         # caps the maximum marker size
        title=None
    )
    figm3.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    figm3.update_layout(
        scene=dict(
            xaxis_title="Income per Person (USD)",
            yaxis_title="Alcohol Consumption per Capita (L)",
            zaxis_title="Suicide Rate per 100k"
        )
    )
    figm3.update_layout(title="3D Scatter: Income, Alcohol, and Suicide")
    c1.plotly_chart(figm3, use_container_width=True)

    c2.markdown("""
    **3D scatter with no missing sizes**  
    - We dropped any rows where `urbanrate` (or the other axes) was null.  
    - `size_max` keeps the markers from becoming too large.  
    - Even fixed, 3D often adds confusion—use sparingly!
    """)
    if c2.checkbox("Show code: Ugly example (Multivariate)", key="multi_ugly_code"):
        c2.code('''# Ugly Example Code: 3D scatter
import pandas as pd
import plotly.express as px

df3d = pd.read_csv("data/gapminder_alcohol.csv").dropna(
    subset=["incomeperperson","alcconsumption","suicideper100th","urbanrate"]
)

figm3 = px.scatter_3d(
    df3d, x="incomeperperson", y="alcconsumption", z="suicideper100th",
    color="urbanrate", size="urbanrate", size_max=20
)
figm3.show()''', language="python")
# --- Interactivity & Narrative ---
with tabs[5]:
    st.header("Interactivity & Narrative")
    st.markdown("""
    **Why interactivity & narrative?**  
    Guided exploration makes data come alive. Shneiderman’s mantra—overview, filter, details on demand—and Segel & Heer’s narrative patterns show how interactivity and storytelling engage and inform.
    """)

    # Good
    st.subheader("✅ Good: Overview → Filter → Details")
    c1, c2 = st.columns([2,1])
    continent = st.selectbox("Filter by continent", ["All","Europe","Asia","Americas","Africa"], key="filter")
    df_int = df_gap.copy()
    if continent != "All":
        # placeholder: no continent in gapminder_alcohol, so simulate
        df_int = df_int.sample(100)
    fign1 = px.scatter(
        df_int,
        x="incomeperperson",
        y="alcconsumption",
        hover_name="country",
        title=None
    )
    fign1.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    fign1.update_layout(
        xaxis_title="Income per Person (USD)",
        yaxis_title="Alcohol Consumption per Capita (L)"
    )
    fign1.update_layout(title="Interactive Scatter: Alcohol vs Income")
    c1.plotly_chart(fign1, use_container_width=True)
    c2.markdown("""
**Why this works:**  
Interactive controls let users explore data progressively—overview first, then drill down—enhancing understanding and engagement.

**Author’s Perspective:**  
Shneiderman’s mantra guides modern dashboards; Segel & Heer advocate merging narrative with exploration for optimal insight.

**Key Takeaways:**
- Provide clear filters and zoom options.
- Use hover tooltips for contextual detail.
- Balance author-led story with reader-driven discovery.
    """)
    if c2.checkbox("Show code: Good example (Interactive)", key="int_good_code"):
        c2.code('''# Good Example Code: Interactive scatter
import pandas as pd
import plotly.express as px

df_gap = pd.read_csv("data/gapminder_alcohol.csv")
df_int = df_gap.copy()
fig = px.scatter(
    df_int, x="incomeperperson", y="alcconsumption",
    hover_name="country"
)
fig.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: Static Dump")
    c1, c2 = st.columns([2,1])
    fign2 = px.scatter(df_int, x="incomeperperson", y="alcconsumption")
    fign2.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    fign2.update_layout(
        xaxis_title="Income per Person (USD)",
        yaxis_title="Alcohol Consumption per Capita (L)"
    )
    fign2.update_layout(title="Static Scatter: Alcohol vs Income")
    c1.plotly_chart(fign2, use_container_width=True)
    c2.markdown("""
    **No interactivity**  
    - Viewers can’t explore.  
    - Static charts limit insight.
    """)
    if c2.checkbox("Show code: Bad example (Interactive)", key="int_bad_code"):
        c2.code('''# Bad Example Code: Static scatter
import pandas as pd
import plotly.express as px

df_gap = pd.read_csv("data/gapminder_alcohol.csv")
fign2 = px.scatter(df_gap, x="incomeperperson", y="alcconsumption")
fign2.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: Tool Overload")
    c1, c2 = st.columns([2,1])
    c1.write("Imagine 10+ dropdowns & sliders that do nothing…")
    c2.markdown("""
    **Excessive controls**  
    - Cognitive overload.  
    - Provide only meaningful interactions.
    """)
    if c2.checkbox("Show code: Ugly example (Interactive)", key="int_ugly_code"):
        c2.code('''# Ugly Example Code: Conceptual tool overload
# Pseudocode: avoid excessive UI controls
# Not implemented here as it’s conceptual.''', language="python")

# --- Data Preparation & Grammar of Graphics ---
with tabs[6]:
    st.header("Data Preparation & Grammar of Graphics")
    st.markdown("""
    **Why data prep & grammar of graphics?**  
    Solid visuals start with clean, well-structured data. Hadley Wickham’s layered grammar approach ensures reproducibility and transparency, while Tufte reminds us that good design begins at the data.
    """)

    # Good
    st.subheader("✅ Good: Layered Construction")
    c1, c2 = st.columns([2,1])
    df_merge = pd.merge(df_coffee_cons, df_coffee_prod, on="country").dropna()
    figp1 = px.scatter(
        df_merge,
        x="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
        y="CoffeeProducing_CoffeeProduction_tonnes_2022",
        size="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
        color="CoffeeProducing_CoffeeYield_kgPerHa_2022",
        color_continuous_scale="Viridis"
    )
    figp1.update_layout(margin=dict(l=0,r=0,t=30,b=0))
    figp1.update_layout(
        xaxis_title="Coffee Consumption per Capita (kg)",
        yaxis_title="Coffee Production (tonnes)"
    )
    figp1.update_layout(title="Scatter: Coffee Consumption vs Production")
    c1.plotly_chart(figp1, use_container_width=True)
    c2.markdown("""
**Why this works:**  
A layered grammar-of-graphics approach breaks down visuals into data, marks, and scales, enabling systematic, reproducible construction.

**Author’s Perspective:**  
Hadley Wickham’s framework fosters transparency and modularity; Tufte’s emphasis on clarity extends to both code and graphics.

**Key Takeaways:**
- Build charts in clear, testable layers.
- Explicitly transform and filter data before plotting.
- Document each step for reproducibility and auditability.
    """)
    if c2.checkbox("Show code: Good example (Grammar)", key="prep_good_code"):
        c2.code('''# Good Example Code: Grammar of Graphics
import pandas as pd
import plotly.express as px

df = pd.merge(df_coffee_cons, df_coffee_prod, on="country").dropna()
fig = px.scatter(
    df, x="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
    y="CoffeeProducing_CoffeeProduction_tonnes_2022",
    size="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022",
    color="CoffeeProducing_CoffeeYield_kgPerHa_2022"
)
fig.show()''', language="python")

    # Bad
    st.subheader("🚫 Bad: No Data Checks")
    c1, c2 = st.columns([2,1])
    c2.markdown("""
    **Plot without cleaning**  
    - NaNs and outliers break charts.  
    - Always filter & validate first.
    """)
    if c2.checkbox("Show code: Bad example (Grammar)", key="prep_bad_code"):
        c2.code('''# Bad Example Code: No data checks
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
# no dropna or filtering
fig = px.bar(df, x="country", y="CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022")
fig.show()''', language="python")

    # Ugly
    st.subheader("💀 Ugly: Hard-coded Munging")
    c1, c2 = st.columns([2,1])
    c2.markdown("""
    **Fragile scripts**  
    - Literal indices & paths.  
    - Break on any schema change.
    """)
    if c2.checkbox("Show code: Ugly example (Grammar)", key="prep_ugly_code"):
        c2.code('''# Ugly Example Code: Hard-coded munging
import pandas as pd

# Fragile hard-coded column names
df = pd.read_csv("data/coffee-consumption-by-country-2025.csv")
value = df["CoffeConsumption_ConsumptionPerCapita_KgPerCapita_2022"].values[0]
print(value)''', language="python")

# --- Conclusion ---
with tabs[7]:
    st.header("Conclusion")
    st.markdown("""
    In this tutorial, we've journeyed through the spectrum of data visualization—from exemplary **Good** practices, through instructive **Bad** pitfalls, to cautionary **Ugly** extremes. Key takeaways include:

    - **Design Principles:** Embrace Tufte’s data-ink ratio and Cleveland & McGill’s perceptual hierarchy to build charts that are immediately clear and accurate.
    - **Color & Accessibility:** Choose perceptually uniform palettes (e.g., Viridis, Cividis) to enhance readability and ensure accessibility for all viewers.
    - **Visual Encoding:** Leverage position and length for precise comparisons; beware of area, angle, and 3D effects that can mislead.
    - **Multivariate Visualization:** Use bubble charts, scatter matrices, and dimensionality reduction thoughtfully to reveal complex relationships without sacrificing clarity.
    - **Interactivity & Narrative:** Follow Shneiderman’s mantra—overview first, zoom & filter, details on demand—to guide users in self-driven exploration.
    - **Data Preparation & Grammar:** Rely on rigorous data cleaning and a layered grammar-of-graphics approach (Wickham) as the foundation for trustworthy, reproducible visuals.

    By contrasting the best designs with common missteps, you now have a robust framework for creating visualizations that are not only beautiful, but, above all, honest and insightful.
    """)
    st.markdown("> “A visualization should be truthful, functional, beautiful, insightful, and enlightening.” — Alberto Cairo")