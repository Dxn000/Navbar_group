import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Tailwind Navbar Presentation", page_icon="🌐", layout="wide")

# --- SIDEBAR NAVIGATION & DELIVERABLES ---
st.sidebar.title("📌 Presentation Navigation")
page = st.sidebar.radio("Go to:", [
    "1. Concept Introduction", 
    "2. Live Demonstration Code", 
    "3. Real-World Usage", 
    "4. Class Activity"
])

st.sidebar.markdown("---")
st.sidebar.title("📦 Project Deliverables")
st.sidebar.markdown("🔗 **GitHub Repository:**")
st.sidebar.info("[Dxn000/Navbar_group](https://github.com/Dxn000/Navbar_group)")

st.sidebar.markdown("🚀 **Live Deployed Site:**")
st.sidebar.success("[Live Demo Site](https://dxn000.github.io/Navbar_group/)")

# --- PAGE 1: CONCEPT INTRODUCTION ---
if page == "1. Concept Introduction":
    st.title("🌐 Navbar Component & Responsive Layouts")
    
    # Question 1 Section
    st.markdown("### **Question 1: What is a Navbar Component?**")
    st.write(
        "A Navigation Bar (Navbar) is a critical user interface (UI) element positioned at the top of a webpage. "
        "It acts as the primary directory or map for a website, hosting links to essential pages like 'Home,' 'About,' "
        "'Services,' and 'Contact'."
    )
    st.write(
        "In modern web development, a navbar cannot be rigid. It must be **responsive**, meaning it gracefully "
        "adapts its layout depending on whether a user is viewing the site on a desktop monitor, a tablet, or a mobile phone screen."
    )
    
    st.write("---") # Visual divider Line
    
    # Question 2 Section
    st.markdown("### **Question 2: Why is Tailwind CSS used to build it?**")
    st.write(
        "Traditionally, making a navbar responsive required writing complex custom CSS with multiple `@media` "
        "queries to handle different screen breakpoints. Tailwind CSS radically simplifies this process using a **mobile-first utility approach**:"
    )
    
    # Bullet points for Question 2
    st.markdown("""
    * **Utility-First Classes:** Instead of writing custom CSS rules in a separate stylesheet, you style elements directly in the HTML using predefined classes (e.g., `flex`, `bg-slate-900`, `text-white`). 
    * **Responsive Modifiers:** Tailwind uses intuitive prefixes like `md:` (medium screens/tablets) and `lg:` (large screens/desktops). You can write `hidden md:flex`, which explicitly tells the browser: *\"Hide this menu by default on mobile, but display it using Flexbox on screens 768px and wider.\"*
    * **Speed and Consistency:** It eliminates the need to constantly switch between HTML and CSS files, ensuring faster prototyping and clean, uniform spacing.
    """)

# --- PAGE 2: LIVE DEMONSTRATION ---
elif page == "2. Live Demonstration Code":
    st.title("💻 Live Demonstration Code")
    st.write("Below is the complete source code for our generalized corporate multi-section landing page, featuring a fully sticky, glassmorphic, and responsive layout.")
    
    # Your comprehensive HTML and Tailwind landing page code
    code_snippet = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navbar & General Landing Page Demo</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-100 font-sans">

    <!-- FIXED RESPONSIVE NAVBAR -->
    <nav class="bg-slate-900/90 backdrop-blur-md text-white sticky top-0 z-50 border-b border-slate-800">
        <div class="max-w-6xl mx-auto px-6">
            <div class="flex justify-between items-center h-16">
                
                <div class="text-xl font-bold tracking-wider text-indigo-400">
                    Nexus<span class="text-white">Corp_</span>
                </div>

                <div class="hidden md:flex space-x-8 font-medium">
                    <a href="#overview" class="text-slate-300 hover:text-indigo-400 transition duration-200">Overview</a>
                    <a href="#services" class="text-slate-300 hover:text-indigo-400 transition duration-200">Services</a>
                    <a href="#contact" class="text-slate-300 hover:text-indigo-400 transition duration-200">Contact</a>
                </div>

                <div class="md:hidden flex items-center">
                    <button id="hamburger" class="text-slate-300 hover:text-white focus:outline-none text-2xl">
                        ☰
                    </button>
                </div>

            </div>
        </div>

        <div id="mobile-menu" class="hidden md:hidden bg-slate-800 px-6 py-4 space-y-3 border-t border-slate-700">
            <a href="#overview" class="block text-slate-300 hover:text-indigo-400 py-1">Overview</a>
            <a href="#services" class="block text-slate-300 hover:text-indigo-400 py-1">Services</a>
            <a href="#contact" class="block text-slate-300 hover:text-indigo-400 py-1">Contact</a>
        </div>
    </nav>


    <!-- SECTION 1: OVERVIEW / HERO -->
    <section id="overview" class="min-h-screen flex items-center justify-center px-6 pt-16">
        <div class="max-w-4xl text-center">
            <span class="text-indigo-400 font-mono text-sm tracking-widest uppercase">Welcome to the Next Generation</span>
            <h1 class="text-5xl md:text-7xl font-extrabold text-white mt-2 mb-4 tracking-tight">
                Modern Solutions For Your Digital Presence.
            </h1>
            <p class="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto mb-8">
                We craft clean user interfaces, organize robust data structures, and deploy seamless corporate web solutions engineered to scale.
            </p>
            <a href="#services" class="inline-block bg-indigo-500 hover:bg-indigo-600 text-white font-bold px-8 py-3 rounded transition duration-200">
                Explore Services
            </a>
        </div>
    </section>


    <!-- SECTION 2: SERVICES -->
    <section id="services" class="min-h-screen flex items-center bg-slate-800/50 px-6 py-20">
        <div class="max-w-5xl mx-auto w-full">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-white mb-2">Our Core Offerings</h2>
                <p class="text-slate-400">Discover how we help enterprises transform their digital capabilities.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-slate-800 p-8 rounded-xl border border-slate-700/50">
                    <h3 class="text-xl font-bold text-indigo-400 mb-4">Design & Layout</h3>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Creating exceptional user experiences with fully responsive architectures that render perfectly on mobile, tablet, and desktop viewports.
                    </p>
                </div>
                <div class="bg-slate-800 p-8 rounded-xl border border-slate-700/50">
                    <h3 class="text-xl font-bold text-purple-400 mb-4">Development</h3>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Engineering solid backend infrastructure, handling relational databases securely, and building optimized, logic-driven systems.
                    </p>
                </div>
                <div class="bg-slate-800 p-8 rounded-xl border border-slate-700/50">
                    <h3 class="text-xl font-bold text-pink-400 mb-4">Deployment</h3>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Streamlining version control workflow pipelines via GitHub and hosting final applications on reliable cloud platform architecture.
                    </p>
                </div>
            </div>
        </div>
    </section>


    <!-- SECTION 3: CONTACT -->
    <section id="contact" class="min-h-screen flex items-center px-6 py-20">
        <div class="max-w-xl mx-auto w-full bg-slate-800 p-8 rounded-2xl border border-slate-700/50 shadow-xl">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold text-white mb-2">Get In Touch</h2>
                <p class="text-slate-400 text-sm">Have a project or questions? Leave a message below.</p>
            </div>

            <form class="space-y-4" onsubmit="event.preventDefault();">
                <div>
                    <label class="block text-xs font-mono tracking-wider text-slate-400 uppercase mb-2">Name</label>
                    <input type="text" placeholder="John Doe" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-indigo-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-mono tracking-wider text-slate-400 uppercase mb-2">Email</label>
                    <input type="email" placeholder="john@example.com" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-indigo-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-mono tracking-wider text-slate-400 uppercase mb-2">Message</label>
                    <textarea rows="4" placeholder="Your message here..." class="w-full bg-slate-900 border border-slate-700 rounded-lg p-3 text-white focus:outline-none focus:border-indigo-500 transition"></textarea>
                </div>
                <button class="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-3 rounded-lg transition duration-200">
                    Send Message
                </button>
            </form>
        </div>
    </section>


    <!-- JAVASCRIPT LOGIC -->
    <script>
        const btn = document.getElementById('hamburger');
        const menu = document.getElementById('mobile-menu');

        // Toggle mobile menu visibility
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });

        // Automatically close the mobile menu dropdown whenever a section link is clicked
        const mobileLinks = menu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                menu.classList.add('hidden');
            });
        });
    </script>

</body>
</html>"""
    
    st.code(code_snippet, language="html")
    st.info("💡 **Demo Guide:** Point out the `sticky top-0` class for the pinned navbar layout, `scroll-smooth` within the `<html>` root for target tracking, and how `hidden md:flex` shifts links beautifully.")

# --- PAGE 3: REAL-WORLD USAGE ---
elif page == "3. Real-World Usage":
    st.title("🌍 Real-World Applications")
    st.write("Responsive navbars are mandatory across the modern web. Here is where you see them every day:")
    
    st.markdown("""
    * **E-Commerce (Amazon, Nike):** Compress massive category lists into a compact hamburger menu on phones.
    * **SaaS Dashboards (GitHub, Notion):** Transition top navbars into collapsible slide-out sidebars.
    * **Streaming (Spotify, Netflix):** Swap desktop links for thumb-friendly bottom icon bars on mobile devices.
    """)

# --- PAGE 4: CLASS ACTIVITY ---
elif page == "4. Class Activity":
    st.title("🎯 Interactive Class Activity")
    
