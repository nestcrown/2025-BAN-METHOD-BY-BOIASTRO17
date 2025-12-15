import os
import time
import smtplib
import ssl
from email.message import EmailMessage
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Initialize colorama and dotenv
init(autoreset=True)
load_dotenv()

perm_file = "perm_ban.txt"
temp_file = "temp_ban.txt"

sender_email = os.getenv('GMAIL_ADDRESS')
password = os.getenv('GMAIL_PASSWORD')

support_emails = [
    "support@whatsapp.com",
    "abuse@support.whatsapp.com",
    "privacy@support.whatsapp.com",
    "terms@support.whatsapp.com",
    "accessibility@support.whatsapp.com"
]


def banner():
    # Use ANSI color codes directly (Termux supports these natively)
    print("\033[31m\n===[ MR DEV — SHADOW BAN CORE ]===\033[0m")
    print("""
\033[91m
|===ALL======-
|===CREDITS======|     CYPHERLORD     CYBER-X
|      ===|
|===TO======|     BOI ASTRO17    LEOSVG
|      ===|    
|===:======|     PAIN           LIVEWARE
|===😉======-                            

         ☠️  BOI ASTRO17 — LORD OF CYBER THREATS ☠️
             ⚔️  Silent. Swift. Fatal. ⚔️

         "The system has no mercy for the wicked..."
\033[0m
""")

def is_banned(number):
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            if number in f.read():
                return "permanent"
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                if line.startswith(number + ","):
                    unban_time = int(line.strip().split(",")[1])
                    if time.time() < unban_time:
                        return "temporary"
    return None

def simulate_reports(number, total):
    # mr dev is the best....
    print(f"\n{Fore.LIGHTBLACK_EX}🍷 {Fore.RED} target launched — Queued:{Fore.WHITE} {total} {Fore.RED}vectors for {Fore.WHITE}{number}")
    time.sleep(0.35)
    for i in range(1, total + 1):
        print(f"{Fore.RED}☠️  [{i:03d}/{total}]  Emitting dark packet → {Fore.WHITE}{number}")
        time.sleep(0.05)
    print(f"\n{Fore.GREEN}✅  Operation complete. {Fore.WHITE}{total} vectors deployed on {number}.")
    print(f"{Fore.LIGHTBLACK_EX}— Crafted & executed by BOI ASTRO 17 🕷️{Style.RESET_ALL}")
def save_perm_ban(number):
    with open(perm_file, "a") as f:
        f.write(number + "\n")

def save_temp_ban(number, duration):
    unban_time = int(time.time() + duration)
    with open(temp_file, "a") as f:
        f.write(f"{number},{unban_time}\n")

def check_temp_expiry():
    if not os.path.exists(temp_file):
        return
    with open(temp_file, "r") as f:
        lines = f.readlines()

    active = []
    for line in lines:
        try:
            number, unban_time = line.strip().split(",")
        except ValueError:
            continue
        if time.time() < int(unban_time):
            active.append(line)
        else:
            print(f"{Fore.RED}🍷  PAY BACK TYM — {Fore.WHITE}{number} {Fore.LIGHTBLACK_EX}has returned from the void...")

    with open(temp_file, "w") as f:
        f.writelines(active)

    print(f"{Fore.LIGHTBLACK_EX}— Orchestrated by BOI ASTRO17 ⚔️{Style.RESET_ALL}")

def ban_permanent():
    number = input(f"{Fore.RED}🫴  Enter target to be eliminated 🔥 {Fore.WHITE}: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}😉  {number} still under attack ({is_banned(number)} ban active).")
        return

    confirm = input(f"{Fore.LIGHTRED_EX}⚠️  Once marked, the soul cannot return. Proceed with eternal ban on {number}? (y/n): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}🕯️  Ritual aborted — the void remains silent.")
        return

    try:
        reports = int(input(f"{Fore.MAGENTA}🔢  Input the number of THREATS strikes to deploy: {Fore.WHITE}"))
    except ValueError:
        print(f"{Fore.RED}❌  Invalid symbol. Only numbers of pain accepted.")
        return

    simulate_reports(number, reports)
    save_perm_ban(number)

    print(f"\n{Fore.RED}😉  The number {number} has been cast into eternal oblivion.")
    print(f"{Fore.LIGHTBLACK_EX}🍷  Whisper sent to the BOIASTRO SERVER… awaiting confirmation.")

    # mr dev is the best lol.....
    reason = "This Number Have Been Stealing and scamming People On WhatsApp, destroying people WhatsApp account, sending negative Text, spamming virus, Sending nudes to different people on WhatsApp please He his Going against the Community guidelines please disable the account from using WhatsApp He hacked My Number and start using it to scam people Online And he his very dangerous Sending Different videos and pictures especially Nudes or sex stuff, please i beg of you WhatsApp support team work together and disable this number from Violating WhatsApp please, He is a Fraud, scammer,Thief, Sending spam messages, text viruses, And many of all negative attitude Please disable the account permanently from using WhatsApp account again he will continue doing so if you guy's didn't take action on time. Thank you"


    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}🕷️  Execution completed. Power channeled by {Fore.RED}BOI ASTRO17 — The LORD OF CYBER THREARS!!!.")

def ban_temporary():
    #  prompt
    number = input("💀 Enter the Shadow Target Number 🎯: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}☠️  {number} is already marked in the dark registry.")
        return

    confirm = input(f"⚠️  Do you wish to unleash temporary lockdown on {number}? (Y/N): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}❌  Operation aborted. Target remains active in the shadows.")
        return

    try:
        minutes = int(input("⏳ Enter Ban Duration in minutes (how long the darkness lasts): "))
        reports = int(input("🔢 Enter number of shadow strikes to deploy: "))
    except ValueError:
        print(f"{Fore.RED}❌  Invalid input. Only numbers for the ritual.")
        return

    # effect 
    print(f"\n{Fore.LIGHTBLACK_EX}{'─'*60}")
    print(f"{Fore.MAGENTA}☠️  Initiating shadow protocol — Target: {Fore.WHITE}{number} {Fore.MAGENTA}· Duration: {minutes}m · Strikes: {reports}")
    print(f"{Fore.LIGHTBLACK_EX}{'─'*60}\n")

    simulate_reports(number, reports)
    save_temp_ban(number, minutes * 60)

    # Success style 
    print(f"\n{Fore.RED}🍷  {Fore.WHITE}{number} has been cloaked in torture chamber for {minutes} minutes.")
    print(f"{Fore.GREEN}✔️  Shadow registry updated successfully.")
    print(f"{Fore.LIGHTBLACK_EX}— Operation executed by MR DEV (Shadow Ban Tool) 🕷️\n")

    # mr dev is the best
    reason = f"This Number will be disabled for some {minutes} minutes because he has been stealing and scamming people on WhatsApp, destroying people's WhatsApp accounts, sending negative texts, spamming viruses, and sending nudes to different people on WhatsApp. He is going against the community guidelines — please disable the account. He hacked my number and started using it to scam people online, and he is very dangerous, sending inappropriate videos and pictures. I beg the WhatsApp support team to work together and disable this number for violating WhatsApp's rules. He is a fraud, scammer, thief, and spammer. Please disable the account permanently before he continues doing so. Thank you."

    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}🕷️  Execution completed. Power channeled by {Fore.RED}MR DEV — The Architect of Shadows.")

def unban_permanent():
    number = input(f"{Fore.RED}🍷 Enter number to unban from PERMANENT ban: ").strip()
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            lines = f.readlines()
        with open(perm_file, "w") as f:
            for line in lines:
                if line.strip() != number:
                    f.write(line)
        print(f"{Fore.MAGENTA}💀 {number} has been freed from eternal darkness.")
    else:
        print(f"{Fore.YELLOW}⚠️ No permanent ban records found.")

def unban_temporary():
    number = input(f"{Fore.RED}🍷 CYPHERORD whispers: 𝗳𝗿𝗼𝗺 TEMP ban , 𝗰𝗹𝗮𝗶𝗺 𝘁𝗵𝗲 𝗰𝗵𝗮𝗼𝘁𝗶𝗰 𝗻𝘂𝗺𝗯𝗲𝗿: ").strip()

    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            lines = f.readlines()
        # mr dev is the best
        new_lines = [line for line in lines if not line.startswith(number + ",")]
        with open(temp_file, "w") as f:
            f.writelines(new_lines)
        print(f"{Fore.MAGENTA}💀 {number} 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗶𝗽𝗽𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗽𝗮𝗶𝗻!")
    else:
        print(f"{Fore.YELLOW}⚠️ 𝗡𝗼 𝗲𝘁𝗵𝗲𝗿𝗲𝗮𝗹 𝗹𝗶𝘀𝘁 𝗳𝗼𝘂𝗻𝗱. 𝗡𝘂𝗺𝗯𝗲𝗿 {number} 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱.")

def send_report_email(target_number, reason, count):
    context = ssl.create_default_context()
    for i in range(count):
        msg = EmailMessage()
        msg['Subject'] = f"Report of WhatsApp Account (Attempt {i+1})"
        msg['From'] = sender_email
        msg['To'] = ", ".join(support_emails)
        msg.set_content(f"""Hello WhatsApp Support,

I would like to report the following WhatsApp number:

📱 Number: {target_number}
📝 Reason: {reason}

please take action immediately 
Thank you.
""")
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)
            print(f"✅ 𝗕𝗮𝗻 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 {i+1}/{count} 𝘀𝗲𝗻𝘁 𝘁𝗼 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽")
        except Exception as e:
            print(f"❌ 𝗕𝗮𝗻 𝗳𝗮𝗶𝗹𝗲𝗱 {i+1} 𝗳𝗮𝗶𝗹𝗲𝗱: {e}")
            break

def view_banned():
    print(f"\n{Fore.RED}🚫 𝗣𝗘𝗥𝗠𝗔𝗡𝗘𝗡𝗧 𝗕𝗔𝗡𝗦:")
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            print(f.read().strip() or "None")
    else:
        print("𝗡𝗼𝗻𝗲")

    print(f"\n{Fore.MAGENTA}⏳ 𝗧𝗘𝗠𝗣𝗢𝗥𝗔𝗥𝗬 𝗕𝗔𝗡𝗦:")
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                number, unban_time = line.strip().split(",")
                remaining = int(unban_time) - int(time.time())
                if remaining > 0:
                    mins = remaining // 60
                    print(f"{number} — {mins} min left")
    else:
        print("𝗡𝗼𝗻𝗲")

# BOI ASTRO17 is the best take am play first
while True:
    check_temp_expiry()
    banner()

    print(f"{Fore.RED}{'═'*70}")
    print(f"{Fore.LIGHTBLACK_EX}🍷 {Fore.RED}   D E V   –   C Y P H E R L O R D  🤞")
    print(f"{Fore.RED}{'═'*70}")
    print(f"{Fore.LIGHTBLACK_EX}💻  Access Level: {Fore.RED}ROOT ADMIN     {Fore.LIGHTBLACK_EX}│  Status: {Fore.RED}ONLINE ⚡")
    print(f"{Fore.RED}{'─'*70}\n")

    print(f"{Fore.RED}1️⃣   💀  PERMANENT BAN        {Fore.LIGHTBLACK_EX}:: Erase target permanently")
    print(f"{Fore.RED}2️⃣   🔥  TEMPORARY BAN        {Fore.LIGHTBLACK_EX}:: Lock target temporarily")
    print(f"{Fore.LIGHTBLACK_EX}3️⃣   🧹  REMOVE PERM BAN      {Fore.LIGHTBLACK_EX}:: Reverse eternal restriction")
    print(f"{Fore.LIGHTBLACK_EX}4️⃣   🕒  REMOVE TEMP BAN      {Fore.LIGHTBLACK_EX}:: Restore temporary subject")
    print(f"{Fore.WHITE}5️⃣   👁️   VIEW BAN RECORDS     {Fore.LIGHTBLACK_EX}:: Access encrypted logs")
    print(f"{Fore.LIGHTBLACK_EX}6️⃣   🚪  EXIT CONSOLE         {Fore.LIGHTBLACK_EX}:: Shutdown operation\n")

    print(f"{Fore.RED}{'─'*70}")
    choice = input(f"{Fore.RED}🕷️  INPUT COMMAND [1–6]: {Fore.WHITE}").strip()
    print(f"{Fore.RED}{'─'*70}\n")

    if choice == "1":
        print(f"{Fore.RED}💣  Deploying PERMANENT ban protocol...\n")
        time.sleep(0.6)
        ban_permanent()

    elif choice == "2":
        print(f"{Fore.RED}⏳  Activating TEMPORARY restriction module...\n")
        time.sleep(0.6)
        ban_temporary()

    elif choice == "3":
        print(f"{Fore.LIGHTBLACK_EX}🔓  Releasing PERMANENT lockdown...\n")
        time.sleep(0.6)
        unban_permanent()

    elif choice == "4":
        print(f"{Fore.LIGHTBLACK_EX}🕒  Lifting TEMPORARY isolation...\n")
        time.sleep(0.6)
        unban_temporary()

    elif choice == "5":
        print(f"{Fore.WHITE}📜  Scanning ban registry archives...\n")
        time.sleep(0.6)
        view_banned()

    elif choice == "6":
        print(f"{Fore.RED}\n🍷  SYSTEM OVERRIDE INITIATED...")
        time.sleep(1)
        print(f"{Fore.LIGHTBLACK_EX}💀  Closing all secure channels...")
        time.sleep(1)
        print(f"{Fore.RED}⚡  CORE OFFLINE. Until next hunt, Mr Dev.\n")
        print(f"{Fore.LIGHTBLACK_EX}{'═'*70}")
        break

    else:
        print(f"{Fore.RED}❌  Invalid command detected. Try again, Operator.\n")

    time.sleep(1.4) 