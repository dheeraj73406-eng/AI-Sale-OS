with open('backend/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"platform":', '"channel":')
content = content.replace('item.pop("is_ai_managed")', 'item.pop("is_ai_managed")\n        channel = item.pop("channel", "Website")')
content = content.replace('customer_id=cust.id,', 'customer_id=cust.id,\n            channel=channel,')
content = content.replace('c.platform or', 'c.conversations[0].channel if c.conversations else')
content = content.replace('"platforms": platforms', '"channels": platforms')

with open('backend/main.py', 'w', encoding='utf-8') as f:
    f.write(content)
