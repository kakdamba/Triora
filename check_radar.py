with open(r'D:\Vibe Code\Android Firewall & VPN\app\src\main\java\com\vibe\privacy\data\TrackerRadar.kt') as f:
    text = f.read()
    print("GA count:", text.count('name = "Google Analytics"'))
    print("FB count:", text.count('name = "Facebook SDK"'))
