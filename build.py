import subprocess
import os

env = os.environ.copy()
env['JAVA_HOME'] = r'C:\Program Files\Android\Android Studio\jbr'
cwd = r'D:\Vibe Code\Android Firewall & VPN'
cmd = [
    r'C:\Program Files\Android\Android Studio\jbr\bin\java.exe',
    '-classpath',
    r'D:\Vibe Code\Android Firewall & VPN\gradle\wrapper\gradle-wrapper.jar',
    'org.gradle.wrapper.GradleWrapperMain',
    'clean',
    'assembleDebug'
]

try:
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    with open(r'D:\Vibe Code\Android Firewall & VPN\build_out.txt', 'w') as f:
        f.write(result.stdout)
        f.write(result.stderr)
    print("Done")
except Exception as e:
    print(e)
