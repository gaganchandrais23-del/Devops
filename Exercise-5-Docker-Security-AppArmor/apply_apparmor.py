from pathlib import Path
import subprocess

profile = Path("my-apparmor-profile")

if not profile.is_file():
    raise SystemExit("ERROR: my-apparmor-profile was not found.")

enabled_path = Path("/sys/module/apparmor/parameters/enabled")
filesystem_path = Path("/sys/kernel/security/apparmor")

enabled = enabled_path.read_text().strip() if enabled_path.exists() else "N"

print(f"AppArmor kernel parameter: {enabled}")
print(f"AppArmor filesystem available: {filesystem_path.exists()}")

if enabled != "Y" or not filesystem_path.exists():
    print("LIMITATION: AppArmor profile loading cannot be verified in this environment.")
    print("Use a compatible Linux host with AppArmor enabled to test enforcement.")
    raise SystemExit(2)

result = subprocess.run(
    ["sudo", "apparmor_parser", "-r", str(profile)],
    check=False
)
raise SystemExit(result.returncode)
