
# ----- Start of book_event.py -----
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
from utils import DBAccess, create_styled_frame
from constants import COLORS, FONTS, STYLES

def handle_booking():
    # Booking logic implementation
    pass

# Window setup
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Book Event")
window.geometry("600x400")

user_id = sys.argv[1] if len(sys.argv) > 1 else None
event_id = sys.argv[2] if len(sys.argv) > 2 else None

main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Booking form implementation
# Similar to original book_event_view

window.mainloop()
# ----- End of book_event.py -----

# ----- Start of config.py -----
# config.py
import os

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "food_event_management",
    "pool_name": "food_pool",
    "pool_size": 5
}

# Application Constants
APP_CONSTANTS = {
    "ROLES": ("Host", "Guest"),
    "BOOKING_STATUSES": ("Pending", "Confirmed", "Canceled"),
    "MAX_USERNAME_GEN_ATTEMPTS": 100,
    "MIN_PASSWORD_LENGTH": 6,
    "MAX_EVENTS_PER_PAGE": 10,
    "IMAGE_UPLOAD_PATH": os.path.join("images", "uploads"),
    "ALLOWED_IMAGE_TYPES": [".jpg", ".jpeg", ".png"],
    "DEFAULT_PROFILE_IMAGE": os.path.join("images", "default_profile.png")
}

# Validation Patterns
VALIDATION_PATTERNS = {
    "PHONE": r"^\d{10}$",
    "EMAIL": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    "PINCODE": r"^\d{6}$",
    "TIME": r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
}

# UI Configuration
UI_CONFIG = {
    "MAX_EVENT_DESCRIPTION_LENGTH": 500,
    "DATE_FORMAT": "%Y-%m-%d",
    "TIME_FORMAT": "%H:%M",
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M"
}

# Security Settings
SECURITY_CONFIG = {
    "PASSWORD_HASH_ALGORITHM": "sha256",
    "SESSION_TIMEOUT_MINUTES": 30,
    "MAX_LOGIN_ATTEMPTS": 5
}
# ----- End of config.py -----

# ----- Start of constants.py -----
# =========================
# Color Palette
# =========================
COLORS = {
    'background'      : '#e8f1e4',
    'navbar'          : '#e8f1e4',
    'primary'         : '#2596BE',
    'secondary'       : '#1c7a9e',
    'accent'          : '#00AEEF',
    'accent_dark'     : '#007EA7',
    'sidebar'         : '#E8F5E9',
    'success'         : '#28a745',
    'success_dark'    : '#15803d',
    'danger'          : '#E53935',
    'danger_dark'     : '#B71C1C',
    'text'            : '#FFFFFF',
    'hover'           : '#434343',
    'card_background' : '#FFFFFF',
    'border'          : '#E2E8F0',
    'disabled'        : '#6c757d',
}

# =========================
# Fonts
# =========================
FONTS = {
    'small'        : ('Arial', 10),
    'medium'       : ('Arial', 12),
    'medium_bold'  : ('Arial', 12, 'bold'),
    'large'        : ('Arial', 16),
    'large_bold'   : ('Arial', 16, 'bold'),
    'header'       : ('Arial', 16, 'bold'),
    'small_bold'   : ('Arial', 12, 'bold'),
    'title'        : ('Helvetica', 20, 'bold'),
}

# =========================
# Styles (depends on COLORS and FONTS)
# =========================

STYLES = {
    # General styles
    'bg_color': '#f0f0f0',
    'fg_color': '#333333',
    'font': ('Arial', 12),
    'corner_radius': 10,
    'border_width': 2,
    'entry_width': 200,  # Add this line for entry width

    # Button styles
    'accent_button': {
        'fg_color'   : COLORS['accent'],
        'hover_color': COLORS['accent_dark'],
        'text_color' : COLORS['text'],
        'font'       : FONTS['medium'],
    },

    # Add more components/styles here as needed
}
# =========================
# Styles (depends on COLORS and FONTS)
# =========================

STYLES = {
    # General styles
    'bg_color': '#f0f0f0',
    'fg_color': '#333333',
    'font': ('Arial', 12),
    'corner_radius': 10,
    'border_width': 2,
    'entry_width': 200,  # Entry field width
    'button_width': 150,  # Add this line for button width

    # Button styles
    'accent_button': {
        'fg_color'   : COLORS['accent'],
        'hover_color': COLORS['accent_dark'],
        'text_color' : COLORS['text'],
        'font'       : FONTS['medium'],
    },

    # Add more components/styles here as needed
}

# =========================
# Styles (depends on COLORS and FONTS)
# =========================

STYLES = {
    # General styles
    'bg_color': '#f0f0f0',
    'fg_color': '#333333',
    'font': ('Arial', 12),
    'corner_radius': 10,
    'border_width': 2,
    'entry_width': 200,  # Entry field width
    'button_width': 150,  # Button width

    # Button styles
    'accent_button': {
        'fg_color'   : COLORS['accent'],
        'hover_color': COLORS['accent_dark'],
        'text_color' : COLORS['text'],
        'font'       : FONTS['medium'],
    },

    'danger_button': {  # Add the 'danger_button' style here
        'fg_color'   : COLORS['danger'],  # Set this to an appropriate color (e.g., red)
        'hover_color': COLORS['danger_dark'],  # Darker shade for hover effect
        'text_color' : COLORS['text'],
        'font'       : FONTS['medium'],
    },

    # Add more components/styles here as needed
}


# ----- End of constants.py -----

# ----- Start of contact.py -----
import customtkinter as ctk
import subprocess
from PIL import Image, ImageTk
from utils import create_styled_frame
from constants import COLORS, FONTS, STYLES

def open_page(page):
    if page != "contact":
        subprocess.Popen(['python', f'{page}.py'])
        window.destroy()

# Window configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Contact Us - Food Platform")
window.geometry("800x500")
window.configure(fg_color=COLORS['background'])

# Main container frame
main_frame = create_styled_frame(window)
main_frame.pack(pady=25, padx=25, fill='both', expand=True)

# Configure grid layout
main_frame.grid_rowconfigure(0, weight=0)  # Header row
main_frame.grid_rowconfigure(1, weight=0)  # Navigation row
main_frame.grid_rowconfigure(2, weight=1)  # Content row
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="Food Event Platform",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "black",
    'fg_color': "transparent",
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['secondary']
}

for idx, (text, page) in enumerate([("Home", "home"), ("Contact Us", "contact"), ("Login", "login"), ("Sign Up", "registration")]):
    ctk.CTkButton(
        nav_frame,
        text=text,
        command=lambda p=page: open_page(p),
        **button_style
    ).grid(row=0, column=idx, padx=5)

# Content area frames
left_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
left_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")
right_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Contact Information
contact_content = ctk.CTkFrame(left_frame, fg_color="transparent")
contact_content.pack(pady=50, padx=20, expand=True)

contact_items = [
    ("📍 Address:", "123 Food Street\nNew York, NY 10001"),
    ("📞 Phone:", "+1 (555) 123-4567"),
    ("📧 Email:", "support@foodplatform.com"),
    ("⏰ Hours:", "Mon-Fri: 9AM - 8PM\nSat-Sun: 10AM - 6PM")
]

for row, (icon, text) in enumerate(contact_items):
    ctk.CTkLabel(
        contact_content,
        text=icon,
        font=FONTS['medium'],
        text_color=COLORS['primary']
    ).grid(row=row, column=0, padx=5, pady=5, sticky='w')
    
    ctk.CTkLabel(
        contact_content,
        text=text,
        font=FONTS['medium'],
        text_color="black"
    ).grid(row=row, column=1, padx=5, pady=5, sticky='w')

# Social Media
social_frame = ctk.CTkFrame(contact_content, fg_color="transparent")
social_frame.grid(row=4, columnspan=2, pady=20)

social_links = [
    ("🌐 Website", "www.foodplatform.com"),
    ("📘 Facebook", "/FoodPlatform"),
    ("📸 Instagram", "@FoodPlatform"),
    ("🐦 Twitter", "@FoodPlatform")
]

for col, (platform, handle) in enumerate(social_links):
    ctk.CTkLabel(
        social_frame,
        text=f"{platform}: {handle}",
        font=FONTS['medium'],
        text_color=COLORS['primary'],
        cursor="hand2"
    ).grid(row=0, column=col, padx=10)

# Map Image
original_image = Image.open("images/map.jpg")
image_label = ctk.CTkLabel(right_frame, text="")
image_label.pack(expand=True, fill='both')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized = original_image.resize((new_width, new_height), Image.LANCZOS)
    ctk_img = ctk.CTkImage(light_image=resized, size=(new_width, new_height))
    image_label.configure(image=ctk_img)
    image_label.image = ctk_img

right_frame.bind("<Configure>", resize_image)

window.mainloop()
# ----- End of contact.py -----

# ----- Start of create_event.py -----
import customtkinter as ctk
import subprocess
import sys
from tkinter import filedialog, messagebox, ttk
from datetime import datetime, timedelta
from tkcalendar import DateEntry
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# ================== NAVIGATION ==================

def show_profile():
    subprocess.Popen(['python', 'host_dashboard.py', host_id])
    window.destroy()

def create_event():
    pass  # Already on Create Event

def view_events():
    subprocess.Popen(['python', 'view_events.py', host_id])
    window.destroy()

def view_user_feedback():
    subprocess.Popen(['python', 'view_user_feedback.py', host_id])
    window.destroy()

def view_bookings():
    subprocess.Popen(['python', 'view_bookings.py', host_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== VALIDATION ==================

def validate_datetime():
    try:
        selected_date = date_entry.get_date()
        selected_time = time_combobox.get()
        event_dt = datetime.strptime(f"{selected_date} {selected_time}", "%Y-%m-%d %H:%M")
        return event_dt > datetime.now()
    except ValueError:
        return False

dish_entries = []

def create_dish_fields():
    try:
        num_dishes = int(num_dishes_entry.get())
        if num_dishes < 1 or num_dishes > 10:
            raise ValueError
        for entry in dish_entries:
            entry.destroy()
        dish_entries.clear()
        for i in range(num_dishes):
            ctk.CTkLabel(dishes_frame, text=f"Dish {i+1}:", font=FONTS['medium'],
                         text_color=COLORS['primary']).grid(row=i, column=0, sticky='w', pady=2)
            entry = ctk.CTkEntry(dishes_frame, font=FONTS['medium'], width=250)
            entry.grid(row=i, column=1, pady=2, padx=5)
            dish_entries.append(entry)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number between 1-10")

def submit_event():
    event_data = {
        'name': event_name_entry.get().strip(),
        'address': address_entry.get().strip(),
        'pincode': pincode_entry.get().strip(),
        'date': date_entry.get_date(),
        'time': time_combobox.get(),
        'num_dishes': num_dishes_entry.get(),
        'serving': serving_entry.get(),
        'prep_time': prep_time_entry.get(),
        'desc': desc_text.get("1.0", "end-1c"),
        'dishes': [entry.get().strip() for entry in dish_entries],
        'cost_per_head': cost_per_head_entry.get().strip()  # New field
    }

    try:
        num_dishes = int(event_data['num_dishes'])
        serving = int(event_data['serving'])
        prep_time = int(event_data['prep_time'])
        cost_per_head = float(event_data['cost_per_head']) if event_data['cost_per_head'] else 0.0  # Allow 0 or numeric value
    except ValueError:
        messagebox.showerror("Error", "Please fill numeric fields (Number of Dishes, Serving Size, Prep Time, Cost per Head) correctly.")
        return

    if not all([event_data['name'], event_data['address'], event_data['pincode']]):
        messagebox.showerror("Error", "Please fill all required fields (*)")
        return

    if len(event_data['dishes']) != num_dishes or any(d == "" for d in event_data['dishes']):
        messagebox.showerror("Error", f"Please fill all {num_dishes} dish fields")
        return

    if not validate_datetime():
        messagebox.showerror("Error", "Please select a valid future date and time")
        return

    try:
        event_datetime = datetime.strptime(
            f"{event_data['date']} {event_data['time']}",
            "%Y-%m-%d %H:%M"
        )
        DBAccess.execute_update(
            """INSERT INTO EVENTS 
            (host_id, event_name, address, pincode, event_datetime,
            dish_name, serving_size, preparation_time, description, cost_per_head, num_dishes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (host_id, event_data['name'], event_data['address'], event_data['pincode'],
             event_datetime, ", ".join(event_data['dishes']), serving, prep_time,
             event_data['desc'], cost_per_head, num_dishes)
        )
        messagebox.showinfo("Success", "Event created successfully!")
        view_events()
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to create event: {str(e)}")

# ================== MAIN WINDOW ==================

window = ctk.CTk()
window.title("Create New Event")
window.geometry("1000x800")
window.configure(fg_color=COLORS['background'])

host_id = sys.argv[1] if len(sys.argv) > 1 else None
if not host_id:
    messagebox.showerror("Error", "No host specified")
    sys.exit(1)

main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=0)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(main_frame, text="Host Dashboard", font=FONTS['title'],
             text_color=COLORS['primary']).grid(row=0, column=0, pady=20, sticky="nsew")

# ================== NAV BAR ==================

nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "white",
    'fg_color': COLORS['accent'],
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['accent_dark'],
    'width': 120
}

ctk.CTkButton(nav_frame, text="My Profile", command=show_profile, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Create Event", command=create_event, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Events", command=view_events, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Feedback", command=view_user_feedback, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Bookings", command=view_bookings, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Logout", command=logout, **button_style).pack(side='left', padx=5)

# ================== SCROLLABLE CONTENT ==================

content_frame = ctk.CTkFrame(main_frame)
content_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

canvas = ctk.CTkCanvas(content_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(content_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['background'])

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ================== FORM FIELDS ==================

form_container = ctk.CTkFrame(scrollable_frame, fg_color="#e8f1e4")
form_container.pack(pady=20, padx=40, fill='both', expand=True)

left_column = ctk.CTkFrame(form_container, fg_color="transparent")
left_column.pack(side='left', padx=20, pady=20, fill='both', expand=True)

right_column = ctk.CTkFrame(form_container, fg_color="transparent")
right_column.pack(side='right', padx=20, pady=20, fill='both')

fields = [
    ("Event Name*", "event_name_entry"),
    ("Address*", "address_entry"),
    ("Pincode* (6 digits)", "pincode_entry"),
    ("Number of Dishes* (1-10)", "num_dishes_entry"),
    ("Serving Size*", "serving_entry"),
    ("Prep Time* (minutes)", "prep_time_entry"),
    ("Cost per Head* (USD)", "cost_per_head_entry")  # New field
]

for row, (label, var_name) in enumerate(fields):
    ctk.CTkLabel(left_column, text=label, font=FONTS['medium'], text_color=COLORS['primary']).grid(row=row, column=0, sticky='w', pady=5)
    entry = ctk.CTkEntry(left_column, font=FONTS['medium'], width=300)
    entry.grid(row=row, column=1, pady=5, padx=10)
    if "pincode" in var_name:
        entry.configure(validate="key", validatecommand=(window.register(lambda s: s.isdigit() and len(s) <= 6), '%S'))
    elif "num_dishes" in var_name:
        entry.configure(validate="key", validatecommand=(window.register(lambda s: s.isdigit()), '%S'))
        entry.bind("<FocusOut>", lambda e: create_dish_fields())
    elif any(x in var_name for x in ['serving', 'prep_time', 'cost_per_head']):
        entry.configure(validate="key", validatecommand=(window.register(lambda s: s.replace('.', '').isdigit() or s == ''), '%S'))  # Allow decimal
    globals()[var_name] = entry

# Date / Time
ctk.CTkLabel(left_column, text="Date*:", font=FONTS['medium'], text_color=COLORS['primary']).grid(row=len(fields), column=0, sticky='w', pady=5)
date_entry = DateEntry(left_column, font=FONTS['medium'], date_pattern='y-mm-dd', width=33)
date_entry.grid(row=len(fields), column=1, pady=5, padx=10, sticky='w')

ctk.CTkLabel(left_column, text="Time* (HH:MM):", font=FONTS['medium'], text_color=COLORS['primary']).grid(row=len(fields)+1, column=0, sticky='w', pady=5)
time_combobox = ttk.Combobox(left_column, font=FONTS['medium'], width=14)
time_combobox['values'] = [(datetime.min + timedelta(minutes=x)).strftime('%H:%M') for x in range(0, 1440, 15)]
time_combobox.grid(row=len(fields)+1, column=1, pady=5, padx=10, sticky='w')

dishes_frame = ctk.CTkFrame(left_column, fg_color="transparent")
dishes_frame.grid(row=len(fields)+2, column=0, columnspan=2, sticky='w', pady=10)

ctk.CTkLabel(left_column, text="Description:", font=FONTS['medium'], text_color=COLORS['primary']).grid(row=len(fields)+3, column=0, sticky='w', pady=5)
desc_text = ctk.CTkTextbox(left_column, font=FONTS['medium'], width=300, height=100)
desc_text.grid(row=len(fields)+3, column=1, pady=5, padx=10)

# ================== SUBMIT ==================

submit_button = ctk.CTkButton(
    scrollable_frame,
    text="CREATE EVENT",
    command=submit_event,
    fg_color=COLORS['primary'],
    hover_color=COLORS['secondary'],
    font=FONTS['medium_bold'],
    width=200,
    height=40
)
submit_button.pack(pady=30)

window.mainloop()
# ----- End of create_event.py -----

# ----- Start of guest_dashboard.py -----
import customtkinter as ctk
import subprocess
import sys
from tkinter import messagebox
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# ================== NAVIGATION FUNCTIONS ==================
def show_profile():
    content_frame.grid_remove()
    profile_frame.grid(row=2, column=0, sticky="nsew", pady=20)
    cancel_edit()  # Reset to view mode when navigating to profile

def open_search_events():
    subprocess.Popen(['python', 'search_events.py', user_id])
    window.destroy()

def open_view_bookings():
    subprocess.Popen(['python', 'my_bookings.py', user_id, 'guest'])
    window.destroy()

def open_feedback():
    subprocess.Popen(['python', 'provide_feedback.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== PROFILE MANAGEMENT ==================
def enter_edit_mode():
    for field, entry, value_label in entry_widgets:
        value_label.grid_remove()
        entry.grid()
    edit_button.grid_remove()
    save_button.grid()
    cancel_button.grid()

def cancel_edit():
    # Reset values from database
    try:
        user_data = DBAccess.execute_query(
            "SELECT name, email, phone_number, username FROM users WHERE user_id = %s",
            (user_id,)
        )[0]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to refresh data: {str(e)}")
        return

    for field, entry, value_label in entry_widgets:
        entry.delete(0, 'end')
        entry.insert(0, user_data[field])
        entry.grid_remove()
        value_label.configure(text=user_data[field])
        value_label.grid()
    
    save_button.grid_remove()
    cancel_button.grid_remove()
    edit_button.grid()

def save_profile_changes():
    try:
        updates = {}
        for field, entry, value_label in entry_widgets:
            updates[field] = entry.get().strip()

        # Validation
        if not updates.get('name'):
            raise ValueError("Name cannot be empty")
        if not updates['phone_number'].isdigit():
            raise ValueError("Phone number must contain only numbers")

        DBAccess.execute_update(
            """UPDATE users SET 
                name=%s, 
                email=%s, 
                phone_number=%s 
            WHERE user_id=%s""",
            (updates['name'], updates['email'], updates['phone_number'], user_id)
        )
        
        # Update UI components
        for field, entry, value_label in entry_widgets:
            value_label.configure(text=updates[field])
        
        welcome_label.configure(text=f"Welcome, {updates['name']}!")
        messagebox.showinfo("Success", "Profile updated successfully")
        cancel_edit()

    except Exception as e:
        messagebox.showerror("Error", f"Save failed: {str(e)}")

# ================== WINDOW SETUP ==================
window = ctk.CTk()
window.title("Guest Dashboard")
window.geometry("1000x700")
window.configure(fg_color=COLORS['background'])

# Get user ID from command line
user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# Main container
main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Grid configuration
main_frame.grid_rowconfigure(0, weight=0)  # Header
main_frame.grid_rowconfigure(1, weight=0)  # Nav bar
main_frame.grid_rowconfigure(2, weight=1)  # Content
main_frame.grid_columnconfigure(0, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="Guest Dashboard",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, pady=20, sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

nav_buttons = [
    ("My Profile", show_profile),
    ("Search Events", open_search_events),
    ("View Bookings", open_view_bookings),
    ("Feedback", open_feedback),
    ("Logout", logout)
]

for (label, action) in nav_buttons:
    ctk.CTkButton(
        nav_frame, 
        text=label,
        command=action,
        width=120,
        fg_color=COLORS['accent'],
        hover_color=COLORS['accent_dark'],
        text_color="white",
        font=FONTS['medium']
    ).pack(side='left', padx=10, pady=5)

# Profile Frame
profile_frame = ctk.CTkFrame(main_frame, fg_color=COLORS['background'])

try:
    user_data = DBAccess.execute_query(
        "SELECT name, email, phone_number, username FROM users WHERE user_id = %s",
        (user_id,)
    )[0]
except Exception as e:
    messagebox.showerror("Error", f"Failed to load profile: {str(e)}")
    user_data = {'name': 'Guest', 'email': 'N/A', 'phone_number': 'N/A', 'username': 'N/A'}

profile_content = ctk.CTkFrame(profile_frame, fg_color="transparent")
profile_content.pack(pady=40, padx=40, expand=True)

# Profile details setup
details = [
    ('name', "👤 Name:", user_data['name']),
    ('email', "📧 Email:", user_data['email']),
    ('phone_number', "📱 Phone:", user_data['phone_number']),
    ('username', "🔐 Username:", user_data['username'])
]

entry_widgets = []
for row, (field, label_text, value) in enumerate(details):
    # Label
    ctk.CTkLabel(profile_content, text=label_text, font=FONTS['medium_bold'],
                text_color=COLORS['primary'], width=140).grid(row=row, column=0, padx=10, pady=5, sticky='e')
    
    # Value display
    value_label = ctk.CTkLabel(profile_content, text=value, font=FONTS['medium'],
                              text_color=COLORS['primary'])
    value_label.grid(row=row, column=1, padx=10, pady=5, sticky='w')
    
    # Entry field (only for editable fields)
    if field != 'username':
        entry = ctk.CTkEntry(profile_content, font=FONTS['medium'])
        entry.insert(0, value)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky='w')
        entry.grid_remove()
        entry_widgets.append((field, entry, value_label))
    else:
        ctk.CTkLabel(profile_content, text=value, font=FONTS['medium'],
                    text_color=COLORS['primary']).grid(row=row, column=1, padx=10, pady=5, sticky='w')

# Profile action buttons
button_frame = ctk.CTkFrame(profile_content, fg_color="transparent")
button_frame.grid(row=len(details), column=0, columnspan=2, pady=20)

edit_button = ctk.CTkButton(button_frame, text="Edit Profile",
                           command=enter_edit_mode, **STYLES['accent_button'])
save_button = ctk.CTkButton(button_frame, text="Save Changes",
                           command=save_profile_changes, **STYLES['accent_button'])
cancel_button = ctk.CTkButton(button_frame, text="Cancel",
                             command=cancel_edit, **STYLES['danger_button'])

edit_button.pack(side='left', padx=10)
save_button.pack(side='left', padx=10)
cancel_button.pack(side='left', padx=10)
save_button.pack_forget()
cancel_button.pack_forget()

# Main Content Frame
content_frame = ctk.CTkFrame(main_frame, fg_color=COLORS['background'])

# Welcome message
welcome_label = ctk.CTkLabel(
    content_frame,
    text=f"Welcome, {user_data['name']}!",
    font=FONTS['title'],
    text_color=COLORS['primary']
)
welcome_label.pack(pady=40, anchor='center')

# Quick Actions
actions_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
actions_frame.pack(pady=20)

# Initial layout
profile_frame.grid(row=2, column=0, sticky="nsew", pady=20)
content_frame.grid(row=2, column=0, sticky="nsew", pady=20)
show_profile()


window.mainloop()
# ----- End of guest_dashboard.py -----

# ----- Start of home.py -----
import customtkinter as ctk
import subprocess
from PIL import Image, ImageTk
from utils import create_styled_frame
from constants import COLORS, FONTS, STYLES
from customtkinter import CTkLabel, CTkImage

# Window setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

home_window = ctk.CTk()
home_window.title("Food Event Home")
home_window.geometry("800x500")
home_window.configure(fg_color=COLORS['accent'])

def open_page(page):
    if page != "home":
        subprocess.Popen(['python', f'{page}.py'])
        home_window.destroy()

# Main container frame
main_frame = create_styled_frame(home_window)
main_frame.pack(pady=25, padx=25, fill='both', expand=True)

# Header
ctk.CTkLabel(
    main_frame,
    text="Food Event Platform",
    font=FONTS['title'],
    text_color=COLORS['primary']
).pack(pady=(10, 20))

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.pack(fill='x', padx=20)

# And update the button_style:
button_style = {
    'font': FONTS['medium'],
    'text_color': "black",
    'fg_color': "transparent",
    'border_color': "#2596BE",  # Direct color instead of COLORS['primary']
    'border_width': 1,
    'hover_color': "#1c7a9e"    # Direct color instead of COLORS['secondary']
}

ctk.CTkButton(nav_frame, text="Home", command=lambda: open_page("home"), **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Contact Us", command=lambda: open_page("contact"), **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Login", command=lambda: open_page("login"), **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Sign Up", command=lambda: open_page("registration"), **button_style).pack(side='left', padx=5)

# Image display frame
image_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
image_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Load the original image
original_image = Image.open("images/home.jpg")  # Replace with your image path

# Create label to display image
image_label = ctk.CTkLabel(image_frame, text="")
image_label.pack(expand=True, fill='both')

# Resize image on window resize
def resize_image(event):
    new_width = event.width
    new_height = event.height
    
    resized = original_image.resize((new_width, new_height), Image.LANCZOS)
    ctk_img = ctk.CTkImage(light_image=resized, size=(new_width, new_height))
    
    image_label.configure(image=ctk_img)
    image_label.image = ctk_img  # Prevent garbage collection

# Bind frame resize to image update
image_frame.bind("<Configure>", resize_image)

home_window.mainloop()
# ----- End of home.py -----

# ----- Start of host_dashboard.py -----
import customtkinter as ctk
import subprocess
import sys
from tkinter import messagebox
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# Command functions
def create_event():
    subprocess.Popen(['python', 'create_event.py', user_id])
    window.destroy()

def view_events():
    subprocess.Popen(['python', 'view_events.py', user_id])
    window.destroy()

def view_user_feedback():
    subprocess.Popen(['python', 'view_user_feedback.py', user_id])
    window.destroy()

def view_bookings():
    subprocess.Popen(['python', 'view_bookings.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# Navigation functions
def show_profile():
    content_frame.grid_remove()
    profile_frame.grid(row=2, column=0, sticky="nsew", pady=20)
    cancel_edit()  # Reset to view mode when navigating to profile

# Profile editing functions
def enter_edit_mode():
    for field, entry, value_label in entry_widgets:
        value_label.grid_remove()
        entry.grid()
    edit_button.grid_remove()
    save_button.grid()
    cancel_button.grid()

def cancel_edit():
    for field, entry, value_label in entry_widgets:
        entry.delete(0, 'end')
        entry.insert(0, value_label.cget("text"))
        entry.grid_remove()
        value_label.grid()
    save_button.grid_remove()
    cancel_button.grid_remove()
    edit_button.grid()

def save_profile_changes():
    try:
        updates = {}
        for field, entry, value_label in entry_widgets:
            updates[field] = entry.get().strip()

        if not updates.get('name'):
            messagebox.showerror("Error", "Name cannot be empty")
            return

        # Use execute_update instead of execute_query
        DBAccess.execute_update(
            "UPDATE Users SET name=%s, email=%s, phone_number=%s WHERE user_id=%s",
            (updates['name'], updates['email'], updates['phone_number'], user_id)
        )
        
        # Update UI components
        for field, entry, value_label in entry_widgets:
            value_label.configure(text=updates[field])
        
        welcome_label.configure(text=f"Welcome back, {updates['name']}!")
        messagebox.showinfo("Success", "Profile updated successfully")
        cancel_edit()

    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to save changes: {str(e)}")

# Window setup
window = ctk.CTk()
window.title("Host Dashboard")
window.geometry("800x600")
window.configure(fg_color=COLORS['background'])

# Get user ID from command line
user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "No user specified")
    sys.exit(1)

# Main container
main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Grid configuration
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=0)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="Host Dashboard",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, pady=20, sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "white",
    'fg_color': COLORS['accent'],
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['accent_dark'],
    'width': 120
}


# Navigation buttons
ctk.CTkButton(nav_frame, text="My Profile", command=show_profile, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Create Event", command=create_event, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Events", command=view_events, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Feedback", command=view_user_feedback, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Bookings", command=view_bookings, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Logout", command=logout, **button_style).pack(side='left', padx=5)

# Profile Frame
profile_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")

try:
    user_data = DBAccess.execute_query(
        "SELECT name, email, phone_number FROM Users WHERE user_id = %s",
        (user_id,)
    )[0]
except Exception as e:
    messagebox.showerror("Database Error", f"Failed to load profile: {str(e)}")
    user_data = {'name': 'User', 'email': 'N/A', 'phone_number': 'N/A'}

profile_content = ctk.CTkFrame(profile_frame, fg_color="transparent")
profile_content.pack(pady=40, padx=40, expand=True)

# Profile details setup
details = [
    ('name', "Name:", user_data['name']),
    ('email', "Email:", user_data['email']),
    ('phone_number', "Phone:", user_data['phone_number'])
]

entry_widgets = []

for row, (field, label_text, value) in enumerate(details):
    # Label
    ctk.CTkLabel(profile_content, text=label_text, font=FONTS['medium'],
                text_color="black").grid(row=row, column=0, padx=10, pady=5, sticky='e')
    
    # Value display
    value_label = ctk.CTkLabel(profile_content, text=value, font=FONTS['medium'],
                              text_color=COLORS['primary'])
    value_label.grid(row=row, column=1, padx=10, pady=5, sticky='w')
    
    # Entry field
    entry = ctk.CTkEntry(profile_content, font=FONTS['medium'],
                       fg_color="white", text_color="black")
    entry.insert(0, value)
    entry.grid(row=row, column=1, padx=10, pady=5, sticky='w')
    entry.grid_remove()
    
    entry_widgets.append((field, entry, value_label))

# Profile action buttons
button_frame = ctk.CTkFrame(profile_content, fg_color="transparent")
button_frame.grid(row=len(details), column=0, columnspan=2, pady=20)

edit_button = ctk.CTkButton(button_frame, text="Edit Profile",
                           command=enter_edit_mode)
save_button = ctk.CTkButton(button_frame, text="Save Changes",
                           command=save_profile_changes)
cancel_button = ctk.CTkButton(button_frame, text="Cancel",
                             command=cancel_edit)

edit_button.pack(side='left', padx=10)
save_button.pack(side='left', padx=10)
cancel_button.pack(side='left', padx=10)
save_button.pack_forget()
cancel_button.pack_forget()

# Main Content Frame
content_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")

# Welcome message
welcome_label = ctk.CTkLabel(
    content_frame,
    text=f"Welcome back, {user_data['name']}!",
    font=FONTS['title'],
    text_color=COLORS['primary']
)
welcome_label.pack(pady=40)

# Quick Stats
stats_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
stats_frame.pack(pady=20)

stats = [
    ("Total Events", "12"),
    ("Upcoming Events", "3"),
    ("Participants", "145")
]

for col, (label, value) in enumerate(stats):
    stat_block = ctk.CTkFrame(stats_frame, fg_color=COLORS['primary'], corner_radius=8)
    stat_block.grid(row=0, column=col, padx=20)
    
    ctk.CTkLabel(stat_block, text=value, font=FONTS['title'], text_color="white"
                ).pack(pady=12, padx=20)
    ctk.CTkLabel(stat_block, text=label, font=FONTS['medium'], text_color="white"
                ).pack(pady=(0, 12), padx=20)

# Initial layout
profile_frame.grid(row=2, column=0, sticky="nsew", pady=20)
content_frame.grid(row=2, column=0, sticky="nsew", pady=20)
show_profile()

window.mainloop()
# ----- End of host_dashboard.py -----

# ----- Start of login.py -----
import customtkinter as ctk
from tkinter import messagebox
import subprocess
from utils import DBAccess, hash_password, create_styled_frame
from constants import COLORS, FONTS, STYLES
from customtkinter import CTkLabel, CTkImage
from PIL import Image, ImageTk

def authenticate(username, password):
    hashed_pw = hash_password(password)
    query = "SELECT user_id, role FROM Users WHERE username = %s AND password = %s"
    result = DBAccess.execute_query(query, (username, hashed_pw))
    return result[0] if result else None

def on_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    try:
        user = authenticate(username, password)
        if user:
            role = 'host' if user['role'].lower() == 'host' else 'guest'
            subprocess.Popen(['python', f'{role}_dashboard.py', str(user['user_id'])])
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid credentials")
    except Exception as e:
        messagebox.showerror("Error", f"Login failed: {str(e)}")

def show_registration():
    subprocess.Popen(['python', 'registration.py'])
    login_window.destroy()

def open_page(page):
    if page != "login":
        subprocess.Popen(['python', f'{page}.py'])
        login_window.destroy()

# Window setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

login_window = ctk.CTk()
login_window.title("Food Event Login")
login_window.geometry("800x500")
login_window.configure(fg_color=COLORS['background'])

# Main container frame
main_frame = create_styled_frame(login_window)
main_frame.pack(pady=25, padx=25, fill="both", expand=True)

# Configure grid layout
main_frame.grid_rowconfigure(0, weight=0)  # Header row
main_frame.grid_rowconfigure(1, weight=0)  # Navigation row
main_frame.grid_rowconfigure(2, weight=1)  # Content row
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="Food Event Platform",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "black",
    'fg_color': "transparent",
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['secondary']
}

for idx, (label, page) in enumerate([("Home", "home"), ("Contact Us", "contact"), ("Login", "login"), ("Sign Up", "registration")]):
    ctk.CTkButton(
        nav_frame,
        text=label,
        command=lambda p=page: open_page(p),
        **button_style
    ).grid(row=0, column=idx, padx=5)

# Content area frames
left_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
left_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")
right_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Image setup
original_image = Image.open("images/login.jpg")
image_label = ctk.CTkLabel(left_frame, text="")
image_label.pack(expand=True, fill="both")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized = original_image.resize((new_width, new_height), Image.LANCZOS)
    ctk_img = ctk.CTkImage(light_image=resized, size=(new_width, new_height))
    image_label.configure(image=ctk_img)
    image_label.image = ctk_img

left_frame.bind("<Configure>", resize_image)

# Login form
ctk.CTkLabel(
    right_frame,
    text="LOGIN",
    font=FONTS['title'],
    text_color="black"
).pack(pady=(40, 20))

form_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
form_frame.pack(pady=10, padx=20)

# Username field
ctk.CTkLabel(
    form_frame,
    text="Username:",
    font=FONTS['medium'],
    text_color="black"
).pack(pady=(5, 2))
username_entry = ctk.CTkEntry(
    form_frame,
    width=STYLES['entry_width'],
    font=FONTS['medium'],
    corner_radius=STYLES['corner_radius'],
    fg_color="#dcdcdd",
    text_color="black"
)
username_entry.pack(pady=5)

# Password field
ctk.CTkLabel(
    form_frame,
    text="Password:",
    font=FONTS['medium'],
    text_color="black"
).pack(pady=(5, 2))
password_entry = ctk.CTkEntry(
    form_frame,
    show="*",
    width=STYLES['entry_width'],
    font=FONTS['medium'],
    corner_radius=STYLES['corner_radius'],
    fg_color="#dcdcdd",
    text_color="black"
)
password_entry.pack(pady=5)

# Buttons container
button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
button_frame.pack(pady=20)

# Login button
ctk.CTkButton(
    button_frame,
    text="Login",
    command=on_login,
    width=STYLES['button_width'],
    font=FONTS['medium'],
    corner_radius=STYLES['corner_radius'],
    fg_color="#dcdcdd",
    text_color="black",
    hover_color="#e0e0e0"
).pack(pady=10)

# Register button
ctk.CTkButton(
    button_frame,
    text="Create Account",
    command=show_registration,
    fg_color="transparent",
    border_color="black",
    border_width=1,
    text_color="black",
    hover_color="#1c7a9e"
).pack()

login_window.mainloop()
# ----- End of login.py -----

# ----- Start of main.py -----
import subprocess
from utils import DBAccess

def create_tables():
    queries = [
        """CREATE TABLE IF NOT EXISTS Users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            phone_number VARCHAR(10),
            email VARCHAR(100) UNIQUE,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(64),
            role ENUM('Host', 'Guest')
        )""",
        """CREATE TABLE IF NOT EXISTS Events (
            event_id INT AUTO_INCREMENT PRIMARY KEY,
            host_id INT,
            event_name VARCHAR(100),
            address TEXT,
            pincode VARCHAR(6),
            event_datetime DATETIME,
            dish_name VARCHAR(100),
            serving_size INT,
            preparation_time INT,
            description TEXT,
            image LONGBLOB,
            FOREIGN KEY (host_id) REFERENCES Users(user_id)
        )""",
        """CREATE TABLE IF NOT EXISTS Bookings (
            booking_id INT AUTO_INCREMENT PRIMARY KEY,
            event_id INT,
            guest_id INT,
            number_of_attendees INT,
            booking_status ENUM('Pending', 'Confirmed', 'Canceled'),
            FOREIGN KEY (event_id) REFERENCES Events(event_id),
            FOREIGN KEY (guest_id) REFERENCES Users(user_id)
        )""",
        """CREATE TABLE IF NOT EXISTS Feedback (
            feedback_id INT AUTO_INCREMENT PRIMARY KEY,
            event_id INT,
            guest_id INT,
            rating INT,
            review TEXT,
            FOREIGN KEY (event_id) REFERENCES Events(event_id),
            FOREIGN KEY (guest_id) REFERENCES Users(user_id)
        )"""
    ]
    
    try:
        for query in queries:
            DBAccess.execute_update(query)
    except Exception as e:
        print("Database error:", e)

if __name__ == "__main__":
    create_tables()
    subprocess.Popen(['python', 'home.py'])
# ----- End of main.py -----

# ----- Start of my_bookings.py -----
import customtkinter as ctk
import sys
import subprocess
from tkinter import messagebox
from datetime import datetime
from utils import DBAccess, create_styled_frame
from constants import COLORS, FONTS, STYLES

def update_serving_size(event_id, people_change):
    try:
        DBAccess.execute_update(
            "UPDATE events SET serving_size = serving_size + %s WHERE event_id = %s",
            (people_change, event_id)
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update event: {str(e)}")

def cancel_booking(booking_id, event_id, num_people):
    if messagebox.askyesno("Confirm", "Cancel this booking?"):
        try:
            DBAccess.execute_update(
                "UPDATE bookings SET status = 'canceled' WHERE booking_id = %s",
                (booking_id,)
            )
            update_serving_size(event_id, num_people)
            messagebox.showinfo("Success", "Booking canceled")
            load_bookings()
        except Exception as e:
            messagebox.showerror("Error", f"Cancel failed: {str(e)}")

def edit_booking(booking_id, event_id, old_people, max_capacity, controls_frame):
    for widget in controls_frame.winfo_children():
        widget.destroy()

    edit_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
    edit_frame.pack(pady=5)

    people_var = ctk.StringVar(value=str(old_people))
    entry = ctk.CTkEntry(edit_frame, textvariable=people_var, width=80,
                         validate="key", validatecommand=(window.register(lambda p: p.isdigit()), "%P"))
    entry.pack(side='left', padx=5)

    def save_changes():
        try:
            new_people = int(people_var.get())
            if new_people < 1:
                messagebox.showerror("Error", "Must book at least 1 person")
                return
            if new_people > max_capacity:
                messagebox.showerror("Error", f"Only {max_capacity} seats available")
                return

            difference = new_people - old_people
            DBAccess.execute_update(
                "UPDATE bookings SET number_of_attendees = %s WHERE booking_id = %s",
                (new_people, booking_id)
            )
            update_serving_size(event_id, -difference)
            messagebox.showinfo("Success", "Booking updated")
            load_bookings()
        except ValueError:
            messagebox.showerror("Error", "Invalid number")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")

    ctk.CTkButton(edit_frame, text="Save", command=save_changes,
                  **STYLES['accent_button_small']).pack(side='left', padx=2)
    ctk.CTkButton(edit_frame, text="Cancel", command=load_bookings,
                  **STYLES['danger_button_small']).pack(side='left', padx=2)

def load_bookings():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    try:
        # Include paid_amount in the query
        bookings = DBAccess.execute_query("""
            SELECT b.booking_id, b.number_of_attendees, b.paid_amount, b.booking_time, b.status,
                   e.event_id, e.event_name, e.address, e.event_datetime,
                   e.serving_size + b.number_of_attendees AS total_capacity,
                   u.name AS host_name
            FROM bookings b
            JOIN events e ON b.event_id = e.event_id
            JOIN users u ON e.host_id = u.user_id
            WHERE b.guest_id = %s AND b.status != 'canceled'
            ORDER BY e.event_datetime DESC
        """, (user_id,))

        if not bookings:
            ctk.CTkLabel(scrollable_frame, text="No active bookings found",
                         font=FONTS['medium'], text_color=COLORS['primary']).pack(pady=40)
            return

        current_time = datetime.now()
        for book in bookings:
            # Stylish card with shadow effect
            event_frame = ctk.CTkFrame(scrollable_frame, 
                                     fg_color=COLORS['card_background'], 
                                     corner_radius=15,
                                     border_width=1,
                                     border_color=COLORS['border'])
            event_frame.pack(pady=15, padx=20, fill='x')

            event_time = book['event_datetime'] if isinstance(book['event_datetime'], datetime) \
                else datetime.strptime(book['event_datetime'], "%Y-%m-%d %H:%M:%S")
            is_past = event_time < current_time

            # Content container with padding
            content_frame = ctk.CTkFrame(event_frame, fg_color="transparent")
            content_frame.pack(expand=True, fill='both', padx=15, pady=15)

            # Status badge
            status_frame = ctk.CTkFrame(content_frame, 
                                      fg_color=COLORS['secondary'] if not is_past else COLORS['disabled'],
                                      corner_radius=8)
            status_frame.pack(anchor='ne', pady=5)
            status_text = "PAST EVENT" if is_past else "UPCOMING"
            ctk.CTkLabel(status_frame, text=status_text,
                        font=FONTS['small_bold'], text_color="white").pack(padx=10, pady=3)

            # Two-column layout
            left_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            left_column.pack(side='left', fill='both', expand=True)

            right_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            right_column.pack(side='right', padx=10)

            # Event title
            ctk.CTkLabel(left_column, text=book['event_name'].upper(),
                        font=FONTS['large_bold'], text_color=COLORS['primary']).pack(anchor='w', pady=(0, 10))

            # Event details in a grid
            details_frame = ctk.CTkFrame(left_column, fg_color="transparent")
            details_frame.pack(fill='x', pady=5)

            details = [
                (f"🗓  {event_time.strftime('%d %B %Y, %I:%M %p')}", FONTS['medium']),
                (f"📍  {book['address']}", FONTS['medium']),
                (f"👨‍🍳  Host: {book['host_name']}", FONTS['medium']),
                (f"👥  Attendees: {book['number_of_attendees']}", FONTS['medium']),
                (f"💰  Paid Amount: ${book['paid_amount']:.2f}", FONTS['medium_bold']),
                (f"📅  Booked on: {book['booking_time'].strftime('%d %B %Y %I:%M %p')}", FONTS['medium']),
            ]

            for text, font in details:
                ctk.CTkLabel(details_frame, text=text, font=font, text_color=COLORS['primary']).pack(anchor='w', pady=3)

            # Controls column
            controls_frame = ctk.CTkFrame(right_column, fg_color="transparent")
            controls_frame.pack(pady=20)

            if not is_past:
                ctk.CTkButton(controls_frame, text="Edit",
                             command=lambda bid=book['booking_id'], eid=book['event_id'], 
                             op=book['number_of_attendees'], mc=book['total_capacity'], cf=controls_frame: 
                             edit_booking(bid, eid, op, mc, cf),
                             **STYLES['accent_button']).pack(pady=5)
                ctk.CTkButton(controls_frame, text="Cancel",
                             command=lambda bid=book['booking_id'], eid=book['event_id'], 
                             np=book['number_of_attendees']: cancel_booking(bid, eid, np),
                             **STYLES['danger_button']).pack(pady=5)
            else:
                ctk.CTkLabel(controls_frame, text="EVENT ENDED",
                            font=FONTS['medium'], text_color=COLORS['disabled']).pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load bookings: {str(e)}")

# ================== NAVIGATION FUNCTIONS ==================
def show_profile():
    subprocess.Popen(['python', 'guest_dashboard.py', user_id])
    window.destroy()

def open_search_events():
    subprocess.Popen(['python', 'search_events.py', user_id])
    window.destroy()

def open_view_bookings():
    subprocess.Popen(['python', 'my_bookings.py', user_id, 'guest'])
    window.destroy()

def open_feedback():
    subprocess.Popen(['python', 'provide_feedback.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== UI SETUP ==================
window = ctk.CTk()
window.title("Guest Dashboard")
window.geometry("1000x720")
window.configure(fg_color=COLORS['background'])

user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# Header
header_frame = create_styled_frame(window)
header_frame.pack(padx=20, pady=(20, 10), fill='x')

header_label = ctk.CTkLabel(header_frame, text="🍽 Guest Dashboard",
                            font=FONTS['header'], text_color=COLORS['primary'])
header_label.pack(pady=10)

# Navigation Bar
nav_frame = ctk.CTkFrame(header_frame, fg_color=COLORS['navbar'], corner_radius=10)
nav_frame.pack(fill='x', padx=10, pady=5)

for (label, action) in [
    ("Profile", show_profile),
    ("Search Events", open_search_events),
    ("My Bookings", open_view_bookings),
    ("Feedback", open_feedback),
    ("Logout", logout)
]:
    ctk.CTkButton(nav_frame, text=label, command=action, width=120,
                  fg_color=COLORS['accent'], hover_color=COLORS['accent_dark'],
                  text_color="white", font=FONTS['small']).pack(side='left', padx=10, pady=5)

# Scrollable Booking Area
main_frame = create_styled_frame(window)
main_frame.pack(pady=(10, 20), padx=20, fill='both', expand=True)

canvas = ctk.CTkCanvas(main_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['background'])

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

load_bookings()
window.mainloop()
# ----- End of my_bookings.py -----

# ----- Start of provide_feedback.py -----
import customtkinter as ctk
import sys
import subprocess
from tkinter import messagebox
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# ============== Feedback Options ==============
RATINGS = ["Outstanding", "Good", "Average"]
FIELDS = ["Service", "Quality of food", "Cleanliness", "Value of money", "Overall Satisfaction"]

# ================== NAVIGATION FUNCTIONS ==================
def show_profile():
    subprocess.Popen(['python', 'guest_dashboard.py', user_id])
    window.destroy()

def open_search_events():
    subprocess.Popen(['python', 'search_events.py', user_id])
    window.destroy()

def open_view_bookings():
    subprocess.Popen(['python', 'my_bookings.py', user_id, 'guest'])
    window.destroy()

def open_feedback():
    subprocess.Popen(['python', 'provide_feedback.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== UI SETUP ==================
window = ctk.CTk()
window.title("Guest Dashboard")
window.geometry("1000x720")
window.configure(fg_color=COLORS['background'])

user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# Header
header_frame = create_styled_frame(window)
header_frame.pack(padx=20, pady=(20, 10), fill='x')

header_label = ctk.CTkLabel(header_frame, text="🍽 Guest Dashboard",
                            font=FONTS['header'], text_color=COLORS['primary'])
header_label.pack(pady=10)

# Navigation Bar
nav_frame = ctk.CTkFrame(header_frame, fg_color=COLORS['navbar'], corner_radius=10)
nav_frame.pack(fill='x', padx=10, pady=5)

for (label, action) in [
    ("Profile", show_profile),
    ("Search Events", open_search_events),
    ("My Bookings", open_view_bookings),
    ("Feedback", open_feedback),
    ("Logout", logout)
]:
    ctk.CTkButton(nav_frame, text=label, command=action, width=120,
                  fg_color=COLORS['accent'], hover_color=COLORS['accent_dark'],
                  text_color="white", font=FONTS['small']).pack(side='left', padx=10, pady=5)

# Scrollable Feedback Area
main_frame = create_styled_frame(window)
main_frame.pack(pady=(10, 20), padx=20, fill='both', expand=True)

canvas = ctk.CTkCanvas(main_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['background'])

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ============== Event Dropdown ==============
ctk.CTkLabel(scrollable_frame, text="Select Event:", font=FONTS["medium_bold"], text_color=COLORS["primary"]).pack(anchor="w", pady=5)
event_options = {}
event_dropdown = ctk.CTkOptionMenu(scrollable_frame, values=["Loading..."])
event_dropdown.pack(pady=5, fill="x")

try:
    results = DBAccess.execute_query("""
        SELECT e.event_id, e.event_name FROM events e
        JOIN bookings b ON b.event_id = e.event_id
        WHERE b.guest_id = %s
    """, (user_id,))
    if results:
        event_names = [f"{row['event_name']} (ID: {row['event_id']})" for row in results]
        for row in results:
            event_options[f"{row['event_name']} (ID: {row['event_id']})"] = row['event_id']
        event_dropdown.configure(values=event_names)
        event_dropdown.set(event_names[0])
    else:
        event_dropdown.configure(values=["You are not accompanied by any events"])
except Exception as e:
    messagebox.showerror("DB Error", f"Could not load events: {str(e)}")

# ============== Detailed Feedback Fields ==============
ctk.CTkLabel(scrollable_frame, text="Rate the following:", font=FONTS["medium_bold"], text_color=COLORS["primary"]).pack(anchor="w", pady=10)

rating_vars = {}
for field in FIELDS:
    section = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
    section.pack(anchor="w", pady=5, fill="x")

    ctk.CTkLabel(section, text=field + ":", font=FONTS["medium_bold"], text_color=COLORS["primary"]).pack(anchor="w")

    var = ctk.StringVar(value="Good")
    rating_vars[field] = var
    radio_frame = ctk.CTkFrame(section, fg_color="transparent")
    radio_frame.pack(anchor="w", pady=5)

    for option in RATINGS:
        ctk.CTkRadioButton(radio_frame, text=option, variable=var, value=option, font=FONTS["small"]).pack(side="left", padx=10)

# ============== 5-Star Rating ==============
ctk.CTkLabel(scrollable_frame, text="Overall Rating (1-5 stars):", font=FONTS["medium_bold"], text_color=COLORS["primary"]).pack(pady=10, anchor="w")
rating_var = ctk.IntVar(value=5)
stars_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
stars_frame.pack(anchor="w", pady=5)

for i in range(1, 6):
    ctk.CTkRadioButton(stars_frame, text=f"{i} ⭐", variable=rating_var, value=i, font=FONTS["medium"]).pack(side="left", padx=5)

# ============== Comments Section ==============
ctk.CTkLabel(scrollable_frame, text="Suggestions or comments:", font=FONTS["medium_bold"], text_color=COLORS["primary"]).pack(anchor="w", pady=10)
comment_box = ctk.CTkTextbox(scrollable_frame, height=100, font=FONTS["medium"])
comment_box.pack(fill="x", pady=5)

# ============== Submit Handler ==============
def submit_feedback():
    try:
        event_name = event_dropdown.get()
        event_id = event_options.get(event_name)
        overall_rating = rating_var.get()
        review = comment_box.get("1.0", "end").strip()

        if not event_id:
            raise ValueError("Invalid or missing event selection.")

        details = {k: v.get() for k, v in rating_vars.items()}
        detail_text = ", ".join([f"{k}: {v}" for k, v in details.items()])
        full_review = f"{review}\n\nDetailed Ratings:\n{detail_text}"

        DBAccess.execute_update("""
            INSERT INTO feedback (event_id, guest_id, rating, review)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE rating = VALUES(rating), review = VALUES(review)
        """, (event_id, user_id, overall_rating, full_review))

        # Show success popup and handle OK click
        if messagebox.showinfo("Success", "Your feedback has been submitted successfully!"):
            subprocess.Popen(['python', 'guest_dashboard.py', user_id])
            window.destroy()

    except Exception as e:
        messagebox.showerror("Submission Error", f"Failed to submit feedback: {str(e)}")

# ============== Submit Button ==============
ctk.CTkButton(scrollable_frame, text="Submit Feedback", command=submit_feedback, **STYLES["accent_button"]).pack(pady=20)

window.mainloop()
# ----- End of provide_feedback.py -----

# ----- Start of registration.py -----
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import re
from PIL import Image, ImageTk
from utils import DBAccess, hash_password, validate_email, validate_phone, generate_username, create_styled_frame
from constants import COLORS, FONTS, STYLES
from config import VALIDATION_PATTERNS, APP_CONSTANTS

def handle_registration():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    role = role_var.get()

    if not all([name, phone, email, password]):
        messagebox.showerror("Error", "All fields are required")
        return

    if not validate_phone(phone):
        messagebox.showerror("Error", "Invalid phone number (10 digits required)")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return

    if len(password) < APP_CONSTANTS["MIN_PASSWORD_LENGTH"]:
        messagebox.showerror("Error", 
            f"Password must be at least {APP_CONSTANTS['MIN_PASSWORD_LENGTH']} characters")
        return

    try:
        name_parts = name.split()
        if not name_parts:
            raise ValueError("Please enter a valid name")
            
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else "User"
        
        username = generate_username(first_name, last_name)
        
        hashed_pw = hash_password(password)
        query = """INSERT INTO Users (name, phone_number, email, username, password, role)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        DBAccess.execute_update(query, (name, phone, email, username, hashed_pw, role))
        
        messagebox.showinfo("Success", "Registration successful!")
        subprocess.Popen(['python', 'login.py'])
        window.destroy()
        
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Error", f"Registration failed: {str(e)}")

def open_page(page):
    if page != "registration":
        subprocess.Popen(['python', f'{page}.py'])
        window.destroy()

# Window configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Food Platform Registration")
window.geometry("800x500")
window.configure(fg_color=COLORS['background'])

# Main container frame
main_frame = create_styled_frame(window)
main_frame.pack(pady=25, padx=25, fill='both', expand=True)

# Configure grid layout
main_frame.grid_rowconfigure(0, weight=0)  # Header row
main_frame.grid_rowconfigure(1, weight=0)  # Navigation row
main_frame.grid_rowconfigure(2, weight=1)  # Content row
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="Food Event Platform",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "black",
    'fg_color': "transparent",
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['secondary']
}

for idx, (text, page) in enumerate([("Home", "home"), ("Contact Us", "contact"), ("Login", "login"), ("Sign Up", "registration")]):
    ctk.CTkButton(
        nav_frame,
        text=text,
        command=lambda p=page: open_page(p),
        **button_style
    ).grid(row=0, column=idx, padx=5)

# Content area frames
left_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
left_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")
right_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Image handling
original_image = Image.open("images/register.jpg")
image_label = ctk.CTkLabel(left_frame, text="")
image_label.pack(expand=True, fill='both')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized = original_image.resize((new_width, new_height), Image.LANCZOS)
    ctk_img = ctk.CTkImage(light_image=resized, size=(new_width, new_height))
    image_label.configure(image=ctk_img)
    image_label.image = ctk_img

left_frame.bind("<Configure>", resize_image)

# Registration form
ctk.CTkLabel(
    right_frame,
    text="CREATE ACCOUNT",
    font=FONTS['title'],
    text_color="black"
).pack(pady=(40, 20))

form_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
form_frame.pack(pady=10, padx=20)

# Form fields
entry_config = {
    'width': STYLES['entry_width'],
    'font': FONTS['medium'],
    'corner_radius': STYLES['corner_radius'],
    'fg_color': "#dcdcdd",
    'text_color': "black"
}

fields = [
    ("Full Name", 'name', False),
    ("Phone Number", 'phone', False),
    ("Email Address", 'email', False),
    ("Password", 'password', True)
]

entries = {}
for row, (label, field, is_password) in enumerate(fields):
    ctk.CTkLabel(
        form_frame,
        text=label + ":",
        font=FONTS['medium'],
        text_color="black"
    ).grid(row=row, column=0, padx=10, pady=7, sticky='w')
    
    entries[field] = ctk.CTkEntry(
        form_frame,
        show='*' if is_password else '',
        **entry_config
    )
    entries[field].grid(row=row, column=1, padx=10, pady=7)

# Role selection
role_var = ctk.StringVar(value="Guest")
ctk.CTkLabel(
    form_frame,
    text="Account Type:",
    font=FONTS['medium'],
    text_color="black"
).grid(row=4, column=0, pady=10, sticky='w')

role_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
role_frame.grid(row=4, column=1, sticky='w')

radio_config = {
    'variable': role_var,
    'font': FONTS['medium'],
    'text_color': "black",
    'fg_color': "#2C2C2C",
    'hover_color': "#1c7a9e"
}

ctk.CTkRadioButton(role_frame, text="Host", value="Host", **radio_config).pack(side='left', padx=5)
ctk.CTkRadioButton(role_frame, text="Guest", value="Guest", **radio_config).pack(side='left', padx=5)

# Buttons
button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
button_frame.grid(row=5, columnspan=2, pady=20)

ctk.CTkButton(
    button_frame,
    text="Register",
    command=handle_registration,
    width=STYLES['button_width'],
    font=FONTS['medium'],
    corner_radius=STYLES['corner_radius'],
    fg_color="#dcdcdd",
    text_color="black",
    hover_color="#e0e0e0"
).pack(pady=10)

ctk.CTkButton(
    button_frame,
    text="Back to Login",
    command=lambda: subprocess.Popen(['python', 'login.py']),
    fg_color="transparent",
    border_color="black",
    border_width=1,
    text_color="black",
    hover_color="#1c7a9e"
).pack()

# Entry references
name_entry = entries['name']
phone_entry = entries['phone']
email_entry = entries['email']
password_entry = entries['password']

window.mainloop()
# ----- End of registration.py -----

# ----- Start of search_events.py -----
import customtkinter as ctk
import sys
from tkinter import messagebox
from datetime import datetime
from utils import DBAccess, create_styled_frame
from constants import COLORS, FONTS, STYLES
import subprocess

# ================== NAVIGATION FUNCTIONS ==================
def show_profile():
    subprocess.Popen(['python', 'guest_dashboard.py', user_id])
    window.destroy()

def open_search_events():
    subprocess.Popen(['python', 'search_events.py', user_id])
    window.destroy()

def open_view_bookings():
    subprocess.Popen(['python', 'my_bookings.py', user_id, 'guest'])
    window.destroy()

def open_feedback():
    subprocess.Popen(['python', 'provide_feedback.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== BOOKING FUNCTIONALITY ==================

def show_booking_form(event_id, available_seats, btn_frame):
    for widget in btn_frame.winfo_children():
        widget.destroy()
    
    booking_frame = ctk.CTkFrame(btn_frame, fg_color="transparent")
    booking_frame.pack(pady=5)
    
    people_entry = ctk.CTkEntry(booking_frame, width=80, font=FONTS['small'],
                              validate="key", validatecommand=(window.register(validate_number), "%P"))
    people_entry.grid(row=0, column=1, padx=5)
    
    ctk.CTkLabel(booking_frame, text="Number of People:", 
                font=FONTS['small']).grid(row=0, column=0, padx=5)
    people_entry.grid(row=0, column=1, padx=5)
    people_entry.focus()
    
    # Fetch cost_per_head for this event
    cost_query = "SELECT cost_per_head FROM events WHERE event_id = %s"
    cost_data = DBAccess.execute_query(cost_query, (event_id,))
    cost_per_head = float(cost_data[0]['cost_per_head']) if cost_data else 0.0
    
    # Display bill preview
    bill_label = ctk.CTkLabel(booking_frame, text=f"Bill: $0.00", font=FONTS['small'])
    bill_label.grid(row=1, column=0, columnspan=2, pady=5)
    
    def update_bill(*args):
        try:
            num_people = int(people_entry.get() or 0)
            total_bill = num_people * cost_per_head
            bill_label.configure(text=f"Bill: ${total_bill:.2f}")
        except ValueError:
            bill_label.configure(text="Bill: $0.00")
    
    people_entry.bind("<KeyRelease>", update_bill)
    
    ctk.CTkButton(booking_frame, text="Confirm", width=70,
                 command=lambda eid=event_id, seats=available_seats, entry=people_entry: 
                 handle_booking(eid, seats, entry, cost_per_head),
                 fg_color=COLORS['accent'], hover_color=COLORS['accent_dark'],
                 text_color='white', font=FONTS['small']).grid(row=0, column=2, padx=2)
    
    ctk.CTkButton(booking_frame, text="Cancel", width=70,
                 command=load_events,
                 fg_color=COLORS['danger'], hover_color=COLORS['danger_dark'],
                 text_color='white', font=FONTS['small']).grid(row=0, column=3, padx=2)

def handle_booking(event_id, available_seats, entry_widget, cost_per_head):
    try:
        num_people = int(entry_widget.get())
        if num_people <= 0:
            messagebox.showerror("Error", "Number of people must be at least 1")
            return
        if num_people > available_seats:
            messagebox.showerror("Error", f"Only {available_seats} seats available")
            return
        
        total_bill = num_people * cost_per_head
        
        # Prompt for payment confirmation with dummy card details
        payment_dialog = ctk.CTkToplevel(window)
        payment_dialog.title("Payment Confirmation")
        payment_dialog.geometry("300x250")  # Increased height to accommodate buttons
        payment_dialog.transient(window)
        payment_dialog.grab_set()
        
        # Main frame for layout
        main_frame = ctk.CTkFrame(payment_dialog)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        ctk.CTkLabel(main_frame, text=f"Total Bill: ${total_bill:.2f}", 
                    font=FONTS['medium']).pack(pady=10)
        
        ctk.CTkLabel(main_frame, text="Card Number:", font=FONTS['small']).pack()
        card_entry = ctk.CTkEntry(main_frame, width=200)
        card_entry.pack(pady=5)
        
        ctk.CTkLabel(main_frame, text="CVV:", font=FONTS['small']).pack()
        cvv_entry = ctk.CTkEntry(main_frame, width=50)
        cvv_entry.pack(pady=5)
        
        # Button frame for confirm and cancel
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=10)
        
        def confirm_payment():
            card_number = card_entry.get().strip()
            cvv = cvv_entry.get().strip()
            
            if not card_number or not cvv or len(cvv) != 3 or not cvv.isdigit():
                messagebox.showerror("Error", "Please enter a valid card number and 3-digit CVV")
                return
            
            if len(card_number) < 12:
                messagebox.showerror("Error", "Invalid card number")
                return
            
            # Update database with booking and paid amount
            DBAccess.execute_update(
                "UPDATE events SET serving_size = serving_size - %s WHERE event_id = %s",
                (num_people, event_id))
            
            DBAccess.execute_update(
                "INSERT INTO bookings (event_id, guest_id, number_of_attendees, paid_amount, booking_time) VALUES (%s, %s, %s, %s, NOW())",
                (event_id, user_id, num_people, total_bill)
            )
            
            messagebox.showinfo("Success", "Booking and payment confirmed!")
            payment_dialog.destroy()
            load_events()
        
        ctk.CTkButton(button_frame, text="Confirm Payment", 
                     command=confirm_payment,
                     fg_color=COLORS['success'], 
                     hover_color=COLORS['success_dark'],
                     text_color='white', 
                     font=FONTS['small']).pack(side="left", padx=5)
        
        ctk.CTkButton(button_frame, text="Cancel", 
                     command=payment_dialog.destroy,
                     fg_color=COLORS['danger'], 
                     hover_color=COLORS['danger_dark'],
                     text_color='white', 
                     font=FONTS['small']).pack(side="left", padx=5)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
    except Exception as e:
        messagebox.showerror("Error", f"Booking failed: {str(e)}")

def validate_number(new_value):
    return new_value.isdigit() or new_value == ""

# ================== EVENT LOADING & FILTERING ==================
def load_events(pincode=None):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    
    try:
        query = """SELECT e.event_id, e.event_name, e.address, e.pincode, 
                         e.event_datetime, e.serving_size, e.preparation_time,
                         e.dish_name, e.description, e.cost_per_head,
                         u.name AS host_name, u.phone_number AS host_phone, u.email AS host_email
                  FROM events e
                  JOIN users u ON e.host_id = u.user_id
                  WHERE 1=1"""
        params = []
        
        if pincode and pincode.isdigit():
            query += " AND e.pincode = %s"
            params.append(pincode)
            
        query += " ORDER BY e.event_datetime DESC"
        
        events = DBAccess.execute_query(query, params)
        
        if not events:
            ctk.CTkLabel(scrollable_frame, text="No events found", 
                        font=FONTS['medium'], text_color=COLORS['primary']).pack(pady=40)
            return
            
        current_time = datetime.now()
        
        for event in events:
            # Main event card with shadow effect
            event_frame = ctk.CTkFrame(scrollable_frame, 
                                     fg_color=COLORS['card_background'], 
                                     corner_radius=15,
                                     border_width=1,
                                     border_color=COLORS['border'])
            event_frame.pack(fill='x', pady=10, padx=20, anchor='center')

            try:
                datetime_obj = event['event_datetime'] if isinstance(event['event_datetime'], datetime) \
                    else datetime.strptime(event['event_datetime'], "%Y-%m-%d %H:%M:%S")
                is_past_event = datetime_obj < current_time
            except:
                is_past_event = True

            # Status determination
            is_sold_out = event['serving_size'] <= 0 and not is_past_event
            status_text = "CLOSED" if is_past_event else ("SOLD OUT" if is_sold_out else "AVAILABLE")
            status_color = COLORS['disabled'] if is_past_event else (
                COLORS['danger'] if is_sold_out else COLORS['success']
            )

            # Content container with padding
            content_frame = ctk.CTkFrame(event_frame, fg_color="transparent")
            content_frame.pack(expand=True, fill='both', padx=15, pady=15)

            # Status badge
            status_frame = ctk.CTkFrame(content_frame, 
                                      fg_color=status_color, 
                                      corner_radius=8)
            status_frame.pack(anchor='ne', pady=5)
            ctk.CTkLabel(status_frame, 
                        text=status_text, 
                        font=FONTS['small_bold'], 
                        text_color="white").pack(padx=10, pady=3)

            # Two-column layout
            left_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            left_column.pack(side='left', fill='both', expand=True)

            right_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            right_column.pack(side='right', padx=10)

            # Event name with better styling
            ctk.CTkLabel(left_column, 
                        text=event['event_name'].upper(), 
                        font=FONTS['large_bold'], 
                        text_color=COLORS['primary']).pack(anchor='w', pady=(0, 10))

            # Formatted event details
            formatted_dt = datetime_obj.strftime("%d %B %Y, %I:%M %p") if not is_past_event \
                else "Closed on " + datetime_obj.strftime("%d %B %Y")
                
            # Details grid
            details_frame = ctk.CTkFrame(left_column, fg_color="transparent")
            details_frame.pack(fill='x', pady=5)

            # Event details with icons
            details = [
                (f"🗓  {formatted_dt}", FONTS['medium']),
                (f"📍  {event['address']} ({event['pincode']})", FONTS['medium']),
                (f"👨‍🍳  Host: {event['host_name']}", FONTS['medium']),
                (f"📞  Host Phone: {event['host_phone']}", FONTS['medium']),
                (f"📧  Host Email: {event['host_email']}", FONTS['medium']),
                (f"🍽  Servings Available: {event['serving_size']}", FONTS['medium']),
                (f"💰  Cost per head: ${event['cost_per_head']:.2f}", FONTS['medium_bold']),
                (f"⏱  Prep time: {event['preparation_time']} mins", FONTS['medium']),
            ]

            for text, font in details:
                ctk.CTkLabel(details_frame, 
                           text=text, 
                           font=font, 
                           text_color=COLORS['primary']).pack(anchor='w', pady=3)

            # Dish information
            ctk.CTkLabel(left_column, 
                        text=f"🍲  {event['dish_name']}", 
                        font=FONTS['medium_bold'], 
                        text_color=COLORS['primary']).pack(anchor='w', pady=(10, 5))
            ctk.CTkLabel(left_column, 
                        text=event['description'], 
                        font=FONTS['small'], 
                        text_color=COLORS['secondary'], 
                        wraplength=500).pack(anchor='w')

            # Booking controls
            controls_frame = ctk.CTkFrame(right_column, fg_color="transparent")
            controls_frame.pack(pady=20)

            if not is_past_event and not is_sold_out:
                btn = ctk.CTkButton(controls_frame, 
                                  text="Book Now", 
                                  width=140,
                                  height=40,
                                  command=lambda eid=event['event_id'], 
                                                seats=event['serving_size'], 
                                                f=controls_frame: 
                                                show_booking_form(eid, seats, f),
                                  fg_color=COLORS['accent'], 
                                  hover_color=COLORS['accent_dark'],
                                  text_color='white', 
                                  font=FONTS['medium_bold'],
                                  corner_radius=10)
                btn.pack(pady=10)
            elif is_sold_out:
                ctk.CTkLabel(controls_frame, 
                           text="SOLD OUT", 
                           font=FONTS['medium_bold'], 
                           text_color=COLORS['danger']).pack(pady=10)
            else:
                ctk.CTkLabel(controls_frame, 
                           text="EVENT ENDED", 
                           font=FONTS['medium_bold'], 
                           text_color=COLORS['disabled']).pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load events: {str(e)}")

def search_by_pincode():
    pincode = pincode_entry.get().strip()
    if pincode and not pincode.isdigit():
        messagebox.showerror("Error", "Pincode must be numeric")
        return
    load_events(pincode)

# ================== UI SETUP ==================
window = ctk.CTk()
window.title("Guest Dashboard")
window.geometry("1000x720")
window.configure(fg_color=COLORS['background'])

# Get user ID from command line
user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# ========== Main Layout Container ==========
main_frame = create_styled_frame(window)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Header
header_label = ctk.CTkLabel(
    main_frame,
    text="🍽 Guest Dashboard",
    font=FONTS['header'],
    text_color=COLORS['primary']
)
header_label.pack(pady=10)

# ========== Navigation Bar ==========
nav_frame = ctk.CTkFrame(main_frame, fg_color=COLORS['navbar'], corner_radius=10)
nav_frame.pack(fill='x', padx=10, pady=10)

# Nav Buttons
nav_buttons = [
    ("Profile", show_profile),
    ("Search Events", open_search_events),
    ("My Bookings", open_view_bookings),
    ("Feedback", open_feedback),
    ("Logout", logout),
]

for (label, action) in nav_buttons:
    ctk.CTkButton(
        nav_frame, 
        text=label,
        command=action,
        width=120,
        fg_color=COLORS['accent'],
        hover_color=COLORS['accent_dark'],
        text_color="white",
        font=FONTS['medium']
    ).pack(side='left', padx=10, pady=5)

# ========== Search Bar ==========
search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
search_frame.pack(fill='x', padx=10, pady=10)

ctk.CTkLabel(
    search_frame,
    text="Search by Pincode:",
    font=FONTS['medium'],
    text_color=COLORS['primary']
).pack(side='left', padx=10)

pincode_entry = ctk.CTkEntry(search_frame, width=150, font=FONTS['small'])
pincode_entry.pack(side='left', padx=5)

ctk.CTkButton(
    search_frame,
    text="Search",
    command=search_by_pincode,
    fg_color=COLORS['success'],
    hover_color=COLORS['success_dark'],
    text_color="white",
    font=FONTS['small']
).pack(side='left', padx=5)

# ========== Scrollable Content Frame ==========
content_container = ctk.CTkFrame(main_frame, fg_color="transparent")
content_container.pack(fill='both', expand=True, padx=10, pady=10)

canvas = ctk.CTkCanvas(content_container, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(content_container, command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color="transparent")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Initial load
load_events()

# Start the main event loop
window.mainloop()
# ----- End of search_events.py -----

# ----- Start of utils.py -----
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from PIL import Image, ImageTk
import customtkinter as ctk
import hashlib
import re
from config import DB_CONFIG
from constants import COLORS, STYLES

# Database Connection Pool
class DBAccess:
    pool = MySQLConnectionPool(
        pool_name=DB_CONFIG["pool_name"],
        pool_size=DB_CONFIG["pool_size"],
        **{k: v for k, v in DB_CONFIG.items() if k not in ["pool_name", "pool_size"]}
    )

    @staticmethod
    def execute_query(query, params=None):
        conn = DBAccess.pool.get_connection()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def execute_update(query, params=None):
        conn = DBAccess.pool.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        finally:
            conn.close()

# UI Utilities
def create_styled_frame(parent):
    """Create a consistently styled CTkFrame"""
    return ctk.CTkFrame(
        parent,
        fg_color=COLORS['background'],
        corner_radius=STYLES['corner_radius'],
        border_width=STYLES['border_width'],
        border_color=COLORS['accent']
    )

def resize_image(path, size):
    """Resize image while maintaining aspect ratio"""
    image = Image.open(path)
    image.thumbnail(size)
    return ImageTk.PhotoImage(image)

# Security Utilities
def hash_password(password):
    """Secure password hashing with SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_username(first_name, last_name):
    """Generate unique username from name components"""
    base = f"{first_name[0].lower()}{last_name.lower().replace(' ', '')}"
    username = base
    counter = 1
    
    while counter <= 100:
        if not DBAccess.execute_query(
            "SELECT username FROM users WHERE username = %s", 
            (username,)
        ):
            return username
        username = f"{base}{counter}"
        counter += 1
    
    raise ValueError("Could not generate unique username after 100 attempts")

# Validation Utilities
def validate_email(email):
    """RFC 5322 compliant email validation"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def validate_phone(phone):
    """International phone number validation"""
    pattern = r"^\+?[1-9]\d{1,14}$"  # E.164 format
    return re.match(pattern, phone)
# ----- End of utils.py -----

# ----- Start of view_bookings.py -----
import customtkinter as ctk
import sys
import subprocess
from tkinter import messagebox
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES
from datetime import datetime

# Command functions
def show_profile():
    subprocess.Popen(['python', 'host_dashboard.py', user_id])
    window.destroy()

def create_event():
    subprocess.Popen(['python', 'create_event.py', user_id])
    window.destroy()

def view_events():
    subprocess.Popen(['python', 'view_events.py', user_id])
    window.destroy()

def view_user_feedback():
    subprocess.Popen(['python', 'view_user_feedback.py', user_id])
    window.destroy()

def view_bookings():
    subprocess.Popen(['python', 'view_bookings.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# Window setup
window = ctk.CTk()
window.title("View Bookings")
window.geometry("1000x720")
window.configure(fg_color=COLORS['background'])

# Get user ID from command line
user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# Main container
main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Grid configuration
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=0)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="🎫 View Bookings",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, pady=20, sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color=COLORS['navbar'], corner_radius=10)
nav_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "white",
    'fg_color': COLORS['accent'],
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['accent_dark'],
    'width': 120
}

# Navigation buttons
ctk.CTkButton(nav_frame, text="My Profile", command=show_profile, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Create Event", command=create_event, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Events", command=view_events, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Feedback", command=view_user_feedback, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Bookings", command=view_bookings, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Logout", command=logout, **button_style).pack(side='left', padx=5)

# Content Frame
content_frame = ctk.CTkFrame(main_frame, fg_color=COLORS['card_background'])
content_frame.grid(row=2, column=0, sticky="nsew", pady=20, padx=20)

# Scrollable bookings area
canvas = ctk.CTkCanvas(content_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(content_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['card_background'])

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

try:
    # Fetch bookings with guest phone_number and email
    results = DBAccess.execute_query("""
        SELECT b.booking_id, b.number_of_attendees, b.paid_amount, b.booking_time, b.status,
               e.event_name, u.name AS guest_name, u.phone_number, u.email, e.event_datetime
        FROM bookings b
        JOIN events e ON b.event_id = e.event_id
        JOIN users u ON b.guest_id = u.user_id
        WHERE e.host_id = %s AND b.status = 'active'
    """, (user_id,))

    if not results:
        ctk.CTkLabel(scrollable_frame, text="😞 No active bookings available.",
                     font=FONTS['medium'], text_color=COLORS['primary']).pack(pady=40)
    else:
        for booking in results:
            # Stylish booking card with shadow effect
            card = ctk.CTkFrame(scrollable_frame, 
                              fg_color="#FFFFFF", 
                              corner_radius=15,
                              border_width=1,
                              border_color=COLORS['border'])
            card.pack(fill='x', pady=15, padx=20)

            # Status badge
            # Check if event_datetime is not None and handle it appropriately
            event_datetime = booking['event_datetime']
            if isinstance(event_datetime, datetime):
                is_past = event_datetime < datetime.now()
            else:
                is_past = datetime.strptime(event_datetime, "%Y-%m-%d %H:%M:%S") < datetime.now()

            status_color = COLORS['success'] if not is_past else COLORS['disabled']
            status_frame = ctk.CTkFrame(card, fg_color=status_color, corner_radius=8)
            status_frame.pack(anchor='ne', pady=5, padx=10)
            status_text = "✅ Confirmed" if not is_past else "⏳ Past Event"
            ctk.CTkLabel(status_frame, text=status_text,
                        font=FONTS['small_bold'], text_color="white").pack(padx=10, pady=2)

            # Content container with two-column layout
            content_frame = ctk.CTkFrame(card, fg_color="transparent")
            content_frame.pack(padx=15, pady=15, fill='both', expand=True)

            left_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            left_column.pack(side='left', fill='both', expand=True)

            right_column = ctk.CTkFrame(content_frame, fg_color="transparent")
            right_column.pack(side='right', padx=10)

            # Event and guest details
            ctk.CTkLabel(left_column, text=booking['event_name'].upper(),
                        font=FONTS['large_bold'], text_color=COLORS['primary']).pack(anchor='w', pady=(0, 10))

            details_frame = ctk.CTkFrame(left_column, fg_color="transparent")
            details_frame.pack(fill='x')

            details = [
                (f"🎉 Event: {booking['event_name']}", FONTS['medium']),
                (f"👤 Guest: {booking['guest_name']}", FONTS['medium']),
                (f"📞 Phone: {booking['phone_number']}", FONTS['medium']),
                (f"📧 Email: {booking['email']}", FONTS['medium']),
                (f"👥 Attendees: {booking['number_of_attendees']}", FONTS['medium']),
                (f"💰 Paid: ${booking['paid_amount']:.2f}", FONTS['medium_bold']),
                (f"📅 Booked on: {booking['booking_time'].strftime('%d %B %Y, %I:%M %p')}", FONTS['medium']),
            ]

            for text, font in details:
                ctk.CTkLabel(details_frame, text=text, font=font, text_color=COLORS['primary']).pack(anchor='w', pady=3)

            # Additional info or controls (placeholder for future expansion)
            if not is_past:
                ctk.CTkLabel(right_column, text="Active Booking",
                            font=FONTS['medium'], text_color=COLORS['success']).pack(pady=10)
            else:
                ctk.CTkLabel(right_column, text="Event Ended",
                            font=FONTS['medium'], text_color=COLORS['disabled']).pack(pady=10)

except Exception as e:
    messagebox.showerror("Database Error", f"Failed to load bookings: {str(e)}")

window.mainloop()
# ----- End of view_bookings.py -----

# ----- Start of view_events.py -----
import customtkinter as ctk
import subprocess
import sys
from tkinter import messagebox
from datetime import datetime
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# ================== NAVIGATION ==================
def show_profile():
    subprocess.Popen(['python', 'host_dashboard.py', host_id])
    window.destroy()

def create_event():
    subprocess.Popen(['python', 'create_event.py', host_id])
    window.destroy()

def view_events():
    pass  # Current page

def view_user_feedback():
    subprocess.Popen(['python', 'view_user_feedback.py', host_id])
    window.destroy()

def view_bookings():
    subprocess.Popen(['python', 'view_bookings.py', host_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# ================== EVENT MANAGEMENT ==================
def delete_event(event_id):
    if messagebox.askyesno("Confirm Delete", "Delete this event permanently?"):
        try:
            DBAccess.execute_update(
                "DELETE FROM events WHERE event_id = %s",
                (event_id,)
            )  
            messagebox.showinfo("Success", "Event deleted!")
            refresh_events()
        except Exception as e:
            messagebox.showerror("Error", f"Delete failed: {str(e)}")

def start_edit_mode(event_id, parent_frame):
    try:
        # Fetch event details
        events = DBAccess.execute_query(
            """
            SELECT event_id, event_name, address, pincode, 
                   event_datetime, serving_size, preparation_time, 
                   dish_name, description, cost_per_head 
            FROM events 
            WHERE event_id = %s
            """, 
            (event_id,)
        )

        if not events:
            messagebox.showerror("Error", "Event not found")
            return

        event = events[0]  # First result

        # Clear the parent frame
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # Create editable frame
        edit_frame = create_styled_frame(parent_frame)
        edit_frame.pack(fill='x', pady=10, padx=20, expand=True)

        # Input Variables
        name_var = ctk.StringVar(value=event['event_name'])
        address_var = ctk.StringVar(value=event['address'])
        pincode_var = ctk.StringVar(value=event['pincode'])
        datetime_var = ctk.StringVar(value=event['event_datetime'].strftime("%Y-%m-%d %H:%M"))
        serving_var = ctk.StringVar(value=str(event['serving_size']))
        prep_time_var = ctk.StringVar(value=str(event['preparation_time']))
        dishes_var = ctk.StringVar(value=event['dish_name'])
        desc_var = ctk.StringVar(value=event['description'])
        cost_var = ctk.StringVar(value=str(event['cost_per_head']))

        # Helper to create input fields
        def create_field(label, var):
            ctk.CTkLabel(edit_frame, text=label, font=FONTS['medium']).pack(anchor='w')
            entry = ctk.CTkEntry(edit_frame, textvariable=var)
            entry.pack(fill='x', pady=5)

        # Create all fields
        create_field("Event Name:", name_var)
        create_field("Address:", address_var)
        create_field("Pincode:", pincode_var)
        create_field("Date & Time (YYYY-MM-DD HH:MM):", datetime_var)
        create_field("Serving Size:", serving_var)
        create_field("Prep Time (mins):", prep_time_var)
        create_field("Dishes:", dishes_var)
        create_field("Description:", desc_var)
        create_field("Cost per Head ($):", cost_var)

        # Save button handler
        def save_changes():
            try:
                datetime_obj = datetime.strptime(datetime_var.get(), "%Y-%m-%d %H:%M")
                serving_size = int(serving_var.get())
                prep_time = int(prep_time_var.get())
                cost_per_head = float(cost_var.get())
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {str(e)}")
                return

            try:
                DBAccess.execute_update(
                    """
                    UPDATE events SET 
                        event_name = %s, 
                        address = %s, 
                        pincode = %s, 
                        event_datetime = %s, 
                        serving_size = %s, 
                        preparation_time = %s, 
                        dish_name = %s, 
                        description = %s,
                        cost_per_head = %s 
                    WHERE event_id = %s
                    """,
                    (
                        name_var.get(), address_var.get(), pincode_var.get(),
                        datetime_obj, serving_size, prep_time,
                        dishes_var.get(), desc_var.get(), cost_per_head, event_id
                    )
                )
                messagebox.showinfo("Success", "Event updated!")
                refresh_events()
            except Exception as e:
                messagebox.showerror("Error", f"Update failed: {str(e)}")

        # Cancel button handler
        def cancel_edit():
            refresh_events()

        # Action Buttons
        btn_frame = ctk.CTkFrame(edit_frame, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Save", command=save_changes, **STYLES['accent_button']).pack(side='left', padx=5)
        ctk.CTkButton(btn_frame, text="Cancel", command=cancel_edit, **STYLES['danger_button']).pack(side='left', padx=5)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

def refresh_events():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    load_events()

def load_events():
    try:
        events = DBAccess.execute_query(
            """SELECT event_id, event_name, address, pincode, 
                    event_datetime, serving_size, preparation_time, 
                    dish_name, description, image, cost_per_head 
             FROM events 
             WHERE host_id = %s 
             ORDER BY event_datetime DESC""",
            (host_id,))
        
        if not events:
            ctk.CTkLabel(scrollable_frame, text="No events found", 
                        font=FONTS['medium'], text_color=COLORS['primary']
                        ).pack(pady=20)
            return

        for event in events:
            # Event card frame with border and shadow effect
            event_frame = ctk.CTkFrame(scrollable_frame, fg_color="#FFFFFF", 
                                     corner_radius=10, border_width=2, border_color=COLORS['primary'])
            event_frame.pack(fill='x', pady=15, padx=20)

            event_id = event['event_id']
            name = event['event_name']
            address = event['address']
            pincode = event['pincode']
            db_datetime = event['event_datetime']
            serving = event['serving_size']
            prep_time = event['preparation_time']
            dishes = event['dish_name']
            desc = event['description']
            cost_per_head = event['cost_per_head']

            # Datetime handling
            if isinstance(db_datetime, str):
                datetime_obj = datetime.strptime(db_datetime, "%Y-%m-%d %H:%M:%S") if '.' not in db_datetime else datetime.strptime(db_datetime, "%Y-%m-%d %H:%M:%S.%f")
            else:
                datetime_obj = db_datetime
            formatted_dt = datetime_obj.strftime("%d %B %Y, %I:%M %p")

            # Inner content frame for padding
            content_frame = ctk.CTkFrame(event_frame, fg_color="transparent")
            content_frame.pack(padx=15, pady=15, fill='both', expand=True)

            # Grid layout for details
            content_frame.grid_columnconfigure(0, weight=0)
            content_frame.grid_columnconfigure(1, weight=1)
            content_frame.grid_columnconfigure(2, weight=0)

            # Event name (header)
            ctk.CTkLabel(content_frame, text=name.upper(), 
                        font=FONTS['large_bold'], text_color=COLORS['primary']).grid(
                            row=0, column=0, columnspan=2, sticky='w', pady=(0, 10))

            # Date and time
            ctk.CTkLabel(content_frame, text="🗓 Date:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=1, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=formatted_dt, 
                        font=FONTS['medium'], text_color=COLORS['primary']).grid(
                            row=1, column=1, sticky='w')

            # Location
            ctk.CTkLabel(content_frame, text="📍 Location:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=2, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=f"{address}, {pincode}", 
                        font=FONTS['medium'], text_color=COLORS['primary']).grid(
                            row=2, column=1, sticky='w')

            # Serving size and prep time
            ctk.CTkLabel(content_frame, text="🍽 Serving:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=3, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=f"{serving} people", 
                        font=FONTS['medium'], text_color=COLORS['primary']).grid(
                            row=3, column=1, sticky='w')
            ctk.CTkLabel(content_frame, text="⏱ Prep Time:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=4, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=f"{prep_time} mins", 
                        font=FONTS['medium'], text_color=COLORS['primary']).grid(
                            row=4, column=1, sticky='w')

            # Dishes
            ctk.CTkLabel(content_frame, text="🍲 Dishes:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=5, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=dishes, 
                        font=FONTS['medium'], text_color=COLORS['primary'], wraplength=500).grid(
                            row=5, column=1, sticky='w')

            # Cost per head
            ctk.CTkLabel(content_frame, text="💰 Cost:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=6, column=0, sticky='w', padx=(0, 10))
            ctk.CTkLabel(content_frame, text=f"${cost_per_head}/head", 
                        font=FONTS['medium'], text_color=COLORS['primary']).grid(
                            row=6, column=1, sticky='w')

            # Description
            ctk.CTkLabel(content_frame, text="📝 Description:", 
                        font=FONTS['medium_bold'], text_color=COLORS['secondary']).grid(
                            row=7, column=0, sticky='nw', padx=(0, 10), pady=(10, 0))
            ctk.CTkLabel(content_frame, text=desc, 
                        font=FONTS['medium'], text_color=COLORS['primary'], wraplength=500).grid(
                            row=7, column=1, sticky='w', pady=(10, 0))

            # Action buttons
            btn_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
            btn_frame.grid(row=0, column=2, rowspan=8, sticky='ne')

            ctk.CTkButton(btn_frame, text="Edit", width=100,
                         command=lambda eid=event_id, frame=event_frame: start_edit_mode(eid, frame),
                         **STYLES['accent_button']).pack(pady=5)
            ctk.CTkButton(btn_frame, text="Delete", width=100,
                         command=lambda eid=event_id: delete_event(eid),
                         **STYLES['danger_button']).pack(pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Load failed: {str(e)}")

# ================== MAIN WINDOW ==================
window = ctk.CTk()
window.title("My Events")
window.geometry("1200x900")
window.configure(fg_color=COLORS['background'])

host_id = sys.argv[1] if len(sys.argv) > 1 else None
if not host_id:
    messagebox.showerror("Error", "Host ID missing")
    sys.exit(1)

# UI Components
main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Navigation Bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.pack(pady=10)

nav_buttons = [
    ("My Profile", show_profile),
    ("Create Event", create_event),
    ("View Events", view_events),
    ("View Feedback", view_user_feedback),
    ("View Bookings", view_bookings),
    ("Logout", logout)
]

for text, cmd in nav_buttons:
    ctk.CTkButton(
        nav_frame,
        text=text,
        command=cmd,
        font=FONTS['medium'],
        text_color="white",
        fg_color=COLORS['accent'],
        border_color=COLORS['primary'],
        border_width=1,
        hover_color=COLORS['accent_dark'],
        width=120
    ).pack(side='left', padx=5)


# Scrollable Area
canvas = ctk.CTkCanvas(main_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['background'])

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

load_events()
window.mainloop()
# ----- End of view_events.py -----

# ----- Start of view_user_feedback.py -----
import customtkinter as ctk
import sys
import subprocess
from tkinter import messagebox
from utils import create_styled_frame, DBAccess
from constants import COLORS, FONTS, STYLES

# Command functions
def show_profile():
    subprocess.Popen(['python', 'host_dashboard.py', user_id])
    window.destroy()

def create_event():
    subprocess.Popen(['python', 'create_event.py', user_id])
    window.destroy()

def view_events():
    subprocess.Popen(['python', 'view_events.py', user_id])
    window.destroy()

def view_user_feedback():
    subprocess.Popen(['python', 'view_user_feedback.py', user_id])
    window.destroy()

def view_bookings():
    subprocess.Popen(['python', 'view_bookings.py', user_id])
    window.destroy()

def logout():
    subprocess.Popen(['python', 'login.py'])
    window.destroy()

# Window setup
window = ctk.CTk()
window.title("View User Feedback")
window.geometry("800x600")
window.configure(fg_color=COLORS['background'])

# Get user ID from command line
user_id = sys.argv[1] if len(sys.argv) > 1 else None
if not user_id:
    messagebox.showerror("Error", "User ID missing")
    sys.exit(1)

# Main container
main_frame = create_styled_frame(window)
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Grid configuration
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=0)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Header
ctk.CTkLabel(
    main_frame,
    text="View User Feedback",
    font=FONTS['title'],
    text_color=COLORS['primary']
).grid(row=0, column=0, pady=20, sticky="nsew")

# Navigation bar
nav_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
nav_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

button_style = {
    'font': FONTS['medium'],
    'text_color': "white",
    'fg_color': COLORS['accent'],
    'border_color': COLORS['primary'],
    'border_width': 1,
    'hover_color': COLORS['accent_dark'],
    'width': 120
}

# Navigation buttons
ctk.CTkButton(nav_frame, text="My Profile", command=show_profile, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Create Event", command=create_event, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Events", command=view_events, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Feedback", command=view_user_feedback, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="View Bookings", command=view_bookings, **button_style).pack(side='left', padx=5)
ctk.CTkButton(nav_frame, text="Logout", command=logout, **button_style).pack(side='left', padx=5)

# Content Frame
content_frame = ctk.CTkFrame(main_frame, fg_color="#e8f1e4")
content_frame.grid(row=2, column=0, sticky="nsew", pady=20)

# Scrollable feedback area
canvas = ctk.CTkCanvas(content_frame, bg=COLORS['background'], highlightthickness=0)
scrollbar = ctk.CTkScrollbar(content_frame, orientation="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, fg_color=COLORS['background'])

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

try:
    # Fetch feedback for events hosted by the user
    results = DBAccess.execute_query("""
        SELECT f.feedback_id, f.rating, f.review, e.event_name, u.name AS guest_name
        FROM feedback f
        JOIN events e ON f.event_id = e.event_id
        JOIN users u ON f.guest_id = u.user_id
        WHERE e.host_id = %s
    """, (user_id,))

    if not results:
        ctk.CTkLabel(scrollable_frame, text="😞 No feedback available.", font=FONTS['medium'], text_color=COLORS['primary']).pack(pady=20)
    else:
        for feedback in results:
            # Stylish feedback card
            card = ctk.CTkFrame(scrollable_frame, fg_color="#ffffff", corner_radius=10, border_width=1, border_color=COLORS['primary'])
            card.pack(fill='x', pady=10, padx=20)  # Corrected by removing duplicate padx

            # Rating badge
            rating_color = COLORS['success'] if feedback['rating'] >= 4 else COLORS['warning'] if feedback['rating'] >= 3 else COLORS['danger']
            rating_frame = ctk.CTkFrame(card, fg_color=rating_color, corner_radius=8)
            rating_frame.pack(anchor='ne', pady=5, padx=10)
            ctk.CTkLabel(rating_frame, text=f"⭐ {feedback['rating']}/5", font=FONTS['small_bold'], text_color="white").pack(padx=10, pady=2)

            # Content
            content_frame = ctk.CTkFrame(card, fg_color="transparent")
            content_frame.pack(padx=15, pady=10, fill='both')

            ctk.CTkLabel(content_frame, text=f"🎉 Event: {feedback['event_name']}", font=FONTS['medium_bold'], text_color=COLORS['primary']).pack(anchor='w', pady=2)
            ctk.CTkLabel(content_frame, text=f"👤 Guest: {feedback['guest_name']}", font=FONTS['medium'], text_color=COLORS['primary']).pack(anchor='w', pady=2)
            ctk.CTkLabel(content_frame, text=f"💬 Review: {feedback['review'] or 'No review provided'}", font=FONTS['medium'], text_color=COLORS['primary'], wraplength=600).pack(anchor='w', pady=2)

except Exception as e:
    messagebox.showerror("Database Error", f"Failed to load feedback: {str(e)}")

window.mainloop()
# ----- End of view_user_feedback.py -----

