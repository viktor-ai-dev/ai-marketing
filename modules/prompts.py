
def marketing_prompt(product,category,features):
    return f"""
    You are an expert in e-commerce marketing strategist.
    Create a FULL marketing campaign for this product.

    Product: {product}
    Category: {category}
    Features: {features}

    Include:

    1. Product Description
    2. Facebook Ad Copy
    3. TikTok Ad Script
    4. Email Campaign

    Make everything high-converting.

    
    Return output in this format:

    ## Product Description
    ...

    ## Facebook Ad
    ...

    ## TikTok Script
    ...

    ## Email Campaign
    ...
    
    """