import streamlit as st

# Application title
st.title("Impact of Artificial Light Exposure on Circadian Health")

# Section 1: Understanding the Effects of Blue Light on Sleep and Circadian Rhythms
st.header("Understanding the Effects of Blue Light on Sleep and Circadian Rhythms")
st.write("""
Blue light, a high-energy visible light, plays a crucial role in our circadian rhythms by influencing the production of melatonin, a hormone that regulates sleep. Exposure to blue light, particularly in the evening, can delay melatonin release, resulting in difficulties falling asleep and poor sleep quality. Understanding this impact is essential for better sleep health.
""")
st.markdown("### Key Concepts")
st.markdown("""
- **Circadian Rhythms and Melatonin Production**: The biological clock that regulates sleep-wake cycles.
- **Retinal Photoreceptors**: Cells in the eye sensitive to blue light, affecting circadian rhythms.
- **Sleep Pressure vs. Circadian Drive**: The interaction between sleep need and the body's internal clock.
""")

# Section 2: Tips for Managing Artificial Light Exposure
st.header("Tips for Managing Artificial Light Exposure During Study or Late Work Hours")
st.write("""
Implementing strategies to manage artificial light exposure, especially during late work or study hours, can improve sleep quality. Here are some practical tips:
""")
st.markdown("### Practical Tips")
st.markdown("""
1. **Enable Night Mode**: Activate night mode or warm mode on devices to reduce blue light.
2. **Use Blue Light Filters**: Apps like F.lux adjust screen color based on time of day.
3. **Take Breaks from Screens**: Follow the 20-20-20 rule to reduce eye strain.
4. **Adjust Lighting Intensity**: Dim lights in the evening or use warm-colored lights.
5. **Increase Daylight Exposure**: Ensure exposure to natural light during the day to regulate the circadian clock.
""")

# Section 3: Role of Screen Settings, Light-Blocking Glasses, and Lighting Choices
st.header("The Role of Screen Settings, Light-Blocking Glasses, and Lighting Choices in Sleep Health")
st.write("""
Modern technology offers tools to control blue light exposure:
""")
st.markdown("### Recommended Products and Settings")
st.markdown("""
- **Screen Settings**: Night Shift, F.lux, or Night Light modes on computers and smartphones.
- **Blue Light Blocking Glasses**: Brands like Swanwick, Felix Gray, or Zenni Optical.
- **Smart Lighting**: Adjustable lights like Philips Hue to mimic natural light.
- **Red or Amber Night Lights**: Gentle on circadian rhythms and reduce blue light impact.
- **Light Therapy Lamps**: Useful for morning light exposure to strengthen the sleep-wake cycle.
""")

# Section 4: Further Concepts and Resources
st.header("Further Concepts, Resources, Ideas, and Products")
st.write("Explore more ideas and products that either assist or hinder effective management of artificial light exposure:")

st.markdown("### Additional Concepts")
st.markdown("""
- **Chronotypes and Sensitivity to Light**: Recognizing individual differences in light sensitivity.
- **Light Hygiene**: Setting consistent light routines to avoid disrupting sleep patterns.
- **Emerging Technologies**: AI-powered lighting systems, wearable devices tracking light exposure.
""")

st.markdown("### Resources")
st.markdown("""
- **National Sleep Foundation**: Research articles on sleep and circadian rhythms.
- **Harvard Health**: Accessible information on managing light exposure.
- **Light Measurement Apps**: Apps like LightMeter to measure brightness levels in your environment.
""")

st.markdown("### Potential Hindrances")
st.markdown("""
- **Inconsistent Use of Blue Light Filters**: Irregular use across devices can diminish benefits.
- **High-Intensity Artificial Light in Workspaces**: Strong artificial lights can disrupt evening sleep.
- **Excessive Screen Time**: Long screen hours increase blue light exposure and strain circadian health.
""")

# Interactive Section: User Input on Current Habits
st.header("Interactive: Check Your Light Exposure Habits")
st.write("Answer the following questions to see if your light exposure habits may be affecting your circadian health.")

screen_time = st.slider("How many hours per day do you spend looking at screens?", 1, 16, 8)
night_mode = st.radio("Do you use night mode or blue light filters on your devices?", ["Yes", "No", "Sometimes"])
light_blocking_glasses = st.radio("Do you use blue light-blocking glasses during evening hours?", ["Yes", "No"])
evening_lighting = st.selectbox("What type of lighting do you use in the evening?", ["Warm (yellow/red)", "Cool (white/blue)", "Dimmable/Adjustable"])

# Summary based on user input
st.write("### Your Summary")
if screen_time > 8:
    st.write("- High screen time may increase blue light exposure. Consider using the 20-20-20 rule or taking frequent breaks.")
if night_mode == "No":
    st.write("- You might benefit from enabling night mode on your devices to reduce blue light exposure.")
if light_blocking_glasses == "No":
    st.write("- Consider using blue light-blocking glasses in the evening for additional protection.")
if evening_lighting == "Cool (white/blue)":
    st.write("- Switching to warmer lighting in the evening may improve sleep quality by reducing blue light exposure.")

st.write("Taking small steps to manage your artificial light exposure can make a significant difference in maintaining a healthy sleep-wake cycle.")
