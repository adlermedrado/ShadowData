from shadow_data.anonymization import TextProcessor, Ipv4Anonymization

original_content = "Little John likes to play with the staff."
anonymized_content = TextProcessor.replace_text("Little John", "XXXXXX XXXX", original_content)
print(f"Original content: {original_content} | Anonymized content: {anonymized_content}")

original_ip = '200.189.45.128'
anonymized_content = Ipv4Anonymization.anonymize_ipv4(original_ip)
print(f"Original IP: {original_ip} | Anonymized IP: {anonymized_content}")
