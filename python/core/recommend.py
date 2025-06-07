from core.database import read_products

def recommend_products(skin_sensitivity=None, skin_type=None, category=None):
    all_products = read_products()
    recommendations = []

    for product in all_products:
        product_skin_types = product.get("skin_type", [])
        product_skin_types = [s.strip().lower() for s in product_skin_types if isinstance(s, str)]

        sensitivity_match = skin_sensitivity.lower() in product_skin_types if skin_sensitivity else True
        type_match = skin_type.lower() in product_skin_types if skin_type else True

        if category and category.lower() != "all":
            category_match = product.get("category", "").lower() == category.lower()
        else:
            category_match = True

        if sensitivity_match and type_match and category_match:
            recommendations.append(product)

    return recommendations
