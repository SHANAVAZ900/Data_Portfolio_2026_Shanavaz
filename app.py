import streamlit as st
import os
from PIL import Image

# ------------- Configuration -------------
st.set_page_config(
    page_title="Mohammad S S V K Shanavaz | Database Developer",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------- Assets Loading -------------
def load_image(image_name):
    if os.path.exists(image_name):
        return Image.open(image_name)
    return None

profile_img = load_image("Shanavaz_Personal.jpeg")
cert_img = load_image("DataAnalyst_SqlAssocistive.png")

# ------------- Custom CSS -------------
# Matching the Dark Green & Gold theme from the HTML version
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: #ecfdf5;
    }
    
    /* Global Background Override */
    .stApp {
        background-color: #022c22;
    }

    /* Hide Sidebar elements completely */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #fbbf24;
        color: #022c22;
        border: none;
        border-radius: 5px;
        font-weight: 700;
        padding: 0.4rem 1.2rem; /* Reduced padding */
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d97706;
        color: white;
        border-color: #d97706;
    }

    /* Headers */
    h1, h2, h3 {
        color: #ffffff !important;
    }
    
    .section-title {
        text-align: center;
        margin-top: 1rem; /* Reduced top margin */
        margin-bottom: 1.5rem; /* Reduced bottom margin */
        font-size: 2.2rem;
        font-weight: 700;
    }
    
    /* Timeline Card (Collapsible) */
    .timeline-card {
        background-color: #064e3b;
        padding: 1rem; /* Reduced padding */
        border-radius: 10px;
        margin-bottom: 0.8rem; /* Reduced margin */
        border-left: 5px solid #fbbf24;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: background-color 0.3s;
    }
    .timeline-card:hover {
        background-color: #065f46;
    }
    
    /* HTML Details/Summary Styling */
    details > summary {
        list-style: none; /* Hide default triangle */
        cursor: pointer;
        outline: none;
    }
    details > summary::-webkit-details-marker {
        display: none;
    }
    
    .skill-container {
        background-color: #064e3b;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 1rem; /* Added margin for stacking mobile */
    }
    
    .date-badge {
        background-color: rgba(251, 191, 36, 0.1);
        color: #fbbf24;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Sidebar Navigation Links */
    .nav-link {
        display: block;
        padding: 0.5rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 5px;
        color: #ecfdf5 !important;
        background-color: rgba(255, 255, 255, 0.05);
        text-decoration: none;
        transition: background-color 0.2s;
    }
    .nav-link:hover {
        background-color: rgba(251, 191, 36, 0.2);
        color: #fbbf24 !important;
    }

    a {
        text-decoration: none;
        color: #fbbf24;
    }
</style>
""", unsafe_allow_html=True)

# ------------- Hero Section -------------
# Create a container for the Hero
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="medium")

with col1:
    st.markdown('<p class="subtitle">Database Developer</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 3rem; margin-bottom: 0.5rem;">Hi, I\'m <span class="highlight">Mohammad S S V K Shanavaz</span></h1>', unsafe_allow_html=True)
    st.markdown('### SQL | PostgreSQL | Power BI | Python | FinTech')
    st.markdown("""
    <p style="font-size: 1.1rem; line-height: 1.5; color: #d1fae5; margin-bottom: 1.5rem;">
    Passionate regarding delivering data-driven and high-impact solutions. Proven ability to optimize
    database performance, design scalable architectures, and collaborate with cross-functional teams.
    </p>
    """, unsafe_allow_html=True)
    
    c_btn1, c_btn2 = st.columns([1, 2])
    with c_btn1:
        if st.button("Contact Me"):
            st.session_state['show_contact_info'] = True

with col2:
    if profile_img:
        st.image(profile_img, use_container_width=True, caption="Mohammad S S V K Shanavaz")

if st.session_state.get('show_contact_info'):
    st.info("📧 Email: shanavaz900@gmail.com")

st.markdown("---")

# ------------- About Section -------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)

col_about_img, col_about_text = st.columns([1, 2], gap="medium")

with col_about_img:
    if profile_img:
        st.image(profile_img, use_container_width=True)

with col_about_text:
    st.markdown('<p class="subtitle">Professional Summary</p>', unsafe_allow_html=True)
    st.markdown('<h2>Experienced <span class="highlight">Database Developer</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="font-size: 1.05rem; line-height: 1.6;">
    Database Developer with a Master’s degree in Information Technology from <strong>IIIT Hyderabad</strong> and
    hands-on experience in <strong>SQL Server, PostgreSQL, Power BI, and Python</strong>. 
    Proven ability to optimize database performance, design scalable architectures, and collaborate with cross-functional
    teams. Experienced in government and fintech projects, including onsite work with the Jaipur
    Government at the Bhamashah Data Center.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Competencies")
    ck1, ck2 = st.columns(2)
    with ck1:
        st.write("✅ SQL Server & PostgreSQL")
        st.write("✅ Performance Optimization")
    with ck2:
        st.write("✅ Scalable Architectures")
        st.write("✅ Power BI & Python")

st.markdown("---")

# ------------- Experience Section -------------
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Professional <span class="highlight">Experience</span></h2>', unsafe_allow_html=True)

def render_experience(role, company, date, location, points):
    list_html = ""
    is_clickable_hint = ""
    
    if points:
        list_str = ''.join([f'<li style="margin-bottom: 0.3rem;">{p}</li>' for p in points])
        list_html = f'<div style="margin-top: 0.8rem; padding-left: 1rem; border-left: 1px solid #ffffff30;"><ul>{list_str}</ul></div>'
        # Wrap in details for collapsible behavior
        content = f"""
        <details>
            <summary>
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div style="flex-grow: 1;">
                        <h3 style="margin: 0; font-size: 1.3rem; color: #fbbf24 !important;">{company}</h3>
                        <h4 style="margin: 0.3rem 0; font-size: 1.1rem; color: white;">{role}</h4>
                    </div>
                    <div style="text-align: right; min-width: 120px;">
                        <span class="date-badge">{date}</span>
                        <div style="color: #9ca3af; font-size: 0.85rem; margin-top: 0.2rem;">{location}</div>
                        <div style="color: #fbbf24; font-size: 0.8rem; margin-top: 0.3rem;">(Click to Expand) 👇</div>
                    </div>
                </div>
            </summary>
            {list_html}
        </details>
        """
    else:
        # Fallback/Generic view (should not ideally be reached for Exp/Edu if split, but keeping for safety)
        content = f"""
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
            <div style="margin-bottom: 0.5rem;">
                <h3 style="margin: 0; font-size: 1.3rem; color: #fbbf24 !important;">{company}</h3>
                <h4 style="margin: 0.3rem 0; font-size: 1.1rem; color: white;">{role}</h4>
            </div>
            <div style="text-align: right; min-width: 120px;">
                <span class="date-badge">{date}</span>
                <div style="color: #9ca3af; font-size: 0.85rem; margin-top: 0.2rem;">{location}</div>
            </div>
        </div>
        """
        
    st.markdown(f"""
    <div class="timeline-card">
        {content}
    </div>
    """, unsafe_allow_html=True)

def render_education(institution, degree, date, location):
    # Specialized card for Education to handle column width constraints better
    st.markdown(f"""
    <div class="timeline-card" style="height: 100%; display: flex; flex-direction: column;">
        <div style="flex-grow: 1;">
            <h3 style="margin: 0; font-size: 1.3rem; color: #fbbf24 !important;">{institution}</h3>
            <h4 style="margin: 0.5rem 0; font-size: 1.1rem; color: white;">{degree}</h4>
        </div>
        <div style="margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
            <span class="date-badge">{date}</span>
            <span style="color: #9ca3af; font-size: 0.9rem;">{location}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Job 1
render_experience(
    "Database Developer", "RPost", "Dec 2023 – Sep 2025", "Hyderabad, India",
    [
        "Improved RPortal system performance by approximately 30% through SQL query optimization and indexing strategies.",
        "Designed and maintained backend database architectures for scalable, high-demand systems.",
        "Collaborated with cross-functional teams to align database solutions with business requirements.",
        "Supported AWS RDS integration in proof-of-concept (POC) initiatives."
    ]
)

# Job 2
render_experience(
    "Database Developer", "Transaction Analysts India Pvt. Ltd.", "Mar 2023 – Nov 2023", "Bengaluru, India",
    [
        "Worked on the JAWS project, a high-impact government initiative.",
        "Completed onsite deployment and support in Jaipur for government stakeholders.",
        "Developed and maintained coupon-based systems for customer–government workflows.",
        "Gained hands-on experience working at the Bhamashah Data Center (BSDC)."
    ]
)

# Job 3
render_experience(
    "Database Developer Intern", "Transaction Analysts India Pvt. Ltd.", "Sep 2022 – Feb 2023", "Bengaluru, India",
    [
        "Contributed to multiple projects including CUB, TA, T, and JAWS.",
        "Handled customer-facing and internal production issues during development cycles.",
        "Built dashboards for TA, T, and JAWS projects to support reporting and analytics.",
        "Strengthened SQL development, debugging, and data handling skills."
    ]
)

# Job 4
render_experience(
    "Frontend Developer Intern", "ShopTrade®", "Oct 2021 – Dec 2021", "Bengaluru, India",
    [
        "Worked on the Pglet project as a frontend developer.",
        "Developed drag-and-drop UI components inspired by canvas-based layouts.",
        "Gained exposure to frontend workflows and component-based UI design."
    ]
)

st.markdown("---")

# ------------- Skills Section -------------
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Technical <span class="highlight">Skills</span></h2>', unsafe_allow_html=True)

# Using st.columns for grid layout
sk_col1, sk_col2, sk_col3, sk_col4 = st.columns(4)

def render_skill(icon, title, details):
    return f"""
    <div class="skill-container">
        <div style="font-size: 2rem; color: #fbbf24; margin-bottom: 1rem;">{icon}</div>
        <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">{title}</h3>
        <p style="color: #d1fae5;">{details}</p>
    </div>
    """

with sk_col1:
    st.markdown(render_skill("🗄️", "Databases", "Microsoft SQL Server, PostgreSQL"), unsafe_allow_html=True)
with sk_col2:
    st.markdown(render_skill("💻", "Programming", "SQL, T-SQL, Python"), unsafe_allow_html=True)
with sk_col3:
    st.markdown(render_skill("📊", "Data & BI", "Power BI"), unsafe_allow_html=True)
with sk_col4:
    st.markdown(render_skill("☁️", "Cloud & Tools", "AWS RDS (POC), Visual Studio Code"), unsafe_allow_html=True)

st.markdown("---")

# ------------- Education Section -------------
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">My <span class="highlight">Education</span></h2>', unsafe_allow_html=True)

edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    render_education("IIIT Hyderabad", "Master of Science (MS) in IT", "June 2019 – July 2021", "Hyderabad")

with edu_col2:
    render_education("Amrita Vishwa Vidyapeetham", "B.Tech in ECE", "June 2014 – Nov 2018", "Bengaluru")

st.markdown("---")

# ------------- Certifications Section -------------
st.markdown('<div id="certs"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Certifications</h2>', unsafe_allow_html=True)

c_col1, c_col2, c_col3 = st.columns([1, 2, 1])
with c_col2:
    if cert_img:
        st.image(cert_img, use_container_width=True, caption="Certified Data Analyst & SQL Associate")
    else:
        st.warning("Certification badge image not found (DataAnalyst_SqlAssocistive.png).")

st.markdown("---")

# ------------- Contact Section -------------
st.markdown('<div id="contact-me"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Contact <span class="highlight">Me</span></h2>', unsafe_allow_html=True)

st.write("Open to new opportunities in Database Development and Data Engineering.")

contact_form = st.form(key='contact_form')
with contact_form:
    c_name = st.text_input("Your Name")
    c_email = st.text_input("Your Email")
    c_msg = st.text_area("Your Message")
    submit_button = st.form_submit_button(label='Send Message')

if submit_button:
    st.balloons()
    st.success(f"Thank you, {c_name}! Your message has been sent successfully.")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 5rem; color: #6b7280; font-size: 0.9rem;">
    &copy; 2026 Mohammad S S V K Shanavaz. All rights reserved.
</div>
""", unsafe_allow_html=True)
