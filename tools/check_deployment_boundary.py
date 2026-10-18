"""Keep production publication and credentials in the private controller."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
for retired in (".github/workflows/deploy-production.yml", ".github/hetzner-release.json"):
    if (ROOT / retired).exists():
        raise SystemExit(f"Retired application release surface reintroduced: {retired}")
for workflow in (ROOT / ".github/workflows").glob("*.y*ml"):
    text = workflow.read_text(encoding="utf-8")
    if re.search(r"HetznerReleaseGateway|id-token:\s*write|HETZNER_|DEPLOY_(?:HOST|USER|PATH|KEY)|SSH_PRIVATE_KEY|secrets:\s*inherit", text, re.IGNORECASE):
        raise SystemExit(f"Application CI must not publish releases or hold deployment credentials: {workflow.name}")
print("Private deployment controller boundary passed")
