
from src.utils.logger import logger

logger.info("Customer support agent triggered")

def customer_support_agent(query):
    if "refund" in query.lower():
        return "Redirecting to refund department"
    
    if "price" in query.lower():
        return "Sharing pricing details"

    return "Escalating to human agent"