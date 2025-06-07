# 💄 SmartBeauty – AI-Powered Skincare Recommendation App

SmartBeauty is a personalized skincare recommendation system that suggests products based on your skin type, skin conditions, and time of use.  
This project provides a desktop-based GUI interface to help users discover suitable skincare products using structured filters.

## 🧠 Features

- 🌿 Skin Type-Based Filtering (Dry, Oily, Combination, Sensitive)
- 🕒 Time-of-Use Selection (Day, Night, Eye, All-day)
- 📂 Category Browsing (Moisturizer, Serum, Cleanser, Mask, etc.)
- 📄 Product Detail View: Brand, Description, Purpose, Volume, Price, URL
- 📦 Local JSON-based product database
- 🎯 Designed for personal care and product exploration

## 🚀 Technologies Used

- Python 3.11+
- Tkinter (GUI framework)
- JSON (for data storage)
- Custom GUI design (fonts, layout, button styling)
- No external image libraries used

## 🗃️ Project Structure

```
smartbeauty/
├── main.py                  # Main GUI application
├── products.json            # Structured product database
├── selection_page.py        # Skin type & category selection logic
├── add_product.py           # Interface for adding new products
├── product_filter.py        # Filtering and recommendation backend
├── database_utils.py        # Data loading and JSON parsing
├── utils.py                 # Helper functions
└── README.md                # This file
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/fatmakyldz/SmartBeauty.git
cd SmartBeauty
```

2. Run the main application:

```bash
python main.py
```

> Make sure you are using Python 3.11 or above.

## 📌 Sample Product JSON Format

```json
{
  "name": "Hydrating Night Cream",
  "brand": "BrandX",
  "type": "Moisturizer",
  "skin_type": ["Dry", "Sensitive"],
  "usage_time": "Night",
  "purpose": "Deep hydration and repair",
  "volume_ml": 50,
  "price": 299.99,
  "link": "https://example.com/product/12345"
}
```

## 👩‍💻 Author

**Fatma Akyıldız**  
Final-year Software Engineering student | Data Science & AI Enthusiast  
[GitHub](https://github.com/fatmakyldz) | [LinkedIn](https://www.linkedin.com/in/fatma-akyıldız)

## 📜 License

This project is open-source for personal and academic use.  
Commercial redistribution is not permitted without written permission.
