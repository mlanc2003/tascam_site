import os

# List of all pages matching your navigation tabs
templates = [
   
    # Lastest Blogs
    "profile",
    "job_application",
    "application_success",

]

# Where templates should go
base_path = os.path.join("templates", "core")

# Template structure
template_content = """{% extends "base.html" %}
{% block title %}{{ title }} | TASCAM Co Ltd{% endblock %}
{% block content %}

<h1>{{ title }}</h1>
<p>Content for the {{ title }} page will appear here.</p>

{% endblock %}
"""

# Make sure folder exists
os.makedirs(base_path, exist_ok=True)

# Create each HTML file if missing
for name in templates:
    file_path = os.path.join(base_path, f"{name}.html")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(template_content.replace("{{ title }}", name.replace("_", " ").title()))
        print(f"✅ Created: {file_path}")
    else:
        print(f"⚠️ Skipped (already exists): {file_path}")

print("\n✅ All templates created successfully!")