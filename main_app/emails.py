from django.conf import settings
from django.core.mail import send_mail
import logging
import ast

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs.log"),
    ])

def send_result_mail(data,subject,receiver):
    logger = logging.getLogger("send_result_mail")
    message = "Hi {} \n\nYour SkillPulse results are as follows:\n\n".format(receiver)
    ratings = data[subject]

# Markdown table header
    markdown_table = ""

    # Populate the table rows
    for question_number, question_data in ratings.items():
        markdown_table += f"----------\nquestion number: {question_number} \n rating:{question_data['rating']} \n Strong Topics:{', '.join(ast.literal_eval(question_data['Strength']))} \n Need to improve:{', '.join(ast.literal_eval(question_data['Weak']))} \n Suggestion:{question_data['Suggestion']} |\n----------\n"

    # Markdown table for final scores
    final_scores = data["final_score"]
    markdown_table += "\nFinal Scores:\n"
    for key, value in final_scores.items():
        markdown_table += f"- {key}: {value}\n"

    # Print or use markdown_table in your email sending code
    print(markdown_table)

    markdown_table += "\n\nThank you for using SkillPulse."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [receiver,]
    send_mail( subject, markdown_table, email_from, recipient_list)
    logger.info("Mail sent to {}".format(receiver))

def print_res():

    data = {
    "cnEntryTest": {
      "1": {
        "rating": "10",
        "Strength": "['DNS', 'Domain Name System', 'IP addresses', 'browsing', 'caching', 'load balancing', 'address resolution']",
        "Weak": "['human-readable domain names']",
        "Suggestion": "to further enhance your knowledge in DNS and its functioning, you could explore topics such as DNS servers, DNS records (such as A, CNAME, MX, etc.), DNS caching mechanisms, and DNS security practices."
      },
      "2": {
        "rating": "10",
        "Strength": "['firewall', 'network security device', 'software', 'trusted internal network', 'untrusted external networks', 'monitoring', 'filtering', 'controlling network traffic', 'security rules']",
        "Weak": "[]",
        "Suggestion": "to expand your knowledge in firewalls and network security, you could explore topics such as firewall architectures (e.g., packet-filtering, stateful inspection, proxy firewalls), intrusion detection and prevention systems (IDS/IPS), virtual private networks (VPNs), and network security best practices."
      },
      "3": {
        "rating": "10",
        "Strength": "['internet', 'web', 'global network of computers', 'accessing information', 'web pages', 'websites']",
        "Weak": "[]",
        "Suggestion": "to deepen your understanding of the internet and the web, you could explore topics such as network protocols (e.g., TCP/IP, HTTP, FTP), TCP/IP addressing and subnetting, website development (HTML, CSS, JavaScript), and emerging technologies shaping the future of the internet (e.g., IPv6, IoT, cloud computing)."
      },
      "4": {
        "rating": "10",
        "Strength": "['network topology', 'physical arrangement', 'logical arrangement', 'network devices', 'star topology', 'central hub', 'switch']",
        "Weak": "[]",
        "Suggestion": "to further broaden your knowledge in network topology and network design, you could explore topics such as other commonly used topologies (e.g., bus, ring, mesh), network protocols (e.g., Ethernet, Wi-Fi, TCP/IP), network performance optimization techniques, and network troubleshooting methodologies."
      },
      "5": {
        "rating": "10",
        "Strength": "['proxy server', 'intermediate server', 'client device', 'destination server', 'anonymity', 'privacy', 'gateway', 'forwarding requests']",
        "Weak": "[]",
        "Suggestion": "to enhance your understanding of proxy servers and their applications, you could explore topics such as different types of proxy servers (e.g., forward proxy, reverse proxy), proxy server configurations and deployment scenarios, proxy server security considerations, and emerging trends in proxy technologies (e.g., SSL/TLS interception, content filtering)."
      },
      "6": {
        "rating": "10",
        "Strength": "['routers', 'switch', 'communication', 'same network']",
        "Weak": "[]",
        "Suggestion": "if you want to further improve your understanding of routers and switches, you could explore topics such as routing protocols (e.g., OSPF, BGP), VLANs and network segmentation, router and switch configuration (e.g., CLI, GUI), and network troubleshooting techniques related to routers and switches."
      },
      "7": {
        "rating": "10",
        "Strength": "['peer-to-peer', 'networking model', 'client', 'server', 'BitTorrent', 'P2P file-sharing system', 'direct file sharing']",
        "Weak": "[]",
        "Suggestion": "to broaden your knowledge in peer-to-peer networks and file-sharing technologies, you could explore topics such as distributed hash tables (DHT), peer discovery mechanisms, peer-to-peer overlay networks, and legal/ethical considerations surrounding P2P file sharing."
      },
      "8": {
        "rating": "10",
        "Strength": "['load balancing', 'traffic distribution', 'performance', 'reliability', 'incoming requests', 'server resources']",
        "Weak": "[]",
        "Suggestion": "to expand your knowledge in load balancing and its role in network architecture, you could explore topics such as load balancing algorithms (e.g., round-robin, least connections), session persistence mechanisms, load balancing across data centers, and scalable load balancing solutions in cloud environments."
      },
      "9": {
        "rating": "10",
        "Strength": "['data sharing', 'systems', 'web', 'peer-to-peer file sharing', 'direct file transfers', 'shared network file access']",
        "Weak": "[]",
        "Suggestion": "to enhance your understanding of data sharing approaches beyond the web, you could explore topics such as distributed file systems (e.g., NFS, DFS), cloud storage and synchronization services, secure file sharing protocols, and data sharing methodologies in hybrid network environments."
      }
    },
    "final_score": {
      "Introduction and Physical layer": 99,
      "Data link layer and LAN": 99,
      "Network and Routing": 99,
      "Transport layer": 33,
      "Application layer": 0,
      "totalMarks": 6.6
    }
  }
  
    ratings = data["cnEntryTest"]

# Markdown table header
    markdown_table = "| Question | Rating | Strengths | Weaknesses | Suggestions |\n"
    markdown_table += "|----------|--------|-----------|------------|-------------|\n"

    # Populate the table rows
    for question_number, question_data in ratings.items():
        markdown_table += f"| {question_number} | {question_data['rating']} | {', '.join(ast.literal_eval(question_data['Strength']))} | {', '.join(ast.literal_eval(question_data['Weak']))} | {question_data['Suggestion']} |\n"

    # Markdown table for final scores
    final_scores = data["final_score"]
    markdown_table += "\nFinal Scores:\n"
    for key, value in final_scores.items():
        markdown_table += f"- {key}: {value}\n"

    # Print or use markdown_table in your email sending code
    print(markdown_table)
